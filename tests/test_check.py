from xlade.cli.check import run


def test_check_warns_no_init(tmp_project, capsys):
    run()
    captured = capsys.readouterr()
    assert "not initialized" in captured.out


def test_check_warns_no_experiments(initialized_project, capsys):
    run()
    captured = capsys.readouterr()
    assert "No experiments directory" in captured.out


def test_check_passes_full_setup(initialized_project, experiments_dir, capsys):
    run()
    captured = capsys.readouterr()
    assert "No issues found" in captured.out
