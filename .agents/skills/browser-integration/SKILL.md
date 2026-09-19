---
name: browser-integration
description: Use before browser-driven work to select the current session's lane: Paseo by default, explicit Chrome, or explicit Codex Browser; not for HTTP-only research.
---

# Browser Integration

The browsers belong to different host/session contexts. Do not switch browser lanes automatically or imply an in-session fallback.

## Backend Selection

Choose exactly one lane for the task:

1. **Google Chrome — explicit.** Use only for `@Chrome`, a mentioned Chrome tab, or an explicit need for its real profile. It requires OpenAI's official extension and a Chrome client advertised to this chat.
2. **Codex built-in browser — explicit.** Select this lane only for `@Browser` or an explicit request for the Codex browser.
3. **Paseo native browser — default.** Without an explicit choice, use concrete `mcp__paseo__browser_*` tools when exposed. Do not load the Codex browser runtime in this lane.

If the lane is unavailable, report its missing prerequisite and required session. Do not silently substitute another browser.

Do not use standalone browser stacks unless explicitly requested.

## Paseo Fast Path

1. Call `mcp__paseo__browser_list_tabs`; reuse the intended tab. If none exists, create one with `mcp__paseo__browser_new_tab`; this is expected state.
2. Navigate only when needed, then call `mcp__paseo__browser_snapshot`.
3. Build actions only from refs in the latest snapshot. Refs expire after page changes.
4. Serialize calls per tab. After an action, check one authoritative state; use screenshots for visual evidence.

If no Paseo browser host is connected, read [references/recovery.md](references/recovery.md), retry Paseo once, then stop this lane with a precise recovery action.

## Codex Built-in or Chrome Path

Read the installed Codex desktop `browser` skill completely. Resolve the plugin root containing `skills/browser/SKILL.md` and `scripts/browser-client.mjs`; never hard-code its version or user path.

This lane requires a concrete sandbox policy. If permissions are disabled/full-access, do not bootstrap it: request a new Default Permissions chat with `@Chrome` or `@Browser`, matching the selected lane. Otherwise call `mcp__node_repl__js` once through the host's supported surface:

```js
if (!globalThis.agent) {
  const { setupBrowserRuntime } = await import("<absolute-plugin-root>/scripts/browser-client.mjs");
  await setupBrowserRuntime({ globals: globalThis });
}
globalThis.availableBrowsers = await agent.browsers.list();
globalThis.chromeInfo = availableBrowsers.find(info => info.type === "extension" && /chrome/i.test(`${info.name} ${JSON.stringify(info.metadata || {})}`));
// @Chrome, only if chromeInfo exists:
// if (!globalThis.browser) globalThis.browser = await agent.browsers.get(chromeInfo.id);
// @Browser instead:
// if (!globalThis.browser) globalThis.browser = await agent.browsers.get("iab");
await browser.nameSession("🔎 short task name");
if (typeof tab === "undefined") globalThis.tab = await browser.tabs.selected();
if (!globalThis.tab) globalThis.tab = await browser.tabs.new();
console.log({ browserId: browser.browserId, tabId: tab.id, url: await tab.url() });
```

For Chrome, require `chromeInfo`; installed or open Chrome is not proof of connection. If absent, follow recovery and keep the lane failed; never substitute `iab` while claiming Chrome.

Reuse `agent`, `browser`, and `tab`. After navigation or UI changes, take a fresh `tab.playwright.domSnapshot()`. Prefer test IDs, stable attributes or `href`, then scoped roles/text; call `count()` when uniqueness is unclear.

On a missing `sandboxPolicy`, connection failure, unavailable Chrome client, or stale state, follow only the matching case in [references/recovery.md](references/recovery.md). Retry recoverable state once inside the selected lane.

## Completion Evidence

Report the lane, target, decisive state, retry, and one recovery action for failures. Include the key screenshot for UI work when available.
