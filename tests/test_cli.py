# Copyright (c) 2026 Oussama Boudinar <lionweb01@gmail.com>
# SPDX-License-Identifier: MIT
"""Basic CLI tests."""

from click.testing import CliRunner

from devkit.cli import main


def test_cli_help() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "DevKit" in result.output


def test_scaffold_creates_files(tmp_path) -> None:
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(main, ["scaffold", "myproj", "--type", "web"])
        assert result.exit_code == 0