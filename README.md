# Legislator overview

## Assignment
Get input data source from a legislator and output results for insight

1. For every legislator in the dataset, how many bills did the legislator support (voted for the bill)? How many bills did the legislator oppose?
2. For every bill in the dataset, how many legislators supported the bill? How many legislators opposed the bill? Who was the primary sponsor of the bill?

## How to use
### Build:
```bash
# Install dependencies
uv pip install -r requirements.txt

# Run the CLI
uv run main.py --help
```
### Example

```bash
uv run main.py \
    --legislators "/path/to/data/legislators.csv" \
    --bills "/path/to/data/bills.csv" \
    --votes "/path/to/data/votes.csv" \
    --vote_results "/path/to/data/vote_results.csv"
```
