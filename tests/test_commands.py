import pytest
from app import App
from app.plugins.greet import GreetCommand


def test_app_greet_command(app, simulate_repl, capsys):
    """Test that the REPL correctly handles the 'greet' command."""
    simulate_repl(["greet", "exit"])

    with pytest.raises(SystemExit):
        app.start()

    captured = capsys.readouterr()
    assert "Hello" in captured.out

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    assert e.value.code == 0, "The app did not exit as expected"
