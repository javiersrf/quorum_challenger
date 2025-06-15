run-dev:
	uv run main.py --legislators "/home/javiersrf/side_projects/quorum-challenger/example_data/legislators.csv" --bills "/home/javiersrf/side_projects/quorum-challenger/example_data/bills.csv" --votes "/home/javiersrf/side_projects/quorum-challenger/example_data/votes.csv" --vote_results "/home/javiersrf/side_projects/quorum-challenger/example_data/vote_results.csv"


test:
	uv run pytest .


format:
	uv run ruff format .