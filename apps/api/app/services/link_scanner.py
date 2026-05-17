"""Scan email bodies for suspicious links."""

from __future__ import annotations

import re
from urllib.parse import urlparse


URL_RE = re.compile(r"https?://[^\s<>\"]+")
SHORTENERS = {"bit.ly", "tinyurl.com", "t.co", "goo.gl"}
SUSPICIOUS_HOST_TERMS = ("login", "verify", "secure", "account", "update")


def scan_links(email_data: dict) -> list[dict]:
    """Return link findings."""
    body = str(email_data.get("body", ""))
    findings: list[dict] = []
    seen: set[str] = set()
    for url in URL_RE.findall(body):
        cleaned = url.rstrip(").,")
        if cleaned in seen:
            continue
        seen.add(cleaned)
        host = urlparse(cleaned).netloc.lower()
        if host in SHORTENERS:
            findings.append(
                {
                    "kind": "email.link.shortener",
                    "severity": "medium",
                    "summary": "Email contains a shortened URL.",
                    "evidence": {"url": cleaned},
                }
            )
        if any(term in host for term in SUSPICIOUS_HOST_TERMS) and not host.endswith("example.com"):
            findings.append(
                {
                    "kind": "email.link.suspicious_host",
                    "severity": "high",
                    "summary": "Email links to a suspicious account-themed host.",
                    "evidence": {"url": cleaned, "host": host},
                }
            )
    return findings
