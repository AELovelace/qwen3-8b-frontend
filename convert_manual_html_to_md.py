#!/usr/bin/env python3
"""Convert GameMaker manual HTML files to Markdown for AI ingestion.

The script recursively scans an input directory for .htm/.html files,
converts them to Markdown, and writes mirrored .md files to an output tree.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as html_to_markdown

HTML_SUFFIXES = {".htm", ".html"}
REMOVE_TAGS = {
    "script",
    "style",
    "noscript",
    "iframe",
    "canvas",
    "svg",
    "object",
}


def iter_html_files(root: Path) -> list[Path]:
    """Return all HTML files under root, sorted for stable processing."""
    files = [
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in HTML_SUFFIXES
    ]
    return sorted(files)


def _rewrite_href_to_markdown(href: str) -> str:
    """Rewrite local manual links from .htm/.html to .md."""
    href = href.strip()
    if not href:
        return href

    lower = href.lower()
    if lower.startswith(("http://", "https://", "mailto:", "tel:", "#")):
        return href

    match = re.match(r"^(.*?)(\?[^#]*)?(#.*)?$", href)
    if not match:
        return href

    path_part = match.group(1) or ""
    query_part = match.group(2) or ""
    fragment_part = match.group(3) or ""

    if path_part.lower().endswith((".htm", ".html")):
        path_part = Path(path_part).with_suffix(".md").as_posix()

    return f"{path_part}{query_part}{fragment_part}"


def clean_and_convert_html(html_text: str) -> str:
    """Convert one HTML document string to cleaned Markdown."""
    soup = BeautifulSoup(html_text, "html.parser")

    for tag_name in REMOVE_TAGS:
        for node in soup.find_all(tag_name):
            node.decompose()

    for link in soup.find_all("a", href=True):
        link["href"] = _rewrite_href_to_markdown(link["href"])

    source = soup.body if soup.body is not None else soup
    markdown = html_to_markdown(
        str(source),
        heading_style="ATX",
        bullets="-",
        strip=["span", "div", "font", "xml", "meta", "link"],
    )

    markdown = markdown.replace("\r\n", "\n").replace("\xa0", " ")

    # Remove any raw HTML that might remain after conversion.
    markdown = re.sub(r"</?[^>\n]+>", "", markdown)

    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip() + "\n"


def convert_tree(input_dir: Path, output_dir: Path, overwrite: bool) -> tuple[int, int]:
    """Convert all HTML files in input_dir and write Markdown to output_dir."""
    html_files = iter_html_files(input_dir)
    converted = 0
    skipped = 0

    for src in html_files:
        rel_path = src.relative_to(input_dir)
        dest = (output_dir / rel_path).with_suffix(".md")

        if dest.exists() and not overwrite:
            skipped += 1
            continue

        raw_html = src.read_text(encoding="utf-8", errors="ignore")
        markdown = clean_and_convert_html(raw_html)

        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(markdown, encoding="utf-8")
        converted += 1

    return converted, skipped


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert all HTML files in gml/Manual to Markdown files."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("gml/Manual"),
        help="Directory containing source HTML files.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("gml/Manual_md"),
        help="Directory where converted Markdown files will be written.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite Markdown files that already exist in output-dir.",
    )

    args = parser.parse_args()
    input_dir = args.input_dir.resolve()
    output_dir = args.output_dir.resolve()

    if not input_dir.exists() or not input_dir.is_dir():
        raise SystemExit(f"Input directory does not exist or is not a directory: {input_dir}")

    converted, skipped = convert_tree(input_dir, output_dir, overwrite=args.overwrite)

    print(f"Input directory : {input_dir}")
    print(f"Output directory: {output_dir}")
    print(f"Converted files : {converted}")
    print(f"Skipped files   : {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
