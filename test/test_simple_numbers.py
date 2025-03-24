
from typer.testing import CliRunner

from src.main import app

runner = CliRunner()

def test_first_test():
    result = runner.invoke(app, ["1", "1", "√2"])
    assert result.exit_code == 0
    assert "r = 2, θ = 45°, ϕ = 45°" in result.stdout

def test_second_test():
    result = runner.invoke(app, ["0", "0", "5"])
    assert result.exit_code == 0

