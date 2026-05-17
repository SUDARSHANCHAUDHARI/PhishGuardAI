# PhishGuard AI Report

## Summary

- Subject: Urgent: Verify now or account locked within 24 hours
- From: Example Support <support@example.com>
- Findings: 7
- Risk score: 100/100

PhishGuard scored this email 100/100. Main signals: email.auth.spf_fail (1), email.auth.dkim_fail (1), email.auth.dmarc_fail (1), email.sender.reply_to_mismatch (1), email.sender.return_path_mismatch (1), email.content.urgency (1), email.link.suspicious_host (1). Review sender authenticity, avoid clicking links, and verify the request through a trusted channel.

## Findings

### SPF authentication failed.

- Severity: `high`
- Type: `email.auth.spf_fail`
- Evidence: `{'authentication_results': 'mx.example.com; spf=fail smtp.mailfrom=evil-login.example.net; dkim=fail; dmarc=fail fail (mx.example.com: domain of evil-login.example.net does not designate permitted sender)'}`

### DKIM authentication failed.

- Severity: `high`
- Type: `email.auth.dkim_fail`
- Evidence: `{'authentication_results': 'mx.example.com; spf=fail smtp.mailfrom=evil-login.example.net; dkim=fail; dmarc=fail fail (mx.example.com: domain of evil-login.example.net does not designate permitted sender)'}`

### DMARC authentication failed.

- Severity: `high`
- Type: `email.auth.dmarc_fail`
- Evidence: `{'authentication_results': 'mx.example.com; spf=fail smtp.mailfrom=evil-login.example.net; dkim=fail; dmarc=fail fail (mx.example.com: domain of evil-login.example.net does not designate permitted sender)'}`

### Reply-To domain does not match From domain.

- Severity: `high`
- Type: `email.sender.reply_to_mismatch`
- Evidence: `{'from_domain': 'example.com', 'reply_to_domain': 'evil-login.example.net'}`

### Return-Path domain does not match From domain.

- Severity: `medium`
- Type: `email.sender.return_path_mismatch`
- Evidence: `{'from_domain': 'example.com', 'return_path_domain': 'evil-login.example.net'}`

### Email uses urgency language common in phishing.

- Severity: `medium`
- Type: `email.content.urgency`
- Evidence: `{'matched_terms': ['account locked', 'immediately', 'urgent', 'verify now', 'within 24 hours']}`

### Email links to a suspicious account-themed host.

- Severity: `high`
- Type: `email.link.suspicious_host`
- Evidence: `{'url': 'https://secure-account-update.evil-login.example.net/session', 'host': 'secure-account-update.evil-login.example.net'}`

