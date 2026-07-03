#!/usr/bin/env python3
"""Generate the blockAds variant with Kelee's Bilibili rules merged in."""

from __future__ import annotations

import argparse
import re
import urllib.request
from collections import OrderedDict
from pathlib import Path


FMZ_BLOCKADS_URL = "https://raw.githubusercontent.com/fmz200/wool_scripts/refs/heads/main/Surge/module/blockAds.module"
KELEE_BILIBILI_URL = "https://raw.githubusercontent.com/zwjtano/kelee-loon-surge-modules/master/modules/Bilibili_remove_ads.sgmodule"
OUTPUT_URL = "https://raw.githubusercontent.com/zwjtano/blockAds-module/master/surge-modules/blockAds-bilibili-search-preserved.module"

BILIBILI_ARGUMENTS = [
    'displayUpList:"show"',
    "purifyComment:true",
    "optimizeRequest:true",
    "sponsorBlock:false",
    'logLevel:"off"',
]
BILIBILI_HOSTS = [
    "grpc.biliapi.net",
    "app.bilibili.com",
    "api.bilibili.com",
    "api.live.bilibili.com",
    "line3-h5-mobile-api.biligame.com",
]
SECTION_ORDER = [
    "Rule",
    "Header Rewrite",
    "URL Rewrite",
    "Body Rewrite",
    "Map Local",
    "Script",
    "MITM",
]


def fetch_text(url: str, timeout: int = 60) -> str:
    with urllib.request.urlopen(url, timeout=timeout) as response:
        return response.read().decode("utf-8-sig")


def split_module(text: str) -> tuple[list[str], OrderedDict[str, list[str]]]:
    header: list[str] = []
    sections: OrderedDict[str, list[str]] = OrderedDict()
    current_section: str | None = None

    for line in text.splitlines():
        section_match = re.match(r"^\[([^\]]+)\]$", line.strip())
        if section_match:
            current_section = section_match.group(1).strip()
            sections.setdefault(current_section, [])
            continue
        if current_section is None:
            header.append(line)
        else:
            sections[current_section].append(line)
    return header, sections


def patch_header(lines: list[str]) -> list[str]:
    output: list[str] = []
    saw_arguments = False
    for line in lines:
        if line.startswith("#!name="):
            output.append("#!name=广告拦截&净化合集 - 合并 Kelee 哔哩去广告")
            continue
        if line.startswith("#!desc="):
            output.append(
                "#!desc=自动同步 fmz200/wool_scripts 的 blockAds.module，合并 Kelee 最新哔哩去广告规则，放行哔哩哔哩热搜、搜索发现和默认搜索词，并移除 YouTube 规则。"
            )
            continue
        if line.startswith("#!raw-url="):
            output.append(f"#!raw-url={OUTPUT_URL}")
            continue
        if line.startswith("#!category="):
            output.append("#!category=zwjtano")
            continue
        if line.startswith("#!arguments="):
            saw_arguments = True
            output.append(merge_arguments(line))
            continue
        output.append(line)

    if not saw_arguments:
        output.append("#!arguments=" + ",".join(BILIBILI_ARGUMENTS))
    return output


def merge_arguments(line: str) -> str:
    current = line.split("=", 1)[1].strip()
    parts = [part.strip() for part in current.split(",") if part.strip()]
    existing_keys = {part.split(":", 1)[0].split("=", 1)[0].strip() for part in parts}
    for argument in BILIBILI_ARGUMENTS:
        key = argument.split(":", 1)[0].split("=", 1)[0]
        if key not in existing_keys:
            parts.append(argument)
    return "#!arguments=" + ",".join(parts)


def strip_youtube(lines: list[str]) -> list[str]:
    output: list[str] = []
    for line in lines:
        if "youtubei.googleapis.com" in line or "*.googlevideo.com" in line:
            line = line.replace(", youtubei.googleapis.com", "").replace(", *.googlevideo.com", "")
        if any(
            marker in line
            for marker in (
                "# > YouTube",
                "rr*.googlevideo.com",
                "googlevideo",
                "youtubei\\.googleapis\\.com",
                "youtube.response.js",
                "YouTube响应体",
            )
        ):
            continue
        output.append(line)
    return output


def remove_comment_block(lines: list[str], title: str) -> list[str]:
    output: list[str] = []
    skipping = False
    for line in lines:
        stripped = line.strip()
        if stripped == title:
            skipping = True
            continue
        if skipping and stripped.startswith("# > "):
            skipping = False
        if not skipping:
            output.append(line)
    return trim_blank_edges(output)


def trim_blank_edges(lines: list[str]) -> list[str]:
    while lines and lines[0] == "":
        lines.pop(0)
    while lines and lines[-1] == "":
        lines.pop()
    return lines


def preserve_bilibili_search(lines: list[str]) -> list[str]:
    output: list[str] = []
    for line in lines:
        if "interface\\.v1\\.(Teenagers\\/ModeStatus|Search\\/DefaultWords)" in line:
            line = line.replace(
                "interface\\.v1\\.(Teenagers\\/ModeStatus|Search\\/DefaultWords)",
                "interface\\.v1\\.Teenagers\\/ModeStatus",
            )
        elif "bilibili\\.app\\.interface\\.v1\\.Search\\/DefaultWords" in line:
            continue
        line = line.replace("|v2\\/search\\/square", "").replace("v2\\/search\\/square|", "")
        line = line.replace("|polymer\\.app\\.search\\.v1\\.Search\\/SearchAll", "")
        line = line.replace("polymer\\.app\\.search\\.v1\\.Search\\/SearchAll|", "")
        output.append(line)
    return output


def extract_kelee_sections(text: str) -> OrderedDict[str, list[str]]:
    _, sections = split_module(text)
    output: OrderedDict[str, list[str]] = OrderedDict()
    for section, lines in sections.items():
        if section == "MITM":
            continue
        cleaned = preserve_bilibili_search(trim_blank_edges(lines.copy()))
        if cleaned:
            output[section] = cleaned
    return output


def insert_bilibili_sections(
    sections: OrderedDict[str, list[str]],
    kelee_sections: OrderedDict[str, list[str]],
) -> OrderedDict[str, list[str]]:
    cleaned: OrderedDict[str, list[str]] = OrderedDict()
    for section, lines in sections.items():
        filtered = strip_youtube(remove_comment_block(lines, "# > 哔哩哔哩"))
        cleaned[section] = filtered

    for section in kelee_sections:
        cleaned.setdefault(section, [])

    ordered: OrderedDict[str, list[str]] = OrderedDict()
    for section in SECTION_ORDER:
        if section in cleaned:
            ordered[section] = merge_section(section, cleaned[section], kelee_sections.get(section, []))
    for section, lines in cleaned.items():
        if section not in ordered:
            ordered[section] = lines
    return ordered


def merge_section(section: str, existing: list[str], bilibili: list[str]) -> list[str]:
    existing = trim_blank_edges(existing.copy())
    if section == "MITM":
        return merge_mitm(existing)
    if not bilibili:
        return existing
    return ["# > 哔哩哔哩（合并自 Kelee）", *bilibili, "", *existing]


def merge_mitm(lines: list[str]) -> list[str]:
    output: list[str] = []
    merged = False
    for line in lines:
        if line.startswith("hostname ="):
            prefix, raw_hosts = line.split("=", 1)
            hosts = [host.strip() for host in raw_hosts.replace("%APPEND%", "").split(",") if host.strip()]
            for host in BILIBILI_HOSTS:
                if host not in hosts:
                    hosts.append(host)
            output.append(f"{prefix.strip()} = %APPEND% " + ", ".join(hosts))
            merged = True
        else:
            output.append(line)
    if not merged:
        output.append("hostname = %APPEND% " + ", ".join(BILIBILI_HOSTS))
    return output


def render_module(header: list[str], sections: OrderedDict[str, list[str]]) -> str:
    output = header.copy()
    while output and output[-1] == "":
        output.pop()
    output.extend(["", ""])
    for section, lines in sections.items():
        output.append(f"[{section}]")
        output.extend(lines)
        output.append("")
    return "\n".join(output).rstrip() + "\n"


def generate(output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    blockads = fetch_text(FMZ_BLOCKADS_URL)
    kelee = fetch_text(KELEE_BILIBILI_URL)
    header, sections = split_module(blockads)
    patched_header = patch_header(strip_youtube(header))
    kelee_sections = extract_kelee_sections(kelee)
    patched_sections = insert_bilibili_sections(sections, kelee_sections)
    text = render_module(patched_header, patched_sections)
    output_path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("surge-modules/blockAds-bilibili-search-preserved.module"),
        help="Path to write the generated Surge module.",
    )
    args = parser.parse_args()
    generate(args.output)


if __name__ == "__main__":
    main()
