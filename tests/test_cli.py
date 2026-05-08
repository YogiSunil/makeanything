from __future__ import annotations

from studyflow.cli import main


def test_cli_prints_plan_and_review(capsys):
    exit_code = main(["plan final project", "--docs", "assignment.md::Build architecture and capture evidence"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "StudyFlow Plan" in output
    assert "Review" in output
