import click

@click.command()
@click.option('--legislators', prompt='legislators file path',
              help='The path to the legislators file to process.')
@click.option('--bills', prompt='legislators file path',
              help='The path to the legislators file to process.')
@click.option('--votes', prompt='legislators file path',
              help='The path to the legislators file to process.')
@click.option('--vote_results', prompt='legislators file path',
              help='The path to the legislators file to process.')
def root(legislators, bills, votes, vote_results):
    """Process input legislators file and output bills insight on the overall bills."""
    click.echo(f"Hello {legislators}!")

