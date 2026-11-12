# Commands Reference

Complete documentation for all devkit commands.

## devkit organize

Sort files in a folder into categories.

### Syntax

devkit organize <PATH> [OPTIONS]

### Options

| Option | Description |
| :--- | :--- |
| --dry-run | Preview changes without moving files |
| --help | Show help |

### Categories

| Folder | Extensions |
| :--- | :--- |
| Images/ | jpg, jpeg, png, gif, svg, webp, bmp |
| Documents/ | pdf, doc, docx, txt, md, odt, xlsx, pptx |
| Videos/ | mp4, mkv, avi, mov, webm |
| Audio/ | mp3, wav, flac, ogg, m4a |
| Archives/ | zip, rar, 7z, tar, gz |
| Code/ | py, js, ts, html, css, json, yml, yaml, sh |
| Other/ | Anything else |

### Examples

devkit organize ~/Downloads --dry-run
devkit organize ~/Downloads
devkit organize C:\Users\ENIGMA\Downloads

### Safety

- Always use --dry-run first
- Only processes files (not folders)
- Skips hidden files
- Creates category folders only if needed

## devkit scaffold

Create a new project from a template.

### Syntax

devkit scaffold <NAME> [OPTIONS]

### Options

| Option | Default | Values |
| :--- | :--- | :--- |
| --type | web | web, python-cli |

### Templates

- web - Creates index.html, style.css, script.js
- python-cli - Creates main.py, requirements.txt

### Examples

devkit scaffold my-site
devkit scaffold my-tool --type python-cli

## devkit git-stats

Show statistics of a git repository.

### Syntax

devkit git-stats [PATH]

### Output

A formatted table with: current branch, total commit count, last commit message, last commit author.

### Examples

devkit git-stats
devkit git-stats /path/to/repo
devkit git-stats C:\Users\ENIGMA\devkit-cli

## Global Commands

| Command | Description |
| :--- | :--- |
| devkit --version | Show version |
| devkit --help | Show all commands |
| devkit <command> --help | Show help for a command |