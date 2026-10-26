#!/usr/bin/env python3
"""Offline, dependency-free validation of Open Collection's Markdown catalog.

Does not check remote URLs, copyright, software security, licenses or pricing.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, parse_qsl

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_CATEGORIES = [
    "01-saas-and-starters",
    "02-design-and-creative",
    "03-web-development",
    "04-web-components",
    "05-mobile-applications",
    "06-ai-and-machine-learning",
    "07-databases-and-storage",
    "08-crm-and-sales",
    "09-erp-and-enterprise",
    "10-finance-and-payments",
    "11-ecommerce",
    "12-self-hosted",
    "13-devops-and-cloud",
    "14-cybersecurity",
    "15-apis-and-sdks",
    "16-automation-and-nocode",
    "17-data-and-analytics",
    "18-content-and-marketing",
    "19-collaboration",
    "20-desktop-and-utilities",
    "21-hardware-and-iot",
    "22-gaming-and-media",
    "23-learning-and-research",
    "24-awesome-collections",
]
ENTRY = re.compile(r"^- \[([^\]]+)\]\((https://[^\s)]+)\) — (.+)$")
TRACKING_KEYS = ("utm_", "ref", "affiliate", "aff_id", "fbclid", "gclid")
errors: list[str] = []
seen: dict[str, tuple[str, int]] = {}
entry_count = 0


def normalize(url: str) -> str:
    p = urlsplit(url.strip())
    host = (p.hostname or "").lower()
    path = p.path.rstrip("/")
    if host == "github.com" and path.endswith(".git"):
        path = path[:-4]
    return urlunsplit((p.scheme.lower(), host, path.lower(), "", ""))


for shortname in EXPECTED_CATEGORIES:
    path = ROOT / "catalog" / (shortname + ".md")
    if not path.is_file():
        errors.append(f"Missing category: {path.relative_to(ROOT)}")
        continue
    content = path.read_text(encoding="utf-8")
    count = 0
    for number, line in enumerate(content.splitlines(), start=1):
        if not line.startswith("- "):
            continue
        match = ENTRY.fullmatch(line)
        if not match:
            errors.append(f"{path.relative_to(ROOT)}:{number} entry format invalid")
            continue
        name, url, description = match.groups()
        if len(name.strip()) < 2 or len(description.strip()) < 14:
            errors.append(f"{path.relative_to(ROOT)}:{number} too little detail")
        parsed = urlsplit(url)
        if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
            errors.append(f"{path.relative_to(ROOT)}:{number} malformed/suspicious URL")
        if parsed.query:
            query_keys = [key.lower() for key, _ in parse_qsl(parsed.query)]
            if any(key.startswith(TRACKING_KEYS) for key in query_keys):
                errors.append(f"{path.relative_to(ROOT)}:{number} tracking/referral parameter")
        key = normalize(url)
        if key in seen:
            prior_path, prior_line = seen[key]
            errors.append(f"{path.relative_to(ROOT)}:{number} duplicate URL (also {prior_path}:{prior_line})")
        else:
            seen[key] = (str(path.relative_to(ROOT)), number)
        count += 1
        entry_count += 1
    if count == 0:
        errors.append(f"Empty category: {path.relative_to(ROOT)}")

for lng in ("README.md", "README.ru.md"):
    text = (ROOT / lng).read_text(encoding="utf-8")
    for cat in EXPECTED_CATEGORIES:
        if f"(catalog/{cat}.md)" not in text:
            errors.append(f"{lng} lacks catalog/{cat}.md")

for unexpected in (ROOT / "catalog").glob("*.md"):
    if unexpected.stem not in EXPECTED_CATEGORIES:
        errors.append(f"Undeclared category: {unexpected.relative_to(ROOT)}")

if errors:
    print("FAIL — catalog validation")
    for message in errors:
        print(f"  - {message}")
    sys.exit(1)

print(f"PASS — {entry_count} listed resources across {len(EXPECTED_CATEGORIES)} categories (offline structure only)")
