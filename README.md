markdown

# 🛠️ DevKit CLI

**A modern CLI toolkit for developers — organize files, scaffold projects, and inspect git repositories. All in one command.**

[![Tests](https://github.com/dzopensource-lab/devkit-cli/actions/workflows/test.yml/badge.svg)](https://github.com/dzopensource-lab/devkit-cli/actions/workflows/test.yml)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Stop wasting time on repetitive tasks. `devkit` handles the boring stuff so you can focus on writing code.

---

## 🎬 Quick Start (60 seconds)

```bash
# 1. Clone and install
git clone https://github.com/dzopensource-lab/devkit-cli.git
cd devkit-cli
pip install -e .

# 2. Try it immediately
devkit organize ~/Downloads --dry-run
devkit scaffold my-new-project --type web
devkit git-stats

That's it. You're ready to go. 🚀
📖 What is DevKit?

devkit is a command-line toolkit that solves three daily problems every developer faces:
Problem	Solution	Command
🗂️ "My Downloads folder is a mess"	Auto-sort files into categories	devkit organize
🧱 "I waste 10 minutes setting up every new project"	Generate project structure instantly	devkit scaffold
📊 "I forget my repo's commit count and current branch"	See git stats in one command	devkit git-stats
✨ Features

    📂 Smart file organizer — Sorts files into Images/, Documents/, Code/, Audio/, Videos/, Archives/ automatically

    🧱 Project scaffolder — Creates ready-to-use templates for web and python-cli projects

    📊 Git inspector — Quick overview: branch, commit count, last author, last commit message

    🎨 Beautiful terminal output — Colors, tables, and clear feedback powered by rich

    🛡️ Safe by default — --dry-run mode lets you preview changes before executing

    🧪 Tested — Fully covered by pytest and GitHub Actions CI

    ⚡ Fast — No dependencies beyond click and rich

🚀 Installation
Option 1: Install from source (recommended for now)
bash

git clone https://github.com/dzopensource-lab/devkit-cli.git
cd devkit-cli
pip install -e .

Option 2: Install from PyPI (coming soon)
bash

pip install dz-devkit-cli

Verify installation
bash

devkit --version
# devkit-cli, version 0.1.0

devkit --help
# Usage: devkit [OPTIONS] COMMAND [ARGS]...

📚 Commands Reference
📂 devkit organize — Sort files into folders

Syntax:
bash

devkit organize <PATH> [--dry-run]

What it does:
Scans the folder <PATH> and moves files into categorized subfolders based on their extension.

Categories:
Folder	Extensions
Images/	.jpg, .jpeg, .png, .gif, .svg, .webp, .bmp
Documents/	.pdf, .doc, .docx, .txt, .md, .odt, .xlsx, .pptx
Videos/	.mp4, .mkv, .avi, .mov, .webm
Audio/	.mp3, .wav, .flac, .ogg, .m4a
Archives/	.zip, .rar, .7z, .tar, .gz
Code/	.py, .js, .ts, .html, .css, .json, .yml, .yaml, .sh
Other/	Everything else

Example:

Before:
text

Downloads/
├── photo.jpg
├── report.pdf
├── song.mp3
├── project.zip
└── script.py

Run:
bash

devkit organize ~/Downloads

After:
text

Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Audio/
│   └── song.mp3
├── Archives/
│   └── project.zip
└── Code/
    └── script.py

Safe preview:
bash

devkit organize ~/Downloads --dry-run

Shows what would happen without moving anything. Always use this first!
🧱 devkit scaffold — Create a new project

Syntax:
bash

devkit scaffold <NAME> [--type web|python-cli]

What it does:
Creates a new folder <NAME> with a ready-to-use starter template.

Available templates:
Template 1: web (default)

Creates:

    index.html — Starter HTML5 page

    style.css — Basic styles

    script.js — Starter JS file

bash

devkit scaffold my-website

Output:
text

my-website/
├── index.html
├── style.css
└── script.js

Template 2: python-cli

Creates:

    main.py — CLI starter using click

    requirements.txt — Dependencies

bash

devkit scaffold my-tool --type python-cli

Output:
text

my-tool/
├── main.py
└── requirements.txt

📊 devkit git-stats — Inspect a git repository

Syntax:
bash

devkit git-stats [PATH]

What it does:
Displays key statistics about a git repository in a formatted table.

Example:
bash

devkit git-stats

Output:
text

        Git Stats — devkit-cli
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric        ┃ Value                        ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Branch        │ main                         │
│ Total commits │ 5                            │
│ Last commit   │ feat: add clean command      │
│ Last author   │ Oussama Boudinar             │
└───────────────┴──────────────────────────────┘

On another repo:
bash

devkit git-stats /path/to/any/repo

💡 Use Cases
Use Case 1: Monthly Downloads cleanup
bash

devkit organize ~/Downloads

Use Case 2: Start a new web project instantly
bash

devkit scaffold my-landing-page
cd my-landing-page
# Open in browser, start coding!

Use Case 3: Quick repo status before a standup meeting
bash

devkit git-stats

🗂️ Project Structure
text

devkit-cli/
├── devkit/
│   ├── __init__.py           # Package metadata
│   ├── cli.py                # Main entry point (Click group)
│   └── commands/
│       ├── organize.py       # File organizer command
│       ├── scaffold.py       # Project scaffolder command
│       └── git_stats.py      # Git stats command
├── tests/
│   └── test_cli.py           # Basic tests
├── .github/
│   └── workflows/
│       └── test.yml          # CI pipeline
├── docs/
│   ├── quickstart.md         # 60-second guide
│   ├── commands.md           # Full command reference
│   └── examples.md           # Real-world examples
├── pyproject.toml            # Package config
├── README.md                 # This file
├── CONTRIBUTING.md           # How to contribute
├── CHANGELOG.md              # Version history
└── LICENSE                   # MIT License

🛡️ Safety Notes
⚠️ Warning	Reason
Always run --dry-run first on organize	To preview before moving files
Don't organize system folders (C:\Windows, Program Files)	May require permissions and break the system
Backup important folders before organizing	Though safe, always be careful
🤝 Contributing

See CONTRIBUTING.md for guidelines.

Quick version:

    Fork the repo

    Create a branch: git checkout -b feature/my-feature

    Make changes + add tests

    Push and open a Pull Request

🧪 Testing
bash

pytest
pytest -v

🗺️ Roadmap

    ☑

    organize — Sort files into categories
    ☑

    scaffold — Create project templates
    ☑

    git-stats — Show repository statistics
    ☑

    GitHub Actions CI
    ☑

    clean command — Remove node_modules, __pycache__, .venv
    ☑

    organize --recursive — Support subfolders
    ☑

    Custom categories from devkit.toml
    ☑

    More scaffold templates (react, fastapi, vue)
    ☑

    Publish to PyPI

📄 License

MIT © 2026 Oussama Boudinar lionweb01@gmail.com — dzopensource-lab
⭐ Show your support

If devkit helped you, please give it a ⭐ on GitHub — it means a lot!
