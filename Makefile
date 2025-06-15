run-dev:
	 uv run main.py --legislators "/home/javiersrf/side_projects/quorum-challenger/data/legislators.csv" --bills "/home/javiersrf/side_projects/quorum-challenger/data/bills.csv" --votes "/home/javiersrf/side_projects/quorum-challenger/data/votes.csv" --vote_results "/home/javiersrf/side_projects/quorum-challenger/data/vote_results.csv"


test:
	uv run pytest .


format:
	uv run ruff format .