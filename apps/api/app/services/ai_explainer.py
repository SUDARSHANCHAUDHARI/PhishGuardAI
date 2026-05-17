"""Deterministic phishing explanation and risk scoring."""

from __future__ import annotations

from collections import Counter


POINTS = {"critical": 90, "high": 30, "medium": 15, "low": 5}


def risk_score(findings: list[dict]) -> int:
    """Return 0-100 phishing risk score."""
    return min(100, sum(POINTS.get(str(finding.get("severity")), 0) for finding in findings))


def explain(email_data: dict, findings: list[dict]) -> str:
    """Return a plain-English phishing explanation."""
    if not findings:
        return "This email did not trigger the MVP phishing checks."
    score = risk_score(findings)
    kinds = Counter(str(finding["kind"]) for finding in findings)
    themes = ", ".join(f"{kind} ({count})" for kind, count in kinds.items())
    return (
        f"PhishGuard scored this email {score}/100. "
        f"Main signals: {themes}. "
        "Review sender authenticity, avoid clicking links, and verify the request through a trusted channel."
    )
