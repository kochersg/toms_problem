import click
import toms_problem.monte_carlo as monte_carlo
@click.group()
def cli() -> None:
    pass


@click.command()
@click.option(
    "-n",
    "--number-of-articles",
    type=click.INT,
    default=20,
)
@click.option(
    "-p",
    "--number-of-places",
    type=click.INT,
    default=5,
)
@click.option(
    "-s",
    "--number-of-searched-articles",
    type=click.INT,
    default=5,
)
@click.option(
    "-r",
    "--number-of-mc-runs",
    type=click.INT,
    default=10000,
)
def calc_mc(number_of_articles: int, number_of_places: int, number_of_searched_articles: int, number_of_mc_runs: int):
    click.echo(f"Number of articles {number_of_articles}")
    click.echo(f"Number of places {number_of_places}")
    click.echo(f"Number of searched articles {number_of_searched_articles}")
    click.echo(f"Number of Monte Carlo runs {number_of_mc_runs}")
    monte_carlo.calc_MC(
        n_articles=number_of_articles, 
        n_places=number_of_places, 
        n_searched_articles=number_of_searched_articles, 
        n_MC_runs=number_of_mc_runs
    )

cli.add_command(calc_mc)
