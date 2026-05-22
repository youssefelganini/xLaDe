import os
from xlade.cli.doctor import run


def test_doctor_detects_missing_lake(tmp_project, capsys, monkeypatch):
    monkeypatch.setattr("shutil.which", lambda x: None)
    run()
    captured = capsys.readouterr()
    assert "lake not found" in captured.out


def test_doctor_detects_missing_lean_core(tmp_project, capsys):
    run()
    captured = capsys.readouterr()
    assert "lean-core missing" in captured.out


def test_doctor_detects_lean_toolchain(tmp_project, capsys):
    open("lean-toolchain", "w").write("leanprover/lean4:stable\n")
    run()
    captured = capsys.readouterr()
    assert "lean-toolchain present" in captured.out


def test_doctor_detects_lean_core_present(tmp_project, capsys):
    os.makedirs("lean-core")
    run()
    captured = capsys.readouterr()
    assert "lean-core submodule present" in captured.out
