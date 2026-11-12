# Real-World Examples

Practical use cases for devkit in real scenarios.

## Scenario 1: Monthly Downloads Cleanup

Problem: Your Downloads folder has 200 files: PDFs, images, ZIPs, old installers.

Solution:

devkit organize ~/Downloads --dry-run
devkit organize ~/Downloads

Result: Your Downloads folder now has 7 neat subfolders instead of 200 scattered files.

## Scenario 2: Start a New Web Project in 5 Seconds

Problem: Every time you start a new website, you create index.html, style.css, script.js manually.

Solution:

devkit scaffold portfolio
cd portfolio
code .

Result: 3 files ready, structure in place. Start coding immediately.

## Scenario 3: Daily Standup Prep

Problem: Before your standup, you need to remember: what branch am I on? how many commits this week?

Solution:

cd my-project
devkit git-stats

Result:

Branch        | feature/login
Total commits | 47
Last commit   | feat: add OAuth2 flow
Last author   | Oussama Boudinar

Copy, paste into your daily message. Done in 3 seconds.

## Scenario 4: Combining Commands

devkit organize ~/Desktop
devkit scaffold new-idea --type python-cli
cd new-idea
git init
devkit git-stats