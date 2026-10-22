#!/usr/bin/env python3
"""Small standard-library checks; these do not validate scientific claims."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CATALOGS = ("README.md", "docs/related-work.md")
DOCS = (*CATALOGS, "CONTRIBUTING.md", ".github/pull_request_template.md")


def prose(text):
    """Exclude fenced examples from structural link checks."""
    return re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.M | re.S)


def anchors(text):
    result, seen = set(), {}
    for heading in re.findall(r"^#{1,6}\s+(.+)$", prose(text), re.M):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        result.add(slug if count == 0 else f"{slug}-{count}")
    result.update(re.findall(r'<a\s+id="([^"]+)"', text))
    return result


def identity(url):
    arxiv = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", url)
    return "arxiv:" + arxiv[1] if arxiv else url.rstrip("/")


def probe(url):
    try:
        request = Request(url, headers={"User-Agent": "AwesomeAutoloop-LinkCheck/1.0"})
        with urlopen(request, timeout=25) as response:
            prefix = response.read(4096).decode("utf-8", errors="ignore").lower()
            if "verifying your browser" in prefix or "just a moment..." in prefix:
                return url, "browser challenge; inspect manually"
            return url, None
    except (HTTPError, URLError, TimeoutError, OSError, ValueError) as error:
        return url, str(error)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--online", action="store_true", help="GET-probe external URLs")
    args = parser.parse_args()
    errors, urls = [], set()
    for name in DOCS:
        path = ROOT / name
        text = prose(path.read_text())
        urls.update(re.findall(r'https?://[^\s)<>"\]]+', text))
        for target in re.findall(r"\]\(([^\s)]+)\)", text):
            if urlsplit(target).scheme:
                continue
            filepart, _, fragment = unquote(target).partition("#")
            destination = path.parent / filepart if filepart else path
            if not destination.is_file():
                errors.append(f"{name}: missing local file {target}")
            elif fragment and destination.suffix == ".md":
                if fragment not in anchors(destination.read_text()):
                    errors.append(f"{name}: missing anchor {target}")
    start, end = "<!-- literature:start -->", "<!-- literature:end -->"
    papers, seen = [], set()
    for name in CATALOGS:
        catalog = (ROOT / name).read_text()
        if (catalog.count(start) != 1 or catalog.count(end) != 1
                or catalog.index(start) > catalog.index(end)):
            errors.append(f"{name}: expected one ordered pair of literature markers")
            continue
        literature = catalog.split(start)[1].split(end)[0]
        entries = re.findall(r"^- \*\*\[.*?\]\(([^)]+)\)", literature, re.M)
        papers.extend(entries)
        for url in entries:
            key = identity(url)
            if key in seen:
                errors.append(f"{name}: duplicate detailed paper {key}")
            seen.add(key)
    for error in errors:
        print("ERROR:", error)
    print(f"Structural check: {len(papers)} literature records, {len(urls)} external URLs, {len(errors)} errors.")
    warnings = []
    if args.online:
        with ThreadPoolExecutor(max_workers=6) as pool:
            warnings = [(url, issue) for url, issue in pool.map(probe, sorted(urls)) if issue]
        for url, issue in warnings:
            print(f"REVIEW: {url}: {issue}")
        print(f"Online check: {len(urls)} probed, {len(warnings)} need manual review.")
    return 1 if errors else (2 if warnings else 0)


if __name__ == "__main__":
    sys.exit(main())
