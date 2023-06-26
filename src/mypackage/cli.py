"""
Author: Mypackage authors
Licence: MIT
"""
import click

from .mypackage import myfunction


@click.group(context_settings=dict(help_option_names=['--help', '-h']))
def cli():
    pass

@cli.command()
@click.argument('n', type=float)
def mysqrt(n):
    """
    Test square rootiness. Call from the command line with:

        mycli mysqrt 100

    Read the click docs for more on building CLIs:

        https://click.palletsprojects.com/

    Or to get rid of this CLI, delete this file, __main__.py,
    tests/test_cli.py, and remove the [project.scipts] section
    from pyproject.toml.
    """
    return myfunction(n)
