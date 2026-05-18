# PhishGuard AI Triage

- Risk level: high
- Risk score: 100/100
- Recommended response: Do not click links. Quarantine the message, report it to security, and verify the request through a trusted channel.

## Analyst Checklist

- Preserve the original message with headers.
- Do not click links from the message.
- Verify the sender through a trusted channel.
- Block or report suspicious URLs if confirmed malicious.

## High Priority Findings

### SPF authentication failed.

- Type: `email.auth.spf_fail`
- Evidence: `{"authentication_results": "mx.example.com; spf=fail smtp.mailfrom=evil-login.example.net; dkim=fail; dmarc=fail fail (mx.example.com: domain of evil-login.example.net does not designate permitted sender)"}`

### DKIM authentication failed.

- Type: `email.auth.dkim_fail`
- Evidence: `{"authentication_results": "mx.example.com; spf=fail smtp.mailfrom=evil-login.example.net; dkim=fail; dmarc=fail fail (mx.example.com: domain of evil-login.example.net does not designate permitted sender)"}`

### DMARC authentication failed.

- Type: `email.auth.dmarc_fail`
- Evidence: `{"authentication_results": "mx.example.com; spf=fail smtp.mailfrom=evil-login.example.net; dkim=fail; dmarc=fail fail (mx.example.com: domain of evil-login.example.net does not designate permitted sender)"}`

### Reply-To domain does not match From domain.

- Type: `email.sender.reply_to_mismatch`
- Evidence: `{"from_domain": "example.com", "reply_to_domain": "evil-login.example.net"}`

### Email links to a suspicious account-themed host.

- Type: `email.link.suspicious_host`
- Evidence: `{"host": "secure-account-update.evil-login.example.net", "url": "https://secure-account-update.evil-login.example.net/session"}`
