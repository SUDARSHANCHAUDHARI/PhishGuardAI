"""Detect sender spoofing and urgency language."""

from __future__ import annotations

import re
from email.utils import parseaddr


URGENCY_TERMS = ("urgent", "immediately", "verify now", "account locked", "final warning", "within 24 hours")


def _domain(address: str) -> str:
    parsed = parseaddr(address)[1]
    return parsed.split("@")[-1].lower() if "@" in parsed else ""


def detect_spoofing(email_data: dict) -> list[dict]:
    """Return sender mismatch findings."""
    from_domain = _domain(str(email_data.get("from", "")))
    reply_domain = _domain(str(email_data.get("reply_to", "")))
    return_domain = _domain(str(email_data.get("return_path", "")))
    findings: list[dict] = []
    if reply_domain and from_domain and reply_domain != from_domain:
        findings.append(
            {
                "kind": "email.sender.reply_to_mismatch",
                "severity": "high",
                "summary": "Reply-To domain does not match From domain.",
                "evidence": {"from_domain": from_domain, "reply_to_domain": reply_domain},
            }
        )
    if return_domain and from_domain and return_domain != from_domain:
        findings.append(
            {
                "kind": "email.sender.return_path_mismatch",
                "severity": "medium",
                "summary": "Return-Path domain does not match From domain.",
                "evidence": {"from_domain": from_domain, "return_path_domain": return_domain},
            }
        )
    return findings


def detect_urgency(email_data: dict) -> list[dict]:
    """Return urgency-language findings."""
    text = f"{email_data.get('subject', '')}\n{email_data.get('body', '')}".lower()
    matches = sorted({term for term in URGENCY_TERMS if re.search(re.escape(term), text)})
    if not matches:
        return []
    return [
        {
            "kind": "email.content.urgency",
            "severity": "medium",
            "summary": "Email uses urgency language common in phishing.",
            "evidence": {"matched_terms": matches},
        }
    ]
