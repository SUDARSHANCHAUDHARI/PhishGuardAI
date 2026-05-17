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


def analyze_email(path: Path) -> tuple[dict, list[dict], dict]:
    """Analyze one email."""
    email_data = parse_email(path)
    findings = [
        *analyze_headers(email_data),
        *detect_spoofing(email_data),
        *detect_urgency(email_data),
        *scan_links(email_data),
    ]
    summary = {
        "subject": email_data["subject"],
        "from": email_data["from"],
        "findings": len(findings),
        "risk_score": risk_score(findings),
        "explanation": explain(email_data, findings),
    }
    return email_data, findings, summary


def build_report(summary: dict, findings: list[dict]) -> str:
    """Return a Markdown report."""
    lines = [
        "# PhishGuard AI Report",
        "",
        "## Summary",
        "",
        f"- Subject: {summary['subject']}",
        f"- From: {summary['from']}",
        f"- Findings: {summary['findings']}",
        f"- Risk score: {summary['risk_score']}/100",
        "",
        summary["explanation"],
        "",
        "## Findings",
        "",
    ]
    for finding in findings:
        lines.extend(
            [
                f"### {finding['summary']}",
                "",
                f"- Severity: `{finding['severity']}`",
                f"- Type: `{finding['kind']}`",
                f"- Evidence: `{finding.get('evidence', {})}`",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


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
    print(f"Analyzed {args.email}")
    print(f"Generated {summary['findings']} finding(s)")
    print(f"Risk score: {summary['risk_score']}/100")


if __name__ == "__main__":
    main()
