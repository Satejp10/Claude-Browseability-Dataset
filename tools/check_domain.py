#!/usr/bin/env python3
"""Simple local lookup tool for the LLM Browseability Index.

Usage:
  python tools/check_domain.py reddit.com
  python tools/check_domain.py https://www.reddit.com/r/example/comments/abc123
"""

from __future__ import annotations

import csv
import pathlib
import sys
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "domains_minimal.csv"


def normalize_domain(value: str) -> str:
    value = value.strip().lower()
    if not value:
        return ""
    if "://" not in value:
        value = "https://" + value
    parsed = urlparse(value)
    host = parsed.netloc or parsed.path
    host = host.split("@").pop().split(":")[0]
    if host.startswith("www."):
        host = host[4:]
    return host


def load_rows() -> list[dict[str, str]]:
    with DATA_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def find_domain(query: str, rows: list[dict[str, str]]) -> dict[str, str] | None:
    domain = normalize_domain(query)
    for row in rows:
        candidate = normalize_domain(row.get("Domain", ""))
        if domain == candidate or domain.endswith("." + candidate):
            return row
    return None


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/check_domain.py <domain-or-url>")
        return 2

    rows = load_rows()
    row = find_domain(sys.argv[1], rows)
    if not row:
        print("No match found. Treat as unknown: try once, then ask for pasted/uploaded content if retrieval fails.")
        return 1

    print(f"Domain: {row.get('Domain')}")
    print(f"Risk severity: {row.get('Risk severity')}")
    print(f"Status: {row.get('Claude access status')}")
    print(f"Live fetch impacted: {row.get('Live fetch impacted?')}")
    print(f"Primary barrier: {row.get('Primary barrier')}")
    print(f"Recommended workaround: {row.get('Recommended workaround')}")
    print(f"Confidence: {row.get('Confidence')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
