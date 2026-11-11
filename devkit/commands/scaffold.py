# Copyright (c) 2026 Oussama Boudinar <lionweb01@gmail.com>
# SPDX-License-Identifier: MIT
"""Scaffold new projects from built-in templates."""

from pathlib import Path

import click
from rich.console import Console

console = Console()

TEMPLATES: dict[str, dict[str, str]] = {
    "web": {
        "index.html": (
            "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
            "  <meta charset=\"UTF-8\" />\n"
            "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n"
            "  <title>New Project</title>\n"
            "  <link rel=\"stylesheet\" href=\"style.css\" />\n"
            "</head>\n<body>\n  <h1>Hello, world!</h1>\n"
            "  <script src=\"script.js\"></script>\n</body>\n</html>\n"
        ),
        "style.css": "body {\n  font-family: system-ui, sans-serif;\n  margin: 2rem;\n}\n",
        "script.js": "console.log('Ready.');\n",
    },
    "python-cli": {
        "main.py": (
            "import click\n\n\n"
            "@click.command()\n"
            "def main() -> None:\n"
            '    """My CLI tool."""\n'
            "    click.echo('Hello!')\n\n\n"
            'if __name__ == "__main__":\n'
            "    main()\n"
        ),
        "requirements.txt": "click>=8.1.0\n",
    },
}


@click.command()
@click.argument("name")
@click.option(
    "--type",
    "template",
    type=click.Choice(TEMPLATES.keys()),
    default="web",
    show_default=True,
)
def scaffold(name: str, template: str) -> None:
    """Create a new project NAME from a template."""
    target = Path(name)
    if target.exists():
        console.print(f"[red]✗[/] Directory '{name}' already exists.")
        raise SystemExit(1)

    files = TEMPLATES[template]
    for filename, content in files.items():
        file_path = target / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content)

    console.print(f"[green]✓[/] Created '{name}' ({template}) — {len(files)} file(s).")
    console.print(f"[dim]  cd {name}[/]")