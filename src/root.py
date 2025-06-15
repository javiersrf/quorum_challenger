import click
from src.services.files import parse_file
from src.services.summary import generate_legislators_summary, generate_bill_summary
import csv


@click.command()
@click.option(
    "--legislators",
    prompt="legislators file path",
    help="The path to the legislators file to process.",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
)
@click.option(
    "--bills",
    prompt="bills file path",
    help="The path to the bills file to process.",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
)
@click.option(
    "--votes",
    prompt="votes file path",
    help="The path to the votes file to process.",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
)
@click.option(
    "--vote_results",
    prompt="vote results file path",
    help="The path to the vote results file to process.",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
)
@click.option(
    "--output",
    default="./",
    prompt="output directory",
    help="The directory where the output files will be saved.",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
)
def root(legislators, bills, votes, vote_results, output):
    """Process input legislators file and output bills insight on the overall bills."""
    legislators = parse_file(legislators, expected_schema=["id", "name"])
    bills = parse_file(bills, expected_schema=["id", "title", "sponsor_id"])
    votes = parse_file(votes, expected_schema=["id", "bill_id"])
    vote_results = parse_file(
        vote_results, expected_schema=["id", "legislator_id", "vote_id", "vote_type"]
    )

    legislators_summary_path = generate_legislators_summary(
        legislators=legislators, vote_results=vote_results, output=output
    )
    click.echo(f"Legislators summary generated at: {legislators_summary_path}")
    bills_summary_path = generate_bill_summary(
        vote_results=vote_results, bills=bills, votes=votes, output=output
    )
    click.echo(f"Bills summary generated at: {bills_summary_path}")
