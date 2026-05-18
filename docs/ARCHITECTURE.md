# Architecture

PhishGuard AI is a defensive email-analysis MVP for explaining phishing risk in plain English.

## Flow

1. `email_parser.py` parses a local `.eml` file.
2. `header_analyzer.py` checks SPF, DKIM, DMARC, and missing authentication results.
3. `spoof_detector.py` checks sender mismatch and urgency language.
4. `link_scanner.py` extracts suspicious links.
5. `ai_explainer.py` generates deterministic plain-English explanations.
6. `cli.py` writes JSON, Markdown report, and triage outputs.

## Outputs

- parsed email JSON
- finding list JSON
- summary JSON
- phishing report Markdown
- analyst triage Markdown

The current MVP is offline and does not send email content to external services.
