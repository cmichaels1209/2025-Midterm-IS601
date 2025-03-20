import os
import pytest
from app import App

@pytest.fixture
def app():
    """Fixture to initialize and return an instance of App"""
    return App()

@pytest.fixture
def simulate_repl(monkeypatch):
    """Fixture to simulate user input in the REPL"""
    def _simulate_repl_input(inputs):
        inputs = iter(inputs)
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    return _simulate_repl_input

@pytest.fixture
def setup_log_file():
    """Fixture to create a test log file and clean it up after"""
    log_file = "logs/app.log"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write("Test log entry\n")

    yield log_file  # Let test use it

    with open(log_file, "w", encoding="utf-8") as f:
        f.truncate(0)  # Clear log after test
