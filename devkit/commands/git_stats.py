# Copyright (c) 2026 Oussama Boudinar <lionweb01@gmail.com>
# SPDX-License-Identifier: MIT
"""Show quick statistics for a git repository."""

import subprocess
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

console = Console()


def _git(path: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(path), *args], text=True
    ).strip()


@click.command()
@click.argument(
    "path",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default=".",
)
def git_stats(path: Path) -> None:
    """Show git statistics for the repository in PATH."""
    if not (path / ".git").exists():
        console.print(f"[red]✗[/] No git repository found in {path}")
        raise SystemExit(1)

    try:
        branch = _git(path, "rev-parse", "--abbrev-ref", "HEAD")
        commits = _git(path, "rev-list", "--count", "HEAD")
        last_commit = _git(path, "log", "-1", "--pretty=%s")
        author = _git(path, "log", "-1", "--pretty=%an")
    except subprocess.CalledProcessError:
        console.print("[red]✗[/] Failed to read git history.")
        raise SystemExit(1)

    table = Table(title=f"Git Stats — {path.resolve().name}")
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")
    table.add_row("Branch", branch)
    table.add_row("Total commits", commits)
    table.add_row("Last commit", last_commit)
    table.add_row("Last author", author)

    console.print(table)