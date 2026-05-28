#!/usr/bin/env python3
"""Generate a markdown radar of recent PBJ-worthy news candidates."""

from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import gzip
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse


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
    signals: list[str]


class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        href = dict(attrs).get("href")
        if href:
            self._href = href
            self._text = []

    def handle_data(self, data: str) -> None:
        if self._href:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self._href:
            self.links.append((self._href, " ".join(self._text)))
            self._href = None
            self._text = []


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
        data = response.read()
        if data.startswith(b"\x1f\x8b"):
            return gzip.decompress(data)
        return data


def title_from_url(url: str) -> str:
    slug = urlparse(url).path.rstrip("/").split("/")[-1]
    slug = re.sub(r"\.(html?|php)$", "", slug)
    return strip_html(slug.replace("-", " ").replace("_", " ")).title()


def published_from_url(url: str) -> dt.datetime | None:
    path = urlparse(url).path
    numeric = re.search(r"/(20\d{2})/(\d{1,2})/(\d{1,2})(?:/|$)", path)
    if numeric:
        year, month, day = map(int, numeric.groups())
        try:
            return dt.datetime(year, month, day)
        except ValueError:
            return None
    dashed = re.search(r"(20\d{2})-(\d{1,2})-(\d{1,2})", path)
    if dashed:
        year, month, day = map(int, dashed.groups())
        try:
            return dt.datetime(year, month, day)
        except ValueError:
            return None
    month_name = re.search(r"/(20\d{2})/([A-Za-z]{3,9})/(\d{1,2})(?:/|$)", path)
    if month_name:
        year, month, day = month_name.groups()
        try:
            month_num = dt.datetime.strptime(month[:3], "%b").month
            return dt.datetime(int(year), month_num, int(day))
        except ValueError:
            return None
    return None


def matches_patterns(value: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, value, re.IGNORECASE) for pattern in patterns)


def score_item(
    title: str,
    summary: str,
    published: dt.datetime | None,
    keywords: list[str],
    boost_keywords: list[str],
    penalty_keywords: list[str],
    source_weight: int,
    now: dt.datetime,
) -> tuple[int, list[str], list[str]]:
    haystack = f"{title} {summary}".lower()
    matches = sorted({kw for kw in keywords if kw.lower() in haystack})
    signals = sorted({kw for kw in boost_keywords if kw.lower() in haystack})
    score = source_weight + len(matches)
    score += 2 * len(signals)
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
    if re.search(r"(\$[0-9]|[0-9]+ ?(m|b|million|billion|%|x)\b)", haystack):
        signals.append("number/money")
        score += 2
    penalties = {kw for kw in penalty_keywords if kw.lower() in haystack}
    score -= 2 * len(penalties)
    return score, matches, sorted(set(signals))


def collect(config: dict, days: int, now: dt.datetime) -> tuple[list[Item], list[str]]:
    keywords = config["keywords"]
    boost_keywords = config.get("boost_keywords", [])
    penalty_keywords = config.get("penalty_keywords", [])
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
                child_text(node, ("pubDate", "published", "updated", "date"))
            )
            summary = strip_html(
                child_text(node, ("description", "summary", "content", "encoded"))
            )
            if not title or not link:
                continue
            if published and published < cutoff:
                continue
            score, matches, signals = score_item(
                title,
                summary,
                published,
                keywords,
                boost_keywords,
                penalty_keywords,
                int(feed.get("weight", 1)),
                now,
            )
            if matches or (signals and feed.get("include_signal_only")):
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
                        signals=signals,
                    )
                )

    for page in config.get("pages", []):
        try:
            html_text = fetch(page["url"]).decode("utf-8", errors="ignore")
        except Exception as exc:  # noqa: BLE001 - show source failures in markdown
            errors.append(f"{page['name']}: {exc}")
            continue

        extractor = LinkExtractor()
        extractor.feed(html_text)
        seen: set[str] = set()
        count = 0
        include_patterns = page.get("include_url_patterns", [])
        exclude_patterns = page.get("exclude_url_patterns", [])
        min_title_chars = int(page.get("min_title_chars", 8))
        max_links = int(page.get("max_links", 30))

        for href, raw_title in extractor.links:
            link = urljoin(page["url"], href).split("#", 1)[0]
            if link in seen:
                continue
            seen.add(link)
            if include_patterns and not matches_patterns(link, include_patterns):
                continue
            if exclude_patterns and matches_patterns(link, exclude_patterns):
                continue
            title = strip_html(raw_title)
            if len(title) < min_title_chars or title.lower() in {
                "read more",
                "learn more",
                "view all",
                "more",
            }:
                title = title_from_url(link)
            if not title:
                continue
            published = published_from_url(link)
            if published and published < cutoff:
                continue
            summary = f"Discovered on {page['name']} index page."
            score, matches, signals = score_item(
                title,
                summary,
                published,
                keywords,
                boost_keywords,
                penalty_keywords,
                int(page.get("weight", 1)),
                now,
            )
            if not (matches or signals):
                continue
            items.append(
                Item(
                    source=page["name"],
                    category=page.get("category", "source-page"),
                    title=title,
                    link=link,
                    published=published,
                    summary=summary,
                    score=score,
                    matches=matches,
                    signals=signals,
                )
            )
            count += 1
            if count >= max_links:
                break

    deduped: dict[str, Item] = {}
    for item in items:
        key = re.sub(r"\W+", "", item.link.lower()) or re.sub(
            r"\W+", "", item.title.lower()
        )
        current = deduped.get(key)
        if current is None or item.score > current.score:
            deduped[key] = item

    return sorted(deduped.values(), key=lambda item: item.score, reverse=True), errors


def select_items(
    items: list[Item], limit: int, per_source_limit: int
) -> list[Item]:
    if per_source_limit <= 0:
        return items[:limit]

    selected: list[Item] = []
    source_counts: Counter[str] = Counter()
    seen: set[str] = set()
    for round_index in range(per_source_limit):
        for item in items:
            key = item.link or f"{item.source}:{item.title}"
            if key in seen or source_counts[item.source] != round_index:
                continue
            selected.append(item)
            seen.add(key)
            source_counts[item.source] += 1
            if len(selected) >= limit:
                return selected
    return selected


def format_date(value: dt.datetime | None) -> str:
    if not value:
        return "undated"
    return value.strftime("%Y-%m-%d")


def format_counter(counter: Counter[str], limit: int = 12) -> str:
    return ", ".join(f"{name} ({count})" for name, count in counter.most_common(limit))


def write_markdown(
    items: list[Item],
    errors: list[str],
    config: dict,
    days: int,
    limit: int,
    out_path: Path,
    now: dt.datetime,
    total_collected: int,
    per_source_limit: int,
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    source_mix = Counter(item.source for item in items)
    category_mix = Counter(item.category for item in items)
    selection_rule = (
        f"round-robin, max {per_source_limit} per source"
        if per_source_limit > 0
        else "no per-source cap"
    )
    lines: list[str] = [
        f"# PBJ News Scan - {now.strftime('%Y-%m-%d')}",
        "",
        f"Window: last {days} days",
        f"Sources: {len(config.get('feeds', []))} feeds, {len(config.get('pages', []))} source pages",
        f"Candidates: {len(items)} shown / {total_collected} collected",
        f"Selection: {selection_rule}",
        "",
        "## Source Mix",
        "",
        f"- Sources: {format_counter(source_mix) if source_mix else 'none'}",
        f"- Categories: {format_counter(category_mix) if category_mix else 'none'}",
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
                f"- Matched: {', '.join(item.matches) if item.matches else 'none'}",
                f"- Signals: {', '.join(item.signals) if item.signals else 'none'}",
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
    parser.add_argument(
        "--per-source-limit",
        type=int,
        default=None,
        help="Limit how many candidates a single source can contribute. Use 0 to disable.",
    )
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    now = dt.datetime.now()
    items, errors = collect(config, args.days, now)
    per_source_limit = (
        args.per_source_limit
        if args.per_source_limit is not None
        else int(config.get("per_source_limit", 4))
    )
    selected_items = select_items(items, args.limit, per_source_limit)
    out_path = args.out or ROOT / "research" / f"{now.strftime('%Y-%m-%d')}-news-scan.md"
    write_markdown(
        selected_items,
        errors,
        config,
        args.days,
        args.limit,
        out_path,
        now,
        len(items),
        per_source_limit,
    )
    print(f"Wrote {out_path}")
    print(f"Candidates: {len(selected_items)} shown / {len(items)} collected")
    if errors:
        print(f"Feed errors: {len(errors)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
