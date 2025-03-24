from typer.testing import CliRunner

from decard_preacher.main import app

runner = CliRunner()

def test_first_test():
    result = runner.invoke(app, ["√3", "1", "1"])
    assert result.exit_code == 0
    assert "r = 2, θ = 63°, ϕ = 30°" in result.stdout

def test_second_test():
    result = runner.invoke(app, ["√2", "√2", "0"])
    assert result.exit_code == 0
    assert "r = 1, θ = 90°, ϕ = 30°"
