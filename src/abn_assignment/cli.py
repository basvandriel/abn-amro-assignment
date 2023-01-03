import click


@click.command()
def populate():
    """
    Program that populates a SQL database with GDP and StackOverflow from 2021.
    """
    click.echo("Hello!")
