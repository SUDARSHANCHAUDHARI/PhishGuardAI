# PhishGuard AI

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#requirements)
[![Status](https://img.shields.io/badge/status-MVP-green)](#status)
[![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#safe-use)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Phishing email analyzer. Parses `.eml` files, checks headers, link risk, sender spoofing, and language indicators, then explains findings in plain English.

---

## Overview

PhishGuard AI is a defensive analysis tool that ingests a raw email (`.eml`) and produces a phishing risk assessment. It checks SPF/DKIM/DMARC alignment, sender display-name spoofing, suspicious link patterns, urgency/coercion language cues, and risky attachment indicators, then generates a plain-English explanation suitable for security awareness training and analyst handoff.

The current MVP is a Python CLI. A FastAPI + React web dashboard is scaffolded under `apps/` for future development.

## Features

- Parses raw `.eml` files
- Header analysis: SPF, DKIM, DMARC alignment
- Sender display-name spoofing detection
- Link risk scoring (typosquatting, redirects, suspicious TLDs)
- Language analysis for urgency, coercion, and impersonation cues
- Plain-English findings explanation
- Outputs JSON findings, risk summary, Markdown report, and triage handoff

## Requirements

- Python 3.10 or newer
- Linux, macOS, or Windows
- No third-party Python packages (standard library only)
- Optional: Docker for the demo container

## Installation

```bash
git clone https://github.com/SUDARSHANCHAUDHARI/PhishGuardAI.git
cd PhishGuardAI
pip install .
```

This registers the `phish-guard` CLI command.

To run without installing:

```bash
python3 main.py --help
```

## Usage

Analyze the included sample phishing email:

```bash
python3 main.py --email data/samples/phish-sample.eml --out-dir data/reports
```

Generated outputs in `data/reports/`:

- `headers.json` — parsed email headers
- `findings.json` — detected phishing indicators
- `summary.json` — risk score and severity breakdown
- `report.md` — plain-English Markdown analysis
- `triage.md` — analyst triage checklist

## Project Structure

```
PhishGuardAI/
├── apps/
│   ├── api/        FastAPI app scaffold (planned)
│   └── web/        React/Next.js app scaffold (planned)
├── data/
│   ├── samples/    Safe sample .eml files
│   └── reports/    Example generated output
├── docker/         Dockerfile + compose support
├── docs/           Architecture, security notes, demo
├── scripts/        Setup, seed, run helpers
├── tests/          Unit and integration tests
├── main.py         CLI entrypoint
├── pyproject.toml  Package metadata
└── LICENSE
```

## Testing

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Docker Demo

```bash
docker compose run --rm api
```

## Safe Use

This project is defensive and analysis-focused. Use only on emails you own or have explicit written permission to analyze. The included sample emails are synthetic and safe for public demo use.

## Status

Working Python CLI MVP. Web dashboard scaffold present but not yet implemented.

## Roadmap

- Real-time SPF/DKIM/DMARC DNS lookups
- Attachment sandboxing summary
- Multi-language phishing detection
- Mail server integration (IMAP, Microsoft Graph, Gmail API)
- Web dashboard for analyst handoff

## License

Released under the [MIT License](LICENSE). You are free to use, modify, and distribute this software with attribution.

## Author

**Sudarshan Chaudhari** — [SudarshanTechLabs](https://github.com/SUDARSHANCHAUDHARI)
Bangkok, Thailand

For inquiries: open an issue on [GitHub](https://github.com/SUDARSHANCHAUDHARI/PhishGuardAI/issues).
