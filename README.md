# PhishGuard AI

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-MVP-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

Phishing email analyzer that explains header, sender, language, and link risks in plain English.

- **Portfolio group:** Product-style SaaS project
- **Status:** MVP implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/PhishGuardAI
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/PhishGuardAI`

## MVP Snapshot

This repository includes a working MVP with safe sample data, deterministic detection or analysis logic, local tests, and generated output reports where relevant. It is ready for README/demo polish or deeper product work.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

## Core Features

- SPF/DKIM/DMARC check
- suspicious links
- sender mismatch
- urgency language detection
- AI explanation
- risk score

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

## MVP Capabilities

- Parses `.eml` email files.
- Checks SPF, DKIM, and DMARC authentication results.
- Detects Reply-To and Return-Path sender mismatches.
- Finds suspicious account-themed links.
- Flags urgency language.
- Generates JSON findings, JSON summary, and a Markdown phishing report.

## Roadmap

- Polish sample output screenshots or terminal demos
- Add architecture diagram and deeper implementation notes
- Expand test coverage around edge cases
- Add Docker or local demo workflow where useful
- Prepare `v0.1.0-mvp` release notes
