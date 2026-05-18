# Security Notes

PhishGuard AI is defensive and analysis-only.

## Safe Use

- Analyze only emails you own or have permission to review.
- Do not commit real user mailboxes, credentials, tokens, or private attachments.
- Treat generated reports as sensitive because they may include sender, recipient, link, and header details.

## Current Boundary

The MVP runs locally and does not call external URL reputation, AI, or mailbox APIs. The sample `.eml` is synthetic and safe for demos.

## Before Production

- Add authentication and authorization.
- Add upload size limits and attachment handling controls.
- Add redaction for private recipients and message IDs.
- Add retention controls for submitted emails and reports.
