#!/usr/bin/env python3
"""Generate a markdown radar of recent PBJ-worthy news candidates."""

from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config" / "sources.json"


@dataclass
class Item:
    source: str
    category: str
    title: str
    link: str
    published: dt.datetime | None
    summary: str
    score: int
    matches: list[str]


def strip_html(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    value = html.unescape(value)
    value = value.translate(
        str.maketrans(
            {
                "\u2018": "'",
                "\u2019": "'",
                "\u201c": '"',
                "\u201d": '"',
                "\u2013": "-",
                "\u2014": "-",
                "\u2026": "...",
                "\u00a0": " ",
            }
        )
    )
    value = value.encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"\s+", " ", value).strip()
    return value


def parse_date(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    value = value.strip()
    try:
        parsed = email.utils.parsedate_to_datetime(value)
        if parsed.tzinfo:
            return parsed.astimezone(dt.timezone.utc).replace(tzinfo=None)
        return parsed
    except (TypeError, ValueError):
        pass
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(
            dt.timezone.utc
        ).replace(tzinfo=None)
    except ValueError:
        return None


def child_text(node: ET.Element, names: tuple[str, ...]) -> str:
    for name in names:
        found = node.find(name)
        if found is not None and found.text:
            return found.text.strip()
    for child in node:
        local = child.tag.rsplit("}", 1)[-1]
        if local in names and child.text:
            return child.text.strip()
    return ""


def entry_link(node: ET.Element) -> str:
    direct = child_text(node, ("link",))
    if direct:
        return direct
    for child in node:
        local = child.tag.rsplit("}", 1)[-1]
        if local == "link":
            href = child.attrib.get("href")
            if href:
                return href
    return ""


def entries(root: ET.Element) -> list[ET.Element]:
    rss_items = root.findall(".//item")
    if rss_items:
        return rss_items
    return [node for node in root.iter() if node.tag.rsplit("}", 1)[-1] == "entry"]


def fetch(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "PBJ-News-Scanner/1.0 (+https://github.com/gentic/pbj)"
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read()


def score_item(
    title: str,
    summary: str,
    published: dt.datetime | None,
    keywords: list[str],
    source_weight: int,
    now: dt.datetime,
) -> tuple[int, list[str]]:
    haystack = f"{title} {summary}".lower()
    matches = sorted({kw for kw in keywords if kw.lower() in haystack})
    score = source_weight + len(matches)
    if published:
        age_days = max((now - published).days, 0)
        if age_days <= 2:
            score += 5
        elif age_days <= 7:
            score += 3
        elif age_days <= 14:
            score += 1
    if any(word in haystack for word in ("agent", "agentic", "mcp", "workflow")):
        score += 3
    if any(word in haystack for word in ("shop", "commerce", "retail", "merchant")):
        score += 2
    if any(word in haystack for word in ("creator", "affiliate", "youtube")):
        score += 2
    return score, matches


def collect(config: dict, days: int, now: dt.datetime) -> tuple[list[Item], list[str]]:
    keywords = config["keywords"]
    cutoff = now - dt.timedelta(days=days)
    items: list[Item] = []
    errors: list[str] = []

    for feed in config["feeds"]:
        try:
            root = ET.fromstring(fetch(feed["url"]))
        except Exception as exc:  # noqa: BLE001 - show feed failures in markdown
            errors.append(f"{feed['name']}: {exc}")
            continue

        for node in entries(root):
            title = strip_html(child_text(node, ("title",)))
            link = entry_link(node)
            published = parse_date(
                child_text(node, ("pubDate", "published", "updated", "dc:date"))
            )
            summary = strip_html(
                child_text(node, ("description", "summary", "content"))
            )
            if not title or not link:
                continue
            if published and published < cutoff:
                continue
            score, matches = score_item(
                title, summary, published, keywords, int(feed.get("weight", 1)), now
            )
            if matches:
                items.append(
                    Item(
                        source=feed["name"],
                        category=feed.get("category", "news"),
                        title=title,
                        link=link,
                        published=published,
                        summary=summary,
                        score=score,
                        matches=matches,
                    )
                )

    deduped: dict[str, Item] = {}
    for item in items:
        key = re.sub(r"\W+", "", item.link.lower()) or re.sub(
            r"\W+", "", item.title.lower()
        )
        current = deduped.get(key)
        if current is None or item.score > current.score:
            deduped[key] = item

    return sorted(deduped.values(), key=lambda item: item.score, reverse=True), errors


def format_date(value: dt.datetime | None) -> str:
    if not value:
        return "undated"
    return value.strftime("%Y-%m-%d")


def write_markdown(
    items: list[Item],
    errors: list[str],
    config: dict,
    days: int,
    limit: int,
    out_path: Path,
    now: dt.datetime,
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = [
        f"# PBJ News Scan - {now.strftime('%Y-%m-%d')}",
        "",
        f"Window: last {days} days",
        "",
        "## Top Candidates",
        "",
    ]

    for index, item in enumerate(items[:limit], start=1):
        summary = item.summary[:260].rstrip()
        if len(item.summary) > 260:
            summary += "..."
        lines.extend(
            [
                f"### {index}. {item.title}",
                "",
                f"- Source: {item.source} ({item.category})",
                f"- Published: {format_date(item.published)}",
                f"- Score: {item.score}",
                f"- Matched: {', '.join(item.matches)}",
                f"- Link: {item.link}",
            ]
        )
        if summary:
            lines.append(f"- Summary: {summary}")
        lines.extend(
            [
                "- PBJ angle:",
                "- Tension/debate:",
                "- Emotional hook:",
                "- Clip potential:",
                "- Visual anchors:",
                "- Questions:",
                "",
            ]
        )

    lines.extend(["## Manual Watchlist", ""])
    for url in config.get("manual_watchlist", []):
        lines.append(f"- {url}")
    lines.append("")

    if errors:
        lines.extend(["## Feed Errors", ""])
        for error in errors:
            lines.append(f"- {error}")
        lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--days", type=int, default=10)
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    now = dt.datetime.now()
    items, errors = collect(config, args.days, now)
    out_path = args.out or ROOT / "research" / f"{now.strftime('%Y-%m-%d')}-news-scan.md"
    write_markdown(items, errors, config, args.days, args.limit, out_path, now)
    print(f"Wrote {out_path}")
    print(f"Candidates: {min(len(items), args.limit)} shown / {len(items)} collected")
    if errors:
        print(f"Feed errors: {len(errors)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
