def test_logs(app, capsys):
    """Test that logs command works"""
    app.do_logs("")
    captured = capsys.readouterr()
    assert "Application Log History" in captured.out or "Log file is empty" in captured.out

def test_clear_logs(app, capsys, setup_log_file):
    """Test that clearing logs works"""
    log_file = setup_log_file  # ✅ Use fixture

    app.do_clear_logs("")
    captured = capsys.readouterr()
    assert "Application log history cleared." in captured.out

    with open(log_file, "r", encoding="utf-8") as f:
        assert f.read().strip() == ""  # ✅ Ensuring log is empty after clearing
