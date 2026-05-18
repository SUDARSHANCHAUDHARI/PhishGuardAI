"""CLI for the PhishGuard AI MVP."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from apps.api.app.services.ai_explainer import explain, risk_score
from apps.api.app.services.email_parser import parse_email
from apps.api.app.services.header_analyzer import analyze_headers
from apps.api.app.services.link_scanner import scan_links
from apps.api.app.services.spoof_detector import detect_spoofing, detect_urgency


def risk_level(score: int) -> str:
    if score >= 80:
        return "high"
    if score >= 45:
        return "medium"
    return "low"


def summarize_findings(findings: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for finding in findings:
        severity = str(finding.get("severity", "low"))
        counts[severity] = counts.get(severity, 0) + 1
    return counts


def recommended_response(score: int) -> str:
    if score >= 80:
        return "Do not click links. Quarantine the message, report it to security, and verify the request through a trusted channel."
    if score >= 45:
        return "Review sender authenticity and links before taking action."
    return "No immediate phishing response is required based on the current checks."


def analyze_email(path: Path) -> tuple[dict, list[dict], dict]:
    """Analyze one email."""
    email_data = parse_email(path)
    findings = [
        *analyze_headers(email_data),
        *detect_spoofing(email_data),
        *detect_urgency(email_data),
        *scan_links(email_data),
    ]
    score = risk_score(findings)
    summary = {
        "subject": email_data["subject"],
        "from": email_data["from"],
        "findings": len(findings),
        "risk_score": score,
        "risk_level": risk_level(score),
        "severity_counts": summarize_findings(findings),
        "recommended_response": recommended_response(score),
        "explanation": explain(email_data, findings),
    }
    return email_data, findings, summary


def _evidence_text(finding: dict) -> str:
    return json.dumps(finding.get("evidence", {}), sort_keys=True)


def build_report(summary: dict, findings: list[dict]) -> str:
    """Return a Markdown report."""
    priority = sorted(findings, key=lambda item: item.get("severity") != "high")
    lines = [
        "# PhishGuard AI Report",
        "",
        "## Summary",
        "",
        f"- Subject: {summary['subject']}",
        f"- From: {summary['from']}",
        f"- Findings: {summary['findings']}",
        f"- Risk score: {summary['risk_score']}/100",
        f"- Risk level: {summary['risk_level']}",
        f"- Recommended response: {summary['recommended_response']}",
        "",
        summary["explanation"],
        "",
        "## Priority Queue",
        "",
    ]
    if not priority:
        lines.append("No phishing findings were produced.")
    for index, finding in enumerate(priority, start=1):
        lines.append(f"{index}. `{finding['kind']}` - {finding['severity']} - {finding['summary']}")
    lines.extend(
        [
            "",
            "## Findings",
            "",
        ]
    )
    for finding in findings:
        lines.extend(
            [
                f"### {finding['summary']}",
                "",
                f"- Severity: `{finding['severity']}`",
                f"- Type: `{finding['kind']}`",
                f"- Evidence: `{_evidence_text(finding)}`",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def build_triage_report(summary: dict, findings: list[dict]) -> str:
    lines = [
        "# PhishGuard AI Triage",
        "",
        f"- Risk level: {summary['risk_level']}",
        f"- Risk score: {summary['risk_score']}/100",
        f"- Recommended response: {summary['recommended_response']}",
        "",
        "## Analyst Checklist",
        "",
        "- Preserve the original message with headers.",
        "- Do not click links from the message.",
        "- Verify the sender through a trusted channel.",
        "- Block or report suspicious URLs if confirmed malicious.",
        "",
        "## High Priority Findings",
        "",
    ]
    high = [finding for finding in findings if finding.get("severity") == "high"]
    if not high:
        lines.append("No high-priority findings were produced.")
    for finding in high:
        lines.extend(
            [
                f"### {finding['summary']}",
                "",
                f"- Type: `{finding['kind']}`",
                f"- Evidence: `{_evidence_text(finding)}`",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="PhishGuard AI email analyzer")
    parser.add_argument("--email", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=Path("data/reports"))
    args = parser.parse_args()

    email_data, findings, summary = analyze_email(args.email)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "email.json").write_text(json.dumps(email_data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.out_dir / "findings.json").write_text(json.dumps(findings, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.out_dir / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.out_dir / "report.md").write_text(build_report(summary, findings), encoding="utf-8")
    (args.out_dir / "triage.md").write_text(build_triage_report(summary, findings), encoding="utf-8")
    print(f"Analyzed {args.email}")
    print(f"Generated {summary['findings']} finding(s)")
    print(f"Risk score: {summary['risk_score']}/100")


if __name__ == "__main__":
    main()
