from typer.testing import CliRunner

from decard_preacher.main import app

runner = CliRunner()

def test_first_test():
    result = runner.invoke(app, ["0.5", "0.5", "√2/2"])
    assert result.exit_code == 0
    assert "r = 1, θ = 45°, ϕ = 45°" in result.stdout

def test_second_test():
    result = runner.invoke(app, ["1.732", "1", "2"])
    assert result.exit_code == 0
    assert "r = 3, θ = 45°, ϕ = 30°" in result.stdout
