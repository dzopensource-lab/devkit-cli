# Copyright (c) 2026 Oussama Boudinar <lionweb01@gmail.com>
# SPDX-License-Identifier: MIT
"""Organize files in a directory into category folders."""

import shutil
from pathlib import Path

import click
from rich.console import Console

console = Console()

CATEGORIES: dict[str, list[str]] = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".md", ".odt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".ts", ".html", ".css", ".json", ".yml", ".yaml", ".sh"],
}


@click.command()
@click.argument("path", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.option("--dry-run", is_flag=True, help="Preview changes without moving files.")
def organize(path: Path, dry_run: bool) -> None:
    """Organize files in PATH into category folders."""
    console.print(f"[bold cyan]Organizing:[/] {path}")
    if dry_run:
        console.print("[yellow]Dry-run mode — no files will be moved.[/]")

    moved = 0
    for file in sorted(path.iterdir()):
        if not file.is_file():
            continue

        category = next(
            (cat for cat, exts in CATEGORIES.items() if file.suffix.lower() in exts),
            "Other",
        )
        target_dir = path / category

        if dry_run:
            console.print(f"  [dim]→[/] {file.name}  →  {category}/")
        else:
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(file), str(target_dir / file.name))

        moved += 1

    verb = "Would move" if dry_run else "Moved"
    console.print(f"[green]✓[/] {verb} {moved} file(s).")