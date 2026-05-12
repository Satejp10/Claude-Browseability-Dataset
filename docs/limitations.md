# Limitations

## This is not a permanent blocklist

Site access changes. A row marked high-risk today may become accessible later, and accessible pages can become blocked after site policy changes.

## Robots.txt is not the whole story

A domain can be difficult for Claude even without a clear robots.txt block because of:

- login walls
- paywalls
- Cloudflare or other WAF rules
- CAPTCHA checks
- JavaScript rendering
- regional differences
- rate limits
- user-agent filtering
- cookie/session requirements

## ClaudeBot is not Claude-User

Blocking `ClaudeBot` usually indicates crawling/indexing restrictions. It does not always prove that live user-requested retrieval via Claude is blocked. Where possible, this dataset separates crawler restrictions from live-fetch impact.

## No bypass guidance

This project is intended for triage and user experience improvement. It should not be used to bypass access controls, paywalls, or site policies.

## Use user-provided content when appropriate

For restricted or degraded sites, the cleanest workflow is often:

1. user provides text, screenshot, PDF, transcript, or export
2. assistant analyzes provided content
3. assistant avoids repeated failed fetch attempts
