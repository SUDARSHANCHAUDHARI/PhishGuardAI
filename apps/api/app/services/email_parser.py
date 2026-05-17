"""Parse .eml files into simple analysis objects."""

from __future__ import annotations

from email import policy
from email.parser import BytesParser
from pathlib import Path


def parse_email(path: Path) -> dict:
    """Parse an email file."""
    message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
    body_parts: list[str] = []
    if message.is_multipart():
        for part in message.walk():
            if part.get_content_type() in {"text/plain", "text/html"}:
                try:
                    body_parts.append(part.get_content())
                except LookupError:
                    continue
    else:
        body_parts.append(message.get_content())

    return {
        "subject": str(message.get("subject", "")),
        "from": str(message.get("from", "")),
        "reply_to": str(message.get("reply-to", "")),
        "return_path": str(message.get("return-path", "")),
        "authentication_results": str(message.get("authentication-results", "")),
        "received_spf": str(message.get("received-spf", "")),
        "headers": {key.lower(): str(value) for key, value in message.items()},
        "body": "\n".join(body_parts),
    }
