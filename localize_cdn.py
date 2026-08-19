#!/usr/bin/env python3

import argparse
import re
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


CDN_URL_RE = re.compile(
    rb"https://(?:unpkg\.com|cdn\.jsdelivr\.net)/[A-Za-z0-9@%_+./?=&~-]+"
)
def download(url: str, destination: Path) -> None:
    request = Request(url, headers={"User-Agent": "msys2.org site builder"})
    with urlopen(request, timeout=120) as response:
        content = response.read()

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(content)


def local_path(site_dir: Path, url: str) -> Path:
    parsed = urlsplit(url)
    path = parsed.path.lstrip("/")
    if not path or path.endswith("/"):
        raise ValueError(f"CDN URL does not identify a file: {url}")
    if parsed.netloc == "unpkg.com" and "/" not in path:
        path += "/index.js"
    return site_dir / "assets" / "vendor" / parsed.netloc / path


def root_relative(site_dir: Path, path: Path) -> str:
    return "/" + path.relative_to(site_dir).as_posix()


def localize(site_dir: Path) -> None:
    javascript_files = sorted(site_dir.rglob("*.js"))
    if not javascript_files:
        raise FileNotFoundError(f"No JavaScript files found in {site_dir}")

    references = {
        match.group().decode("ascii")
        for path in javascript_files
        for match in CDN_URL_RE.finditer(path.read_bytes())
    }
    replacements = {}
    for url in sorted(references):
        if "pyodide" in urlsplit(url).path:
            continue

        destination = local_path(site_dir, url)
        download(url, destination)
        replacements[url] = root_relative(site_dir, destination)

    for path in javascript_files:
        content = path.read_bytes()
        for url, replacement in replacements.items():
            content = content.replace(url.encode(), replacement.encode())
        path.write_bytes(content)

    print(f"Localized {len(replacements)} CDN references")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download CDN assets referenced by generated JavaScript"
    )
    parser.add_argument("site_dir", nargs="?", default="site", type=Path)
    args = parser.parse_args()
    localize(args.site_dir.resolve())


if __name__ == "__main__":
    main()
