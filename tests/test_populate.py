from click.testing import CliRunner
from abn_assignment.cli import populate


def test_populate_bad():
    runner = CliRunner()
    result = runner.invoke(populate)

    assert result.exit_code == 0
