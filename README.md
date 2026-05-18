# PhishGuard AI

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-product%20polish-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

Phishing email analyzer that explains header, sender, language, and link risks in plain English.

- **Portfolio group:** Product-style SaaS project
- **Status:** Product polish implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/PhishGuardAI
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/PhishGuardAI`

## MVP Snapshot

This repository includes a working MVP with safe sample data, deterministic email analysis, local tests, JSON outputs, Markdown report, analyst triage handoff, and Docker demo support.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

## Core Features

- SPF/DKIM/DMARC check
- suspicious links
- sender mismatch
- urgency language detection
- AI explanation
- risk score
- severity breakdown
- recommended response
- analyst triage report

## Suggested Stack

FastAPI, React, email parsing libraries, Docker.

## Status

Working CLI MVP.

## Quick Start

Analyze the included safe phishing sample:

```bash
python3 -m apps.api.app.cli --email data/samples/phishing.eml --out-dir data/reports
```

Run tests:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

Generated outputs:

- `data/reports/email.json`
- `data/reports/findings.json`
- `data/reports/summary.json`
- `data/reports/report.md`
- `data/reports/triage.md`

## Docker Demo

```bash
docker compose run --rm api
```

## Product Polish Capabilities

- Parses `.eml` email files.
- Checks SPF, DKIM, and DMARC authentication results.
- Detects Reply-To and Return-Path sender mismatches.
- Finds suspicious account-themed links.
- Flags urgency language.
- Generates JSON findings, JSON summary, and a Markdown phishing report.
- Adds risk level, severity counts, recommended response, and triage checklist.

## Roadmap

- Add attachment metadata inspection
- Add brand impersonation checks
- Add provider boundary for URL reputation enrichment
- Add user submission workflow in the web UI
- Add SOC queue export
