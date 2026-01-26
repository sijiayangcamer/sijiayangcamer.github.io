# Scripts

This directory contains utility scripts for maintaining the CAMER Lab website.

## update_member_publications.py

Automatically matches publications from `_bibliography/papers.bib` to lab members in `_data/members.yml` by author name.

### Requirements

```bash
pip install pyyaml
```

### Usage

```bash
# From the repository root
python scripts/update_member_publications.py
```

### What it does

1. Parses `_bibliography/papers.bib` to extract all publications
2. Reads `_data/members.yml` to get member names
3. Matches members to publications by comparing author names
4. Updates `_data/members.yml` with matched publications for each member
5. Publications are sorted by year (most recent first)

### Name Matching

The script handles various name formats:
- "Firstname Lastname" matches "Lastname, Firstname" (BibTeX format)
- Handles middle names/initials
- Case-insensitive matching

### Output

For each member in `graduate_students` and `undergraduate_students`, the script adds a `publications` array containing:
- `title`: Publication title
- `journal`: Journal or conference name
- `year`: Publication year
- `doi`: DOI link (if available)
- `html`: HTML/URL link (preferred over DOI if both exist)

Alumni are not processed since they don't display publications on the people page.

### When to run

Run this script whenever:
- You add new publications to `papers.bib`
- You add new members to `members.yml`
- You need to refresh the publication listings

### Example Output

```
Reading bibliography from: /path/to/_bibliography/papers.bib
Found 89 publications in bibliography

Processing graduate_students:
  Luhang Sun: 5 publications
  Thomas Hongjie Zhang: 2 publications
  Feifei Zhao: 0 publications
  ...

✓ Successfully updated members.yml with publications from papers.bib
```

### Notes

- The script preserves all existing member data (photo, email, research interest, projects, links)
- Only the `publications` field is updated/added
- Publications are automatically sorted by year, most recent first
- The "Click to see more" expandable feature on the website works when a member has >3 publications
