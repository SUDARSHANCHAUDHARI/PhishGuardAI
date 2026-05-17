# PhishGuard AI

**Goal:** Phishing email detector and plain-English explainer.

**MVP:** Upload .eml, analyze headers and body.

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

## Repository Status

This repository contains the production-ready foundation for the PhishGuard AI MVP. The current codebase is scaffolded and ready for focused implementation work.

## Production Foundation

- Private GitHub repository linked to `main`
- Initial MVP scaffold committed
- CI repository-health workflow
- Security policy
- Contribution guide
- Pull request and issue templates
- Production readiness checklist
- Safe ignore rules for local secrets and generated files
