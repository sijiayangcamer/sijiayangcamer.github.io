# CAMER Lab Publication Management Guide

**Complete Guide for Lab Managers**
**Version 2.0 | Last Updated: January 2026**

---

## Overview

This guide provides complete instructions for adding new publications to the CAMER lab website. When you add a publication correctly, it will automatically:

✅ Appear on the Publications page, grouped by year
✅ Be filterable by research area (Communication of Morality, Artificial Influence, Translational Communication Interventions)
✅ Show up in "Recent Publications" on the homepage (5 most recent)
✅ Display corresponding author markers with asterisks (*)
✅ Link to full PDF and DOI

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Step-by-Step Instructions](#step-by-step-instructions)
3. [BibTeX Templates](#bibtex-templates)
4. [Field Reference](#field-reference)
5. [File Organization](#file-organization)
6. [Building the Site](#building-the-site)
7. [Verification Checklist](#verification-checklist)
8. [Troubleshooting](#troubleshooting)
9. [Printable Checklist](#printable-checklist)
10. [Quick Reference](#quick-reference)

---

## Quick Start

**For experienced users: 5-step process**

1. **Add BibTeX entry** to top of `_bibliography/papers.bib`
2. **Add preview image** to `assets/img/publication_preview/`
3. **Add PDF** to `assets/pdf/`
4. **Build site:** `cd ~/Documents/sijiayangcamer.github.io && bundle exec jekyll build`
5. **Verify** in `_site/publications/index.html` and `_site/index.html`

**Key formatting rules:**
- Authors: `{LastName, FirstName and LastName, FirstName}`
- Corresponding: `{LastName, FirstName}` (must match author format exactly)
- Category: `{morality}`, `{artificial}`, or `{translational}` (required)
- PDF filename must match BibTeX key exactly

⚠️ **Most common mistake:** Corresponding author format doesn't match → no asterisk appears

[Skip to Templates](#bibtex-templates) | [Skip to Troubleshooting](#troubleshooting)

---

## Step-by-Step Instructions

### Step 1: Gather Required Files

Before starting, collect:

- [ ] **PDF file** - Final published version of the paper
- [ ] **Thumbnail image** - Figure, visualization, or graphical abstract (800-1200px wide, PNG or JPG)
- [ ] **Complete metadata:**
  - All author names
  - Corresponding author(s)
  - DOI
  - Volume/issue/page numbers (if available)
  - Full abstract text
  - Journal or conference name

### Step 2: Add BibTeX Entry

**Location:** `_bibliography/papers.bib`

**Action:** Open the file and add your entry **at the top** (after any file header comments)

**Template:** See [BibTeX Templates](#bibtex-templates) section below

**Important notes:**
- Insert at the TOP for newest publications to appear first
- Use `@article` for journal articles, `@inproceedings` for conference papers
- BibTeX key format: `firstauthorYEARkeyword` (e.g., `liu2025eyetracking`)
- Key must be unique across all entries

### Step 3: Add Preview Image

**Location:** `assets/img/publication_preview/`

**Naming convention:** `lastname_year_keyword.png`
- Example: `liu_2025_visual.png`
- Use underscores, lowercase
- Must match filename in `preview={...}` field

**Image requirements:**
- **Format:** PNG (preferred) or JPG
- **Dimensions:** 800-1200px wide recommended
- **Aspect ratio:** 16:9 or 4:3 works best
- **Content:** Key figure, chart, or graphical abstract from paper
- **Quality:** Clear and readable when displayed as thumbnail

### Step 4: Add PDF File

**Location:** `assets/pdf/`

**Naming convention:** Must match BibTeX key **exactly** + `.pdf`
- BibTeX key: `liu2025eyetracking`
- PDF filename: `liu2025eyetracking.pdf`
- Case-sensitive!

**File requirements:**
- Final published version (not preprint)
- Must be named in `pdf={...}` field

### Step 5: Build the Site

Open Terminal and run:

```bash
cd /Users/sijiayang/Documents/sijiayangcamer.github.io
bundle exec jekyll build
```

**Expected output:**
```
Configuration file: _config.yml
            Source: /Users/sijiayang/Documents/sijiayangcamer.github.io
       Destination: /Users/sijiayang/Documents/sijiayangcamer.github.io/_site
      Generating...
                    done in 6.049 seconds.
```

**If you see errors:** Check [Troubleshooting](#troubleshooting) section

### Step 6: Verify Publication

**Check these locations:**

1. **Publications page:** `_site/publications/index.html`
2. **Homepage:** `_site/index.html`

**What to verify:** See [Verification Checklist](#verification-checklist) section

---

## BibTeX Templates

### Journal Article Template

Copy and paste this template into `papers.bib`:

```bibtex
@article{firstauthorYEARkeyword,
  % REQUIRED FIELDS
  title={Publication Title Here},
  author={LastName, FirstName and LastName, FirstName and Yang, Sijia},
  journal={Journal Name},
  year={2025},
  doi={10.xxxx/xxxxx},
  abbr={JournalAbbrev},
  preview={firstauthor_year_keyword.png},
  category={translational},
  abstract={Full abstract text here. Can span multiple lines. Include all details from the published abstract.},
  corresponding={Yang, Sijia},
  pdf={firstauthorYEARkeyword.pdf},

  % OPTIONAL FIELDS (delete if not applicable)
  volume={XX},
  number={X},
  pages={XXX--XXX},
  note={First two authors contributed equally},
  replication={https://osf.io/xxxxx},
  selected={true},
}
```

**Category options:**
- `category={morality}` - Communication of Morality
- `category={artificial}` - Artificial Influence
- `category={translational}` - Translational Communication Interventions

### Conference Paper Template

```bibtex
@inproceedings{firstauthorYEARkeyword,
  % REQUIRED FIELDS
  title={Conference Paper Title Here},
  author={LastName, FirstName and LastName, FirstName and Yang, Sijia},
  booktitle={Proceedings of the Conference Name},
  year={2025},
  doi={10.xxxx/xxxxx},
  abbr={ConfAbbrev},
  preview={firstauthor_year_keyword.png},
  category={artificial},
  abstract={Full abstract text here. Can span multiple lines. Include all details from the published abstract.},
  corresponding={Yang, Sijia},
  pdf={firstauthorYEARkeyword.pdf},

  % OPTIONAL FIELDS (delete if not applicable)
  pages={XXX--XXX},
  note={First two authors contributed equally},
  replication={https://osf.io/xxxxx},
  selected={true},
}
```

### Real Example from CAMER Lab

```bibtex
@article{liu2025eyetracking,
  title={Visual attention and memory retention of cannabis warning labels: An eye-tracking experiment with young adults},
  author={Liu, Jiaying and Mi, Ranran Z. and Jeon, Moonsun and Fabbricatore, Jessica L. and Wicke, Rebekah and Cojulun, Lauren Raquel and Yang, Sijia},
  journal={Annals of Behavioral Medicine},
  volume={59},
  number={1},
  year={2025},
  note={Liu and Mi share first authorship},
  doi={10.1093/abm/kaaf094},
  abbr={ABM},
  preview={liu_2025_visual.png},
  category={translational},
  abstract={Cannabis use is rising among young adults, while their perceived risks are declining. Existing cannabis warning labels (CWLs), often dense, generic, and text-only, struggle to sustain attention or promote effective risk recognition. Drawing on construal-level theory, this study investigates whether the concreteness of textual and pictorial elements improves CWL effectiveness.},
  corresponding={Yang, Sijia},
  pdf={liu2025eyetracking.pdf},
  replication={https://osf.io/k97xh},
}
```

---

## Field Reference

### Required Fields

| Field | Description | Example | Notes |
|-------|-------------|---------|-------|
| **title** | Publication title | `{Visual attention and memory retention...}` | Enclose in braces |
| **author** | All authors | `{Liu, Jiaying and Yang, Sijia}` | **Must use "Last, First" format** separated by " and " |
| **journal** | Journal name (articles) | `{Annals of Behavioral Medicine}` | Use full journal name |
| **booktitle** | Conference name (proceedings) | `{Proceedings of CHI 2025}` | For @inproceedings only |
| **year** | Publication year | `{2025}` | 4-digit year |
| **doi** | Digital Object Identifier | `{10.1093/abm/kaaf094}` | **Just the identifier, no https://** |
| **abbr** | Venue abbreviation | `{ABM}` | Shown as colored badge |
| **preview** | Thumbnail filename | `{liu_2025_visual.png}` | Must exist in assets/img/publication_preview/ |
| **category** | Research area | `{translational}` | **Required:** morality, artificial, or translational |
| **abstract** | Full abstract | `{Your abstract...}` | Can span multiple lines |
| **corresponding** | Corresponding author(s) | `{Yang, Sijia}` | **Must match author format exactly** |
| **pdf** | PDF filename | `{liu2025eyetracking.pdf}` | Must match BibTeX key |

### Optional Fields

| Field | Description | Example |
|-------|-------------|---------|
| **volume** | Journal volume | `{59}` |
| **number** | Issue number | `{1}` |
| **pages** | Page range | `{123--145}` |
| **note** | Special authorship notes | `{First two authors contributed equally}` |
| **replication** | Replication materials link | `{https://osf.io/k97xh}` |
| **selected** | Mark as featured | `{true}` |

### Category Values (CRITICAL)

**You MUST include exactly one of these values:**

- **`morality`** → Communication of Morality tab
- **`artificial`** → Artificial Influence tab
- **`translational`** → Translational Communication Interventions tab

⚠️ **Without a category field, publication only appears in "All" tab**

### Formatting Rules

#### Author Names

**Format:** `LastName, FirstName`

✅ **Correct:**
```bibtex
author={Liu, Jiaying and Mi, Ranran Z. and Yang, Sijia}
```

❌ **Wrong:**
```bibtex
author={Jiaying Liu and Ranran Z. Mi and Sijia Yang}
```

**Multiple authors:** Separate with ` and ` (spaces before and after)

**Middle initials:** Include them: `Mi, Ranran Z.`

#### Corresponding Authors

**Must match author format exactly!**

✅ **Correct:**
```bibtex
author={Liu, Jiaying and Yang, Sijia}
corresponding={Yang, Sijia}
```

❌ **Wrong:**
```bibtex
author={Liu, Jiaying and Yang, Sijia}
corresponding={Sijia Yang}    % Wrong format!
```

**Multiple corresponding authors:**
```bibtex
corresponding={Yang, Sijia and Cascio, Christopher N.}
```

#### DOI Format

**Use just the identifier, not the full URL**

✅ **Correct:** `doi={10.1093/abm/kaaf094}`
❌ **Wrong:** `doi={https://doi.org/10.1093/abm/kaaf094}`

---

## File Organization

```
sijiayangcamer.github.io/
│
├── _bibliography/
│   └── papers.bib                      ← Add BibTeX entries here
│
├── assets/
│   ├── img/
│   │   └── publication_preview/        ← Add thumbnail images here
│   │       ├── liu_2025_visual.png
│   │       ├── kim_2024_textual.png
│   │       └── ...
│   │
│   └── pdf/                            ← Add PDF files here
│       ├── liu2025eyetracking.pdf
│       ├── kim2024textual.pdf
│       └── ...
│
└── _site/                              ← Generated site (check here after build)
    ├── index.html                      ← Homepage
    └── publications/
        └── index.html                  ← Publications page
```

**File naming conventions:**

| File Type | Location | Naming | Example |
|-----------|----------|--------|---------|
| BibTeX entry | `_bibliography/papers.bib` | `firstauthorYEARkeyword` | `liu2025eyetracking` |
| PDF | `assets/pdf/` | `{bibtex_key}.pdf` | `liu2025eyetracking.pdf` |
| Preview image | `assets/img/publication_preview/` | `lastname_year_keyword.png` | `liu_2025_visual.png` |

---

## Building the Site

### Build Command

```bash
cd /Users/sijiayang/Documents/sijiayangcamer.github.io
bundle exec jekyll build
```

### Expected Output

```
Configuration file: _config.yml
            Source: /Users/sijiayang/Documents/sijiayangcamer.github.io
       Destination: /Users/sijiayang/Documents/sijiayangcamer.github.io/_site
 Incremental build: disabled. Enable with --incremental
      Generating...
                    done in 6.049 seconds.
```

### Common Build Errors

| Error Message | Likely Cause | Solution |
|---------------|--------------|----------|
| "Liquid Exception: undefined method" | BibTeX syntax error | Check for unmatched braces `{}` |
| "Could not read file" | Missing PDF or image | Verify file exists and path is correct |
| "Invalid date" | Year format wrong | Use 4-digit year: `{2025}` not `{25}` |

---

## Verification Checklist

### Publications Page Verification

Open `_site/publications/index.html` in a browser and check:

- [ ] Publication appears in correct **year section**
- [ ] Publication visible when **"All" tab** is selected
- [ ] Publication appears under correct **research area tab**:
  - [ ] Communication of Morality (if `category={morality}`)
  - [ ] Artificial Influence (if `category={artificial}`)
  - [ ] Translational Communication Interventions (if `category={translational}`)
- [ ] **Title** is correct
- [ ] All **authors** are listed
- [ ] **Corresponding author(s) have asterisk (*)** ← **CRITICAL CHECK**
- [ ] **Journal/conference name** is correct
- [ ] **Year** is correct
- [ ] **Abstract** is visible and complete below the entry
- [ ] **Preview thumbnail** displays correctly
- [ ] **DOI button** opens correct DOI page
- [ ] **PDF button** opens the PDF file
- [ ] **Replication button** works (if applicable)

### Homepage Verification

Open `_site/index.html` in a browser and check:

- [ ] Publication appears in **"Recent Publications"** section (if one of 5 most recent)
- [ ] **Corresponding author has asterisk (*)** ← **CRITICAL CHECK**
- [ ] **Title** displays correctly
- [ ] **Authors** display correctly
- [ ] **Journal name** displays correctly
- [ ] **PDF button** opens the PDF

### Common Issues Quick Check

| Issue | Check This |
|-------|------------|
| ❌ No asterisk on corresponding author | `corresponding={Last, First}` matches author format exactly |
| ❌ Publication not in research area tab | `category={morality}`, `{artificial}`, or `{translational}` is present |
| ❌ PDF link broken | PDF filename matches BibTeX key exactly (case-sensitive) |
| ❌ Preview image not showing | Image filename in `preview={...}` matches file in directory |
| ❌ Publication not appearing at all | Check BibTeX syntax (matched braces, commas) |

---

## Troubleshooting

### Problem 1: Corresponding Author Asterisk Not Appearing

**Symptoms:** The corresponding author's name appears but without an asterisk (*)

**This is the #1 most common issue!**

**Cause 1: Format mismatch**

❌ **Wrong:**
```bibtex
author={Liu, Jiaying and Yang, Sijia}
corresponding={Sijia Yang}    % First Last format
```

✅ **Correct:**
```bibtex
author={Liu, Jiaying and Yang, Sijia}
corresponding={Yang, Sijia}    % Last, First format
```

**Cause 2: Name doesn't match exactly**

If author is listed as `Yang, S.`, corresponding must also be `Yang, S.` (not `Yang, Sijia`)

Check for:
- Extra spaces
- Middle initials
- Spelling differences

**Cause 3: Multiple corresponding authors syntax**

❌ **Wrong:** `corresponding={Yang, Sijia, Smith, John}`
✅ **Correct:** `corresponding={Yang, Sijia and Smith, John}`

Use ` and ` to separate (with spaces)

### Problem 2: Publication Not in Research Area Tab

**Symptoms:** Publication shows in "All" tab but not in Communication of Morality, Artificial Influence, or Translational tabs

**Cause:** Missing or incorrect `category` field

**Solution:** Add the category field with exactly one of these values:

```bibtex
category={morality},       % Communication of Morality
category={artificial},     % Artificial Influence
category={translational},  % Translational Communication Interventions
```

⚠️ **Must be lowercase and exactly as shown**

### Problem 3: PDF or Preview Image Not Found

**Symptoms:** Broken link or missing image

**Checklist:**

1. **File exists in correct directory?**
   - PDFs: `assets/pdf/`
   - Images: `assets/img/publication_preview/`

2. **Filename matches exactly?** (case-sensitive)
   - BibTeX key: `liu2025eyetracking`
   - PDF must be: `liu2025eyetracking.pdf`
   - Preview can be: `liu_2025_visual.png`

3. **File extension correct?**
   - PDFs: `.pdf`
   - Images: `.png` or `.jpg`

4. **Filename specified in BibTeX?**
   ```bibtex
   pdf={liu2025eyetracking.pdf},
   preview={liu_2025_visual.png},
   ```

### Problem 4: BibTeX Parsing Errors During Build

**Symptoms:** Build fails with errors about BibTeX syntax

**Common causes:**

1. **Unmatched braces**
   - Every `{` must have a closing `}`
   - Check nested braces carefully

2. **Missing commas**
   - Each field except the last must end with a comma
   ```bibtex
   title={My Title},     % comma required
   author={Smith, John}, % comma required
   year={2025}           % no comma on last field
   ```

3. **Special characters**
   - Use LaTeX escaping:
     - `\&` for &
     - `\%` for %
     - `\_` for _

4. **Smart quotes**
   - Don't copy from Word/Google Docs
   - Use straight quotes: `"` not `"` or `"`

**How to find the error:**
1. Look at the error message for line number
2. Check that line and surrounding lines for syntax issues
3. Use a text editor with brace matching

### Problem 5: Publication Not on Homepage

**Symptoms:** Publication shows on publications page but not in "Recent Publications" on homepage

**Causes:**

1. **Not in top 5 most recent**
   - Homepage shows only 5 newest publications
   - Check if other publications have more recent years

2. **Position in papers.bib**
   - Publications are shown in order from top of file
   - Make sure you added your entry at the TOP

**Note:** Publications are sorted by year, then by position in file

---

## Printable Checklist

**Publication Title:** _________________________________

**First Author:** _________________________________

**BibTeX Key:** _________________________________

**Date Added:** _________________________________

---

### Pre-Addition

- [ ] PDF file obtained (final published version)
- [ ] Thumbnail image prepared (figure/visualization from paper)
- [ ] Complete metadata collected:
  - [ ] All author names (in "Last, First" format)
  - [ ] Corresponding author(s) confirmed
  - [ ] DOI confirmed
  - [ ] Volume/issue numbers (if available)
  - [ ] Page numbers (if available)
  - [ ] Full abstract text
- [ ] Research area determined:
  - [ ] Communication of Morality (`category={morality}`)
  - [ ] Artificial Influence (`category={artificial}`)
  - [ ] Translational Communication Interventions (`category={translational}`)

### File Addition

- [ ] **BibTeX entry added** to `_bibliography/papers.bib`
  - [ ] Added at TOP of file (after header comments)
  - [ ] All required fields included
  - [ ] Authors formatted as "Last, First and Last, First"
  - [ ] Corresponding author matches author format exactly
  - [ ] Category field included (morality/artificial/translational)
  - [ ] DOI is just the identifier (no https://)
  - [ ] PDF filename matches BibTeX key
  - [ ] Preview filename included

- [ ] **Preview image added** to `assets/img/publication_preview/`
  - [ ] Filename: `_____________________________.png`
  - [ ] Image is 800-1200px wide
  - [ ] Image is clear and representative

- [ ] **PDF added** to `assets/pdf/`
  - [ ] Filename matches BibTeX key exactly: `_____________________________.pdf`
  - [ ] PDF opens correctly

### Build & Verification

- [ ] **Site rebuilt successfully**
  ```bash
  cd /Users/sijiayang/Documents/sijiayangcamer.github.io
  bundle exec jekyll build
  ```
  - [ ] No error messages
  - [ ] Build completed ("done in X seconds")

- [ ] **Publications page verified** (`_site/publications/index.html`)
  - [ ] Publication appears in correct year section
  - [ ] Publication visible in "All" tab
  - [ ] Publication appears under correct research area tab
  - [ ] Title correct
  - [ ] All authors listed
  - [ ] Corresponding author has asterisk (*) ← **CHECK CAREFULLY**
  - [ ] Journal/conference name correct
  - [ ] Year correct
  - [ ] Abstract visible and complete
  - [ ] Preview thumbnail displays
  - [ ] DOI button works
  - [ ] PDF button works
  - [ ] Replication button works (if applicable)

- [ ] **Homepage verified** (`_site/index.html`)
  - [ ] Publication in "Recent Publications" (if one of 5 most recent)
  - [ ] Corresponding author has asterisk (*) ← **CHECK CAREFULLY**
  - [ ] Title displays correctly
  - [ ] Authors display correctly
  - [ ] Journal name displays correctly
  - [ ] PDF button works

### Sign-off

- [ ] All checks passed
- [ ] Ready for deployment

**Checked by:** _________________________________

**Date:** _________________________________

**Notes/Issues:**
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________

---

## Quick Reference

### Key Formatting Rules

```bibtex
% Author format
author={LastName, FirstName and LastName, FirstName}

% Corresponding author (must match author format)
corresponding={LastName, FirstName}

% Category (choose one)
category={morality}      % Communication of Morality
category={artificial}    % Artificial Influence
category={translational} % Translational Communication Interventions

% DOI (no https://)
doi={10.xxxx/xxxxx}

% Files
pdf={bibtexkey.pdf}                    % Must match BibTeX key exactly
preview={lastname_year_keyword.png}    % Can use different naming
```

### File Locations

| What | Where |
|------|-------|
| BibTeX entries | `_bibliography/papers.bib` |
| PDF files | `assets/pdf/` |
| Preview images | `assets/img/publication_preview/` |
| Check results | `_site/publications/index.html` and `_site/index.html` |

### Build Command

```bash
cd /Users/sijiayang/Documents/sijiayangcamer.github.io
bundle exec jekyll build
```

### File Naming

| Type | Format | Example |
|------|--------|---------|
| BibTeX key | `firstauthorYEARkeyword` | `liu2025eyetracking` |
| PDF filename | `{bibtex_key}.pdf` | `liu2025eyetracking.pdf` |
| Preview image | `lastname_year_keyword.png` | `liu_2025_visual.png` |

### Most Common Mistakes

1. ❌ Corresponding author format doesn't match author format
2. ❌ Missing `category` field
3. ❌ PDF filename doesn't match BibTeX key exactly
4. ❌ Added entry at bottom of file instead of top
5. ❌ Included `https://doi.org/` in DOI field

---

## Future: Team Member Integration

When the people page is built, publications will automatically link to team member profiles.

### Option A: Author-Based Filtering

Team member pages can show their publications:

```liquid
{% bibliography --query @*[author~=LastName] %}
```

### Option B: Clickable Author Names

To make author names clickable:

Edit `_data/coauthors.yml`:

```yaml
"cotter":
  - firstname: ["Lynne", "L.", "L. M.", "Lynne M."]
    url: /people/#lynne-cotter

"liu":
  - firstname: ["Jiaying", "J."]
    url: /people/#jiaying-liu
```

This automatically hyperlinks names in all publications to their profile pages.

---

## Contact & Support

**Need help?**
- Sijia Yang (Lab PI): sijia.yang@wisc.edu

**Maintenance scripts:**
- Verify BibTeX against PDFs: `_scripts/verify_bib_against_pdfs.py`
- Compare with Zotero: `_scripts/detailed_comparison_fixed.py`

---

**Document maintained by:** CAMER Lab
**Last updated:** January 2026
**Version:** 2.0 (Consolidated)
