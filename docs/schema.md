# Dataset Schema

## Main dataset

File: `data/claude_browseability_dataset.csv`

| Column | Type | Description |
|---|---:|---|
| `ID` | integer | Stable row identifier |
| `Site` | string | Human-readable site name |
| `Domain` | string | Canonical domain |
| `Category` | string | Site category |
| `Market/Region` | string | Geographic or market scope |
| `Claude access status` | string | Overall classification |
| `Live fetch impacted?` | enum | `Yes`, `Partial`, `Unclear`, or `No` |
| `Risk severity` | enum | `High`, `Medium`, or `Low` |
| `Affected Claude/AI agents` | string | Agent/user-agent or access mode affected |
| `Primary barrier` | string | Main reason fetch is likely to fail or degrade |
| `Evidence type` | string | Evidence category |
| `Evidence summary` | string | Short explanation of evidence |
| `Source URL` | URL/string | Supporting source URL where available |
| `Date checked` | date | Date the row was last reviewed |
| `Recommended workaround` | string | Best user action or assistant behavior |
| `Confidence` | enum | `High`, `Medium`, or `Low` |
| `Notes` | string | Additional caveats |

## Minimal dataset

File: `data/domains_minimal.csv`

| Column | Description |
|---|---|
| `Domain` | Domain to check |
| `Risk severity` | Overall risk |
| `Claude access status` | Short status label |
| `Live fetch impacted?` | Whether live user fetch is likely affected |
| `Primary barrier` | Main access issue |
| `Recommended workaround` | Action to take instead |
| `Confidence` | Confidence level |

## JSON dataset

File: `data/claude_browseability_dataset.json`

Uses snake_case keys equivalent to the CSV fields.
