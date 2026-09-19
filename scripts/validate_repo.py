#!/usr/bin/env python3
"""Repo-local integrity checks for the marius93rm photography portfolio.

The goal is not to prove every sentence in the docs. The goal is to catch
high-signal drift between the canonical files:

- .codex/agents/*.toml
- .agents/skills/*/SKILL.md
- AGENTS.md
- README.md
- docs/agent-catalog.md
- the static HTML pages
- .gitignore
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlparse
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
REPO_BLOB_PREFIX = "/marius93rm/marius93rm.github.io/blob/main/"

AGENT_REQUIRED_FIELDS = {
    "name",
    "description",
    "model",
    "model_reasoning_effort",
    "sandbox_mode",
    "developer_instructions",
}

ALLOWED_REASONING = {"low", "medium", "high"}
ALLOWED_SANDBOX = {"read-only", "workspace-write"}
ALLOWED_MODELS = {"gpt-5.6-sol", "gpt-5.6-terra", "gpt-5.6-luna"}
MODEL_DISPLAY_ORDER = ("gpt-5.6-sol", "gpt-5.6-terra", "gpt-5.6-luna")
BROWSER_SKILL_MARKERS = {
    'mcp__node_repl__js',
    'scripts/browser-client.mjs',
    'agent.browsers.get("iab")',
    'browser.tabs.selected()',
    'browser.tabs.new()',
}

EXPECTED_SITE_METADATA = {
    "index.html": {
        "title": "Marius | Photographer for Events, Portraits & Motorcycles",
        "description": (
            "Event, portrait, motorcycle and automotive photography by Marius in Rome, Brașov and beyond. "
            "View the portfolio or enquire about your project."
        ),
        "canonical": "https://marius93rm.github.io/",
        "current": "index.html",
    },
    "people.html": {
        "title": "People & Portrait Photography in Rome | Marius",
        "description": (
            "Candid event coverage and portrait photography by Marius in Rome, Brașov and beyond. Explore people, "
            "artists and live moments, then discuss your project."
        ),
        "canonical": "https://marius93rm.github.io/people.html",
        "current": "people.html",
    },
    "wheels.html": {
        "title": "Motorcycle & Automotive Photography | Marius",
        "description": (
            "Motorcycle and automotive photography by Marius in Rome, Brașov and beyond. Explore road, workshop "
            "and action photographs of bikes and cars, then enquire."
        ),
        "canonical": "https://marius93rm.github.io/wheels.html",
        "current": "wheels.html",
    },
    "world.html": {
        "title": "Travel, Landscape & Street Photography | Marius",
        "description": (
            "Travel, landscape and street photography by Marius, with photographs of Rome, architecture, coastlines, "
            "mountains and everyday life. Explore the collection."
        ),
        "canonical": "https://marius93rm.github.io/world.html",
        "current": "world.html",
    },
    "contact.html": {
        "title": "Contact Marius | Photographer in Rome & Brașov",
        "description": (
            "Contact Marius for event, portrait, motorcycle or automotive photography in Rome, Brașov and beyond. "
            "Include your date, location and project details."
        ),
        "canonical": "https://marius93rm.github.io/contact.html",
        "current": "contact.html",
    },
}


@dataclass(frozen=True)
class CheckResult:
    path: str
    message: str


class LocalHtmlParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.links: list[tuple[str, str]] = []
        self.images: list[dict[str, str]] = []
        self.anchors: list[dict[str, object]] = []
        self.controls: list[tuple[str, dict[str, str]]] = []
        self.labels_for: set[str] = set()
        self.nav_links: list[dict[str, str]] = []
        self.preloaded_images: list[str] = []
        self.canonicals: list[str] = []
        self.descriptions: list[str] = []
        self.title_parts: list[str] = []
        self._anchor_stack: list[int] = []
        self._in_title = False
        self._nav_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key: value or "" for key, value in attrs}
        if "id" in attr_map:
            self.ids.add(attr_map["id"])
        if "href" in attr_map:
            self.links.append((tag, attr_map["href"]))
        if "src" in attr_map:
            self.links.append((tag, attr_map["src"]))
        if tag == "img":
            self.images.append(attr_map)
        if tag == "title":
            self._in_title = True
        if tag == "meta" and attr_map.get("name") == "description":
            self.descriptions.append(attr_map.get("content", ""))
        if tag == "link":
            rel_values = attr_map.get("rel", "").split()
            if "canonical" in rel_values:
                self.canonicals.append(attr_map.get("href", ""))
            if "preload" in rel_values and attr_map.get("as") == "image":
                self.preloaded_images.append(attr_map.get("href", ""))
        if tag == "nav":
            self._nav_depth += 1
        if tag == "a":
            self.anchors.append({"attrs": attr_map, "text": []})
            self._anchor_stack.append(len(self.anchors) - 1)
            if self._nav_depth:
                self.nav_links.append(attr_map)
        if tag in {"input", "textarea", "select", "button"}:
            self.controls.append((tag, attr_map))
        if tag == "label" and attr_map.get("for"):
            self.labels_for.add(attr_map["for"])

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        if tag == "nav" and self._nav_depth:
            self._nav_depth -= 1
        if tag == "a" and self._anchor_stack:
            self._anchor_stack.pop()

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_parts.append(data)
        if self._anchor_stack:
            text_parts = self.anchors[self._anchor_stack[-1]]["text"]
            assert isinstance(text_parts, list)
            text_parts.append(data)

    @property
    def title(self) -> str:
        return "".join(self.title_parts).strip()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def fail(failures: list[CheckResult], path: str | Path, message: str) -> None:
    failures.append(CheckResult(rel(path) if isinstance(path, Path) else path, message))


def parse_simple_toml(text: str) -> dict[str, str]:
    """Parse the simple top-level string assignments used by agent TOML files."""
    data: dict[str, str] = {}
    lines = text.splitlines()
    index = 0

    while index < len(lines):
        line = lines[index].strip()
        index += 1

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()

        if value.startswith('"""'):
            collected: list[str] = []
            value = value[3:]
            if value.endswith('"""'):
                data[key] = value[:-3]
                continue
            collected.append(value)
            while index < len(lines):
                current = lines[index]
                index += 1
                if current.rstrip().endswith('"""'):
                    collected.append(current.rstrip()[:-3])
                    break
                collected.append(current)
            data[key] = "\n".join(collected).strip()
            continue

        match = re.fullmatch(r'"(.*)"', value)
        if match:
            data[key] = match.group(1)

    return data


def parse_skill_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    frontmatter: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()

    return frontmatter


def find_agent_files() -> list[Path]:
    return sorted((ROOT / ".codex" / "agents").glob("*.toml"))


def find_skill_files() -> list[Path]:
    return sorted((ROOT / ".agents" / "skills").glob("*/SKILL.md"))


def assert_text_mentions_all(
    failures: list[CheckResult],
    doc_path: Path,
    names: Iterable[str],
    label: str,
) -> None:
    text = read_text(doc_path)
    for name in names:
        if f"`{name}`" not in text and name not in text:
            fail(failures, doc_path, f"missing {label} reference: {name}")


def check_agents(failures: list[CheckResult]) -> list[str]:
    agent_files = find_agent_files()
    agent_names: list[str] = []

    if not agent_files:
        fail(failures, ".codex/agents", "no agent TOML files found")
        return agent_names

    for path in agent_files:
        data = parse_simple_toml(read_text(path))
        missing = sorted(AGENT_REQUIRED_FIELDS - data.keys())
        if missing:
            fail(failures, path, f"missing required fields: {', '.join(missing)}")
            continue

        expected_name = path.stem
        actual_name = data["name"]
        agent_names.append(actual_name)

        if actual_name != expected_name:
            fail(failures, path, f"name must match filename stem: expected {expected_name}, got {actual_name}")
        if data["model_reasoning_effort"] not in ALLOWED_REASONING:
            fail(failures, path, f"invalid model_reasoning_effort: {data['model_reasoning_effort']}")
        if data["sandbox_mode"] not in ALLOWED_SANDBOX:
            fail(failures, path, f"invalid sandbox_mode: {data['sandbox_mode']}")
        if data["model"] not in ALLOWED_MODELS:
            fail(failures, path, f"model should follow the repo GPT-5.6 routing, got {data['model']}")
        if len(data["developer_instructions"].split()) < 20:
            fail(failures, path, "developer_instructions look too short to guide the agent")

    return sorted(agent_names)


def check_skills(failures: list[CheckResult]) -> list[str]:
    skill_files = find_skill_files()
    skill_names: list[str] = []

    if not skill_files:
        fail(failures, ".agents/skills", "no SKILL.md files found")
        return skill_names

    for path in skill_files:
        frontmatter = parse_skill_frontmatter(read_text(path))
        expected_name = path.parent.name
        actual_name = frontmatter.get("name")

        if not actual_name:
            fail(failures, path, "missing frontmatter name")
            continue

        skill_names.append(actual_name)

        if actual_name != expected_name:
            fail(failures, path, f"name must match directory: expected {expected_name}, got {actual_name}")
        if not frontmatter.get("description"):
            fail(failures, path, "missing frontmatter description")

        if actual_name == "browser-integration":
            text = read_text(path)
            missing_markers = sorted(marker for marker in BROWSER_SKILL_MARKERS if marker not in text)
            if missing_markers:
                fail(failures, path, f"missing browser integration markers: {', '.join(missing_markers)}")

    return sorted(skill_names)


def check_docs(failures: list[CheckResult], agent_names: list[str], skill_names: list[str]) -> None:
    agents_md = ROOT / "AGENTS.md"
    readme = ROOT / "README.md"
    catalog = ROOT / "docs" / "agent-catalog.md"
    model_routing = ROOT / "docs" / "model-routing.md"

    for path in [agents_md, readme, catalog, model_routing]:
        if not path.exists():
            fail(failures, path, "required documentation file is missing")
            return

    assert_text_mentions_all(failures, catalog, agent_names, "agent")
    assert_text_mentions_all(failures, model_routing, agent_names, "agent")

    for model in sorted(ALLOWED_MODELS):
        if f"`{model}`" not in read_text(model_routing):
            fail(failures, model_routing, f"missing model routing reference: {model}")

    model_routing_text = read_text(model_routing)
    for agent_path in find_agent_files():
        data = parse_simple_toml(read_text(agent_path))
        model = data.get("model", "")
        name = data.get("name", agent_path.stem)
        row_pattern = rf"\| `{re.escape(model)}` \| [^\n]*`{re.escape(name)}`"
        if not re.search(row_pattern, model_routing_text):
            fail(failures, model_routing, f"agent routing does not match TOML: {name} -> {model}")

    assert_text_mentions_all(failures, catalog, skill_names, "skill")

    for entry in ["index.html", "assets/css/main.css", "assets/js/main.js", "scripts/validate_repo.py"]:
        if entry not in read_text(readme):
            fail(failures, readme, f"project documentation should mention `{entry}`")


def is_external_reference(value: str) -> bool:
    if not value:
        return True
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https", "mailto", "tel", "data"} and REPO_BLOB_PREFIX not in parsed.path


def repo_blob_path(value: str) -> Path | None:
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"}:
        return None
    if not parsed.netloc.endswith("github.com"):
        return None
    if REPO_BLOB_PREFIX not in parsed.path:
        return None
    raw_path = parsed.path.split(REPO_BLOB_PREFIX, 1)[1]
    return ROOT / unquote(raw_path)


def check_html(failures: list[CheckResult], agent_names: list[str], skill_names: list[str]) -> None:
    del agent_names, skill_names
    html_paths = sorted(ROOT.glob("*.html"))
    expected_pages = set(EXPECTED_SITE_METADATA)
    found_pages = {path.name for path in html_paths}

    for missing in sorted(expected_pages - found_pages):
        fail(failures, missing, "required site page is missing")

    for html_path in html_paths:
        parser = LocalHtmlParser()
        parser.feed(read_text(html_path))
        expected_metadata = EXPECTED_SITE_METADATA.get(html_path.name)

        for tag, value in parser.links:
            if value == "#":
                continue
            if not value or value.startswith("#"):
                if value.startswith("#") and value[1:] not in parser.ids:
                    fail(failures, html_path, f"broken anchor link `{value}` in <{tag}>")
                continue

            blob_path = repo_blob_path(value)
            if blob_path is not None:
                if not blob_path.exists():
                    fail(failures, html_path, f"GitHub blob link points to missing path: {rel(blob_path)}")
                continue

            if is_external_reference(value):
                continue

            local_path = ROOT / value.split("#", 1)[0]
            if not local_path.exists():
                fail(failures, html_path, f"local <{tag}> reference points to missing path: {value}")

        for image in parser.images:
            src = image.get("src", "")
            alt = image.get("alt", "")
            if src and not alt.strip():
                fail(failures, html_path, f"image `{src}` is missing alt text")
            for dimension in ("width", "height"):
                value = image.get(dimension, "")
                if not value.isdigit() or int(value) <= 0:
                    fail(failures, html_path, f"image `{src}` needs a positive explicit {dimension}")

        for anchor in parser.anchors:
            attrs = anchor["attrs"]
            text_parts = anchor["text"]
            assert isinstance(attrs, dict)
            assert isinstance(text_parts, list)
            accessible_name = (
                str(attrs.get("aria-label", "")).strip()
                or "".join(str(part) for part in text_parts).strip()
                or str(attrs.get("title", "")).strip()
            )
            if not accessible_name:
                fail(failures, html_path, f"link `{attrs.get('href', '')}` has no accessible name")

            href = str(attrs.get("href", ""))
            if href.startswith("tel:"):
                href_digits = re.sub(r"\D", "", href.removeprefix("tel:"))
                text_digits = re.sub(r"\D", "", "".join(str(part) for part in text_parts))
                if href_digits != text_digits:
                    fail(failures, html_path, f"telephone link `{href}` does not match its visible number")

        for tag, attrs in parser.controls:
            if tag == "button":
                continue
            if tag == "input" and attrs.get("type", "text") in {"hidden", "submit", "button", "reset", "image"}:
                continue
            control_id = attrs.get("id", "")
            if not control_id or control_id not in parser.labels_for:
                fail(failures, html_path, f"form control `{attrs.get('name', tag)}` needs an associated label")

        skip_links = [
            anchor for anchor in parser.anchors
            if "skip-link" in str(anchor["attrs"].get("class", "")).split()
            and anchor["attrs"].get("href") == "#main-content"
        ]
        if len(skip_links) != 1 or "main-content" not in parser.ids:
            fail(failures, html_path, "page needs one skip link targeting `#main-content`")

        current_links = [link for link in parser.nav_links if link.get("aria-current") == "page"]
        if len(current_links) != 1:
            fail(failures, html_path, "primary navigation needs exactly one `aria-current=page` link")
        elif expected_metadata:
            current_link = current_links[0]
            if current_link.get("href") != expected_metadata["current"]:
                fail(failures, html_path, "primary navigation marks the wrong page as current")
            if "active" not in current_link.get("class", "").split():
                fail(failures, html_path, "current navigation link also needs the `active` class")

        mobile_toggles = [
            attrs for tag, attrs in parser.controls
            if tag == "button" and "mobile-nav-toggle" in attrs.get("class", "").split()
        ]
        if len(mobile_toggles) != 1:
            fail(failures, html_path, "page needs exactly one mobile navigation toggle")
        else:
            controlled_id = mobile_toggles[0].get("aria-controls", "")
            if not controlled_id or controlled_id not in parser.ids:
                fail(failures, html_path, "mobile navigation toggle must control an existing element")

        gallery_images = [
            image for image in parser.images
            if image.get("src", "").startswith("assets/img/thumbs/")
            and "/" in image.get("src", "").removeprefix("assets/img/thumbs/")
        ]
        if gallery_images:
            first_gallery_image = gallery_images[0]
            first_src = first_gallery_image.get("src", "")
            if first_gallery_image.get("loading") != "eager" or first_gallery_image.get("fetchpriority") != "high":
                fail(failures, html_path, f"first gallery image `{first_src}` must be eager and high priority")
            if parser.preloaded_images != [first_src]:
                fail(failures, html_path, f"page must preload only its first gallery image `{first_src}`")
            for image in gallery_images[1:]:
                if image.get("loading") != "lazy" or image.get("fetchpriority") == "high":
                    fail(failures, html_path, f"later gallery image `{image.get('src', '')}` must be lazy")

        if expected_metadata:
            if parser.title != expected_metadata["title"]:
                fail(failures, html_path, f"unexpected page title: `{parser.title}`")
            if parser.descriptions != [expected_metadata["description"]]:
                fail(failures, html_path, "page needs its expected unique meta description")
            if parser.canonicals != [expected_metadata["canonical"]]:
                fail(failures, html_path, "page needs its expected canonical URL")

        if html_path.name == "contact.html" and any("glightbox" in value for _, value in parser.links):
            fail(failures, html_path, "contact page should not load GLightbox assets")


def check_search_files(failures: list[CheckResult]) -> None:
    sitemap = ROOT / "sitemap.xml"
    robots = ROOT / "robots.txt"
    expected_urls = {metadata["canonical"] for metadata in EXPECTED_SITE_METADATA.values()}

    if not sitemap.exists():
        fail(failures, sitemap, "required sitemap is missing")
    else:
        try:
            root = ElementTree.fromstring(read_text(sitemap))
        except ElementTree.ParseError as error:
            fail(failures, sitemap, f"invalid XML: {error}")
        else:
            sitemap_urls = {node.text.strip() for node in root.findall(".//{*}loc") if node.text}
            if sitemap_urls != expected_urls:
                fail(failures, sitemap, "sitemap URLs do not match the five canonical site URLs")

    if not robots.exists():
        fail(failures, robots, "required robots file is missing")
    else:
        robots_text = read_text(robots)
        for directive in (
            "User-agent: *",
            "Allow: /",
            "Sitemap: https://marius93rm.github.io/sitemap.xml",
        ):
            if directive not in robots_text:
                fail(failures, robots, f"missing directive: {directive}")


def check_gitignore(failures: list[CheckResult]) -> None:
    gitignore = ROOT / ".gitignore"
    if not gitignore.exists():
        fail(failures, gitignore, "required repository hygiene file is missing")
        return

    patterns = {
        line.strip()
        for line in read_text(gitignore).splitlines()
        if line.strip() and not line.startswith("#")
    }
    for required in {".DS_Store", "__pycache__/", "node_modules/", ".env"}:
        if required not in patterns:
            fail(failures, gitignore, f"missing required ignore pattern: {required}")


def run_checks() -> list[CheckResult]:
    failures: list[CheckResult] = []
    agent_names = check_agents(failures)
    skill_names = check_skills(failures)
    check_docs(failures, agent_names, skill_names)
    check_html(failures, agent_names, skill_names)
    check_search_files(failures)
    check_gitignore(failures)
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the photography portfolio and its repo-local agent setup.")
    parser.add_argument("--quiet", action="store_true", help="Only print failures.")
    args = parser.parse_args()

    failures = run_checks()

    if failures:
        print("Repo validation failed:\n")
        for item in failures:
            print(f"- {item.path}: {item.message}")
        return 1

    if not args.quiet:
        print("Portfolio validation passed.")
        print(f"- agents: {len(find_agent_files())}")
        print(f"- skills: {len(find_skill_files())}")
        print("- agent config, docs, accessibility, metadata, links, images, search files, and .gitignore checked")

    return 0


if __name__ == "__main__":
    sys.exit(main())
