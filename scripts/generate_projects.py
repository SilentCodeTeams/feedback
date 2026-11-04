#!/usr/bin/env python3
"""Generate the feedback project list from top-level project directories.

A project is any top-level directory that either contains a project.json file
or at least one of the standard feedback categories. Adding a directory is the
only step needed; the GitHub workflow regenerates docs/projects.json.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "projects.json"
CATEGORIES = ("bug", "feature", "language", "question")
EXCLUDED = {".git", ".github", "docs", "lang", "scripts"}
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def load_manifest(project_dir: Path) -> dict:
    manifest_path = project_dir / "project.json"
    if not manifest_path.is_file():
        return {}
    with manifest_path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{manifest_path}: expected a JSON object")
    return value


def discover() -> list[dict]:
    projects = []
    seen_slugs = set()
    for project_dir in sorted(ROOT.iterdir(), key=lambda path: path.name.lower()):
        if not project_dir.is_dir() or project_dir.name in EXCLUDED or project_dir.name.startswith("."):
            continue
        categories = [name for name in CATEGORIES if (project_dir / name).is_dir()]
        try:
            manifest = load_manifest(project_dir)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            raise SystemExit(f"invalid project manifest: {exc}") from exc
        if not categories and not manifest:
            continue
        if manifest.get("hidden") or manifest.get("status") == "archived":
            continue
        name = str(manifest.get("name") or project_dir.name).strip()
        slug = str(manifest.get("slug") or project_dir.name.lower()).strip()
        if not name:
            raise SystemExit(f"{project_dir.name}: name must not be empty")
        if not SLUG_RE.fullmatch(slug):
            raise SystemExit(f"{project_dir.name}: invalid slug {slug!r}")
        if slug in seen_slugs:
            raise SystemExit(f"duplicate project slug: {slug}")
        seen_slugs.add(slug)
        projects.append({
            "name": name,
            "slug": slug,
            "description": str(manifest.get("description") or "").strip(),
            "status": str(manifest.get("status") or "active"),
            "order": int(manifest.get("order", 1000)),
            "path": project_dir.name,
            "categories": categories,
        })
    projects.sort(key=lambda item: (item["order"], item["name"].casefold()))
    return projects


def main() -> int:
    payload = {"version": 1, "projects": discover()}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(payload['projects'])} project(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
