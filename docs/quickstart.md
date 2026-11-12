# Quick Start - 60 Seconds

Get devkit running in under a minute.

## Step 1: Install (20 sec)

git clone https://github.com/dzopensource-lab/devkit-cli.git
cd devkit-cli
pip install -e .

## Step 2: Verify (5 sec)

devkit --version

## Step 3: Try your first command (10 sec)

devkit organize . --dry-run

This shows what organize would do in your current folder - without moving anything.

## Step 4: Try a real command (10 sec)

devkit scaffold my-first-project --type web

## Step 5: Inspect a git repo (10 sec)

devkit git-stats

Done! You know the 3 main commands.

## Next Steps

- Commands reference: docs/commands.md
- Examples: docs/examples.md
- Back to README: ../README.md