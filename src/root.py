import click
from src.services.files import parse_file
from src.services.summary import generate_legislators_summary, generate_bill_summary
import csv


@click.command()
@click.option(
    "--legislators",
    prompt="legislators file path",
    help="The path to the legislators file to process.",
)
@click.option(
    "--bills",
    prompt="bills file path",
    help="The path to the bills file to process.",
)
@click.option(
    "--votes",
    prompt="votes file path",
    help="The path to the votes file to process.",
)
@click.option(
    "--vote_results",
    prompt="vote results file path",
    help="The path to the vote results file to process.",
)
def root(legislators, bills, votes, vote_results):
    """Process input legislators file and output bills insight on the overall bills."""
    legislators = parse_file(legislators, expected_schema=["id", "name"])
    bills = parse_file(bills, expected_schema=["id", "title", "sponsor_id"])
    votes = parse_file(votes, expected_schema=["id", "bill_id"])
    vote_results = parse_file(
        vote_results, expected_schema=["id", "legislator_id", "vote_id", "vote_type"]
    )
