import pytest

def test_app_greet_command(app, simulate_repl, capsys):
    """Test that the REPL correctly handles the 'greet' command."""
    simulate_repl(["greet", "exit"])  # Simulate user input

    with pytest.raises(SystemExit):  # Expect app to exit
        app.start()

    captured = capsys.readouterr()
    assert "Hello" in captured.out  # Check expected output
