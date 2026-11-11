# Copyright (c) 2026 Oussama Boudinar <lionweb01@gmail.com>
# SPDX-License-Identifier: MIT
"""Entry point for the DevKit CLI."""

import click

from devkit.commands import git_stats, organize, scaffold


@click.group()
@click.version_option(package_name="devkit-cli")
def main() -> None:
    """DevKit — a modern CLI toolkit for developers."""
    pass


main.add_command(organize.organize)
main.add_command(scaffold.scaffold)
main.add_command(git_stats.git_stats)


if __name__ == "__main__":
    main()