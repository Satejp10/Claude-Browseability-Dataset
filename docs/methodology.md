# Methodology

This dataset classifies domains by likely reliability for Claude-style web retrieval.

## Classification goal

The goal is not to prove permanent inaccessibility. The goal is to estimate whether asking Claude to fetch a URL is likely to waste usage before requiring the user to paste or upload the content manually.

## Evidence types

| Evidence type | Meaning |
|---|---|
| `robots.txt` | The domain exposes crawler rules that restrict one or more relevant user agents |
| `robots.txt wildcard` | The domain broadly blocks unapproved crawlers using `User-agent: *` or equivalent rules |
| `Claude-specific robots block` | The domain explicitly references Claude/Anthropic agents |
| `policy statement` | The site states automated access is restricted or requires permission |
| `login wall` | The content usually requires a logged-in session |
| `paywall` | The content is subscriber-only or metered |
| `anti-bot / WAF` | Cloudflare, CAPTCHA, bot protection, or similar checks often interfere |
| `dynamic JS` | Content is rendered client-side and may not appear in simple server-side fetches |
| `observed behavior` | Repeated practical failures or partial fetches, usually requiring user-provided content |
| `third-party report` | Public reporting or analysis documents restrictions |

## Risk severity

| Risk | Meaning |
|---|---|
| `High` | Direct fetch is often blocked, partial, login-gated, paywalled, or not worth attempting repeatedly |
| `Medium` | Fetch may work for some pages, but results are unreliable or incomplete |
| `Low` | Generally accessible, but still has caveats |

## Confidence

| Confidence | Meaning |
|---|---|
| `High` | Strong evidence such as explicit robots rules, policy, or consistent access barrier |
| `Medium` | Evidence is mixed, indirect, or site behavior varies by page/region/session |
| `Low` | Included as a watchlist item or based on weak/limited evidence |

## Claude agent distinction

Claude-related access is not one thing. Important agents include:

- `ClaudeBot`: crawling/training/indexing style access
- `Claude-SearchBot`: search-related access
- `Claude-User`: user-directed retrieval when a Claude user asks to open a page

A site blocking `ClaudeBot` does not automatically prove that `Claude-User` is blocked. The dataset therefore includes a separate `Live fetch impacted?` field when possible.

## Recommended action rules

| Situation | Recommended behavior |
|---|---|
| High-risk social / forum URL | Ask user to paste post/thread/comments or upload screenshots |
| Paywalled article | Ask user to paste text they have access to |
| Login-gated app page | Ask for export, screenshot, or copied text |
| Dynamic video page | Ask for transcript, captions, or description |
| Unknown domain | Try once, then stop if blocked/partial |
| Public docs/GitHub/PDF | Fetch normally |

## Maintenance notes

Access changes quickly. Re-check rows periodically, especially major platforms and publishers. Prefer updating evidence summaries rather than deleting uncertain rows.
