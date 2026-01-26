# Pre-commit Hook Guide

A pre-commit hook has been set up to automatically update `_data/members.yml` whenever you commit changes to `_bibliography/papers.bib`.

## How It Works

1. You edit `_bibliography/papers.bib` (add/modify publications)
2. You save the file
3. You stage and commit:
   ```bash
   git add _bibliography/papers.bib
   git commit -m "Add new publications"
   ```
4. **The hook automatically runs:**
   - Detects that papers.bib changed
   - Runs the matching script
   - Updates members.yml with new publications
   - Stages members.yml for the commit
5. Both files are committed together
6. You push to GitHub

## What You'll See

When you commit changes to papers.bib, you'll see output like:

```
📚 Detected changes to papers.bib...
🔄 Automatically updating member publications...
Reading bibliography from: ...
Found 45 publications in bibliography
...
✓ Successfully updated members.yml
✓ Staged members.yml for commit
[main abc1234] Add new publications
 2 files changed, 50 insertions(+), 10 deletions(-)
```

## Manual Update (If Needed)

If you ever need to manually update members.yml without committing:

```bash
source .venv/bin/activate
python scripts/update_member_publications.py
deactivate
```

## Requirements

The hook uses the Python virtual environment (`.venv`) with PyYAML installed. This has already been set up in your repository.

## Troubleshooting

If the hook fails:
1. Check that `.venv` exists and has PyYAML installed
2. Run the script manually to see the error:
   ```bash
   source .venv/bin/activate
   python scripts/update_member_publications.py
   ```
3. Fix any errors in the script or data files
4. Try committing again

## Disabling the Hook

If you need to temporarily disable the hook:

```bash
# Rename it to disable
mv .git/hooks/pre-commit .git/hooks/pre-commit.disabled

# Rename back to enable
mv .git/hooks/pre-commit.disabled .git/hooks/pre-commit
```

## Notes

- The hook only runs when `papers.bib` is being committed
- Changes to other files won't trigger the hook
- Alumni don't get publications updated (they don't display publications on the site)
- Publications are automatically sorted by year (most recent first)
