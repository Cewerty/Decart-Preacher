from typer.testing import CliRunner

from decard_preacher.main import app

runner = CliRunner()

def test_first_test():
    result = runner.invoke(app, ["1/2", "1/2", "√2/2"])
    assert result.exit_code == 0
    assert "r = 1, θ = 45°, ϕ = 45°" in result.stdout

def test_second_test():
    result = runner.invoke(app, ["√2/2", "1/2", "0"])
    assert result.exit_code == 0
    assert "r = 1, θ = 90°, ϕ = 35°" in result.stdout
