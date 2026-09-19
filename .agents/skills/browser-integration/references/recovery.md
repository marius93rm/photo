# Browser Recovery

Read only the case matching the observed failure. Recovery stays inside the selected browser lane; changing lanes requires a new explicit user/session choice.

- **Paseo tools missing:** the agent did not receive the Paseo MCP toolset. Confirm **Settings → your host → Agents → Enable Paseo tools** and **Browser tools**, then reload or start a new Paseo agent. Do not invent tool names or switch lanes.
- **No Paseo browser host:** Paseo Desktop owns the browser host; the daemon alone is insufficient. Confirm the Desktop app is running and connected to the affected host, then retry `mcp__paseo__browser_list_tabs` once. If it still fails, report that host connection as the blocker.
- **Tools enabled after agent start:** existing agents may retain their original tool catalog. Reload the agent if supported; otherwise start a new agent in the same workspace and use the Paseo lane there.
- **No Paseo tab:** create one with `mcp__paseo__browser_new_tab`; this is expected state.
- **Expired Paseo ref:** take one new snapshot and rebuild the action from its refs. Never reuse an expired ref.
- **Codex `sandboxPolicy` missing:** do not retry the runtime in the same chat. Full-access/disabled permissions do not support this bridge; report the exact cause and require a new Default Permissions chat with the same explicit `@Chrome` or `@Browser` selection.
- **Chrome client absent:** do not infer connection from a running browser or installed extension. In Codex/ChatGPT Desktop, update the app, open **Settings → Computer Use → Chrome**, confirm **Manage**, use the Chrome profile containing OpenAI's official extension, then start a new Default Permissions chat with `@Chrome`.
- **No selected Codex/Chrome tab:** create one with `browser.tabs.new()`; this is expected state.
- **Stale Codex/Chrome handle:** list tabs once and recover the intended tab by ID.
- **Identifier already declared:** reuse the existing binding or choose a fresh descriptive name; do not reset reflexively.
- **Locator count is `0` or greater than `1`:** take a fresh snapshot and build one stronger scoped locator. Never use `.first()` as a shortcut.
- **Repeated host connection error:** stop the selected lane after one retry. Report the lane, failed prerequisite, retry result, and the single next action; do not collapse distinct paths into “the browser does not work”.
- **User or extension interruption:** report it naturally and wait for direction.

Current setup references: [Paseo browser automation](https://paseo.sh/docs/browser) and [OpenAI's Chrome extension](https://learn.chatgpt.com/docs/chrome-extension).
