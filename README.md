Work in progress and not reviewed yet, use with caution. 

# LLM Browseability Index

A practical dataset of domains that are commonly **blocked, degraded, paywalled, login-gated, JavaScript-heavy, Cloudflare-protected, or otherwise unreliable** for Claude-style web retrieval.

The goal is not to claim that a site is permanently inaccessible. The goal is to help users and AI assistants avoid wasting usage on predictable fetch failures.

> **Tagline:** Stop wasting LLM browsing tokens on URLs that were never going to work.

## Why this exists

Claude and other AI assistants often attempt to fetch URLs that are predictably difficult to access, then spend tokens discovering that the site is blocked, degraded, or only partially visible.

This dataset provides a pre-fetch triage layer:

1. Check the domain before browsing.
2. Classify the likely access risk.
3. Recommend the best workaround.
4. Avoid repeated failed fetch attempts.

## What is included

```text
llm-browseability-index/
├── README.md
├── data/
│   ├── claude_browseability_dataset.csv
│   ├── claude_browseability_dataset.xlsx
│   ├── claude_browseability_dataset.json
│   ├── domains_minimal.csv
│   └── summary.json
├── prompts/
│   ├── claude_prefetch_triage_prompt.md
│   └── compact_claude_instruction.md
├── docs/
│   ├── methodology.md
│   ├── schema.md
│   ├── status_legend.md
│   └── limitations.md
├── examples/
│   └── sample_outputs.md
├── tools/
│   └── check_domain.py
├── .gitignore
├── CONTRIBUTING.md
└── LICENSE
```

## Dataset formats

| File | Use case |
|---|---|
| `data/claude_browseability_dataset.xlsx` | Best for manual review, filtering, and notes |
| `data/claude_browseability_dataset.csv` | Best for GitHub, spreadsheets, scripts, and import |
| `data/claude_browseability_dataset.json` | Best for apps, extensions, APIs, and automation |
| `data/domains_minimal.csv` | Compact denylist-style lookup table |
| `data/summary.json` | Basic dataset counts |

## Core fields

| Field | Meaning |
|---|---|
| `Domain` | Domain being evaluated |
| `Category` | Social, news, retail, docs, forum, etc. |
| `Claude access status` | Human-readable access classification |
| `Live fetch impacted?` | Whether user-directed fetching is likely affected |
| `Risk severity` | High / Medium / Low |
| `Primary barrier` | Main reason access is degraded |
| `Evidence type` | robots.txt, login wall, paywall, observed behavior, policy, etc. |
| `Source URL` | Supporting URL where available |
| `Recommended workaround` | What the user or assistant should do instead |
| `Confidence` | High / Medium / Low confidence in classification |

## Example use

When a user gives Claude a Reddit, X, LinkedIn, paywalled news, or Cloudflare-heavy URL, Claude should not repeatedly attempt direct fetching. It should tell the user that access is likely degraded and ask for pasted text, screenshots, PDFs, exports, or transcripts instead.

## Claude project instruction

Copy this into a Claude Project, Custom Instruction, or reusable prompt:

```text
Before attempting to fetch a URL, check whether the domain is commonly inaccessible, login-gated, paywalled, Cloudflare-protected, JavaScript-heavy, or blocked for Claude-related user agents.

If the URL is from a high-risk domain, do not repeatedly attempt direct fetching. Tell the user the site is likely inaccessible or degraded, then ask them to paste the text, upload a screenshot/PDF/export, or provide a transcript.

For GitHub, official docs, public PDFs, arXiv, Wikipedia, government pages, and static documentation sites, direct fetching is usually acceptable.
```

More complete versions are in [`prompts/`](prompts/).

## Important caveat

This dataset is **probabilistic, not absolute**.

Site access can change over time. A domain may block `ClaudeBot` for crawling while still allowing `Claude-User` for user-directed retrieval, or it may allow indexing while blocking live fetches. Some failures are caused by login walls, paywalls, JavaScript rendering, bot protection, or region-specific behavior rather than a visible robots.txt block.

## Roadmap

- [ ] Add automated robots.txt checks
- [ ] Add per-agent fields for `ClaudeBot`, `Claude-SearchBot`, and `Claude-User`
- [ ] Add ChatGPT / Gemini / Perplexity comparison columns
- [ ] Build a small URL checker web app
- [ ] Build a browser extension warning before sharing URLs with Claude
- [ ] Add community submissions and validation workflow

## License

MIT. See [`LICENSE`](LICENSE).

## Disclaimer

This is an independent community dataset. It is not affiliated with Anthropic, Claude, OpenAI, Google, Reddit, X, LinkedIn, or any listed site.
