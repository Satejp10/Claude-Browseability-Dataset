# Contributing

Contributions are welcome if they improve evidence quality, update stale rows, or add useful domains.

## Good contributions

- Add a domain with clear evidence
- Update a stale robots.txt or policy reference
- Split vague rows into more precise classifications
- Add a better workaround
- Improve confidence labels
- Add comparison data for other assistants

## Evidence requirements

Prefer at least one of:

- robots.txt URL
- official policy page
- public documentation
- clear login/paywall behavior
- repeatable observed failure
- credible third-party analysis

## Row quality checklist

Before submitting a row, check:

- Domain is canonical and deduplicated
- Risk is not overstated
- `ClaudeBot` and `Claude-User` are not conflated
- Evidence summary is short and factual
- Recommended workaround is actionable
- Confidence matches the strength of evidence

## Suggested pull request format

```md
## Change type
- [ ] Add domain
- [ ] Update evidence
- [ ] Fix classification
- [ ] Improve docs

## Summary
Briefly explain the change.

## Evidence
Add source URLs or observed behavior.

## Notes
Mention caveats or uncertainty.
```
