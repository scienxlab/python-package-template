from click.testing import CliRunner

from mypackage import cli


def test_help():
    """
    Test that the help shows up.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert 'Show this message and exit.' in result.output
