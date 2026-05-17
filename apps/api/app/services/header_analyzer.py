"""Analyze email authentication headers."""

from __future__ import annotations


def analyze_headers(email_data: dict) -> list[dict]:
    """Return SPF/DKIM/DMARC findings."""
    auth = f"{email_data.get('authentication_results', '')} {email_data.get('received_spf', '')}".lower()
    findings: list[dict] = []
    checks = {
        "spf": "email.auth.spf_fail",
        "dkim": "email.auth.dkim_fail",
        "dmarc": "email.auth.dmarc_fail",
    }
    for check, kind in checks.items():
        if f"{check}=fail" in auth or f"{check}=softfail" in auth:
            findings.append(
                {
                    "kind": kind,
                    "severity": "high",
                    "summary": f"{check.upper()} authentication failed.",
                    "evidence": {"authentication_results": auth[:240]},
                }
            )
    if not auth.strip():
        findings.append(
            {
                "kind": "email.auth.missing",
                "severity": "medium",
                "summary": "No email authentication results were present.",
                "evidence": {},
            }
        )
    return findings
