# CAMER Lab Members Guide

This guide explains how to add and manage lab member profiles on the people page.

## Quick Start

**Data File**: `_data/members.yml`
**Photos**: `/assets/img/members/`
**Page**: `/people/`

---

## Adding a New Member

### 1. Prepare Member Photo

- **Size**: 400x400px minimum (square)
- **Format**: JPG or PNG
- **Filename**: Use lowercase with underscores (e.g., `jane_doe.jpg`)
- **Location**: Save to `/assets/img/members/`

### 2. Edit members.yml

Open `_data/members.yml` and add the member under the appropriate category.

#### Graduate Student Example

```yaml
graduate_students:
  - name: "Jane Doe"
    photo: "members/jane_doe.jpg"
    email: "janedoe@wisc.edu"
    projects:
      - moral_messaging  # Must match project file name in _projects/
      - health_intervention
    links:
      cv: "/assets/pdf/members/jane_doe_cv.pdf"
      website: "https://janedoe.com"
      google_scholar: "https://scholar.google.com/citations?user=XXXXX"
      github: "https://github.com/janedoe"
      osf: "https://osf.io/xxxxx/"
      linkedin: "https://linkedin.com/in/janedoe"
      twitter: "https://twitter.com/janedoe"
```

#### Undergraduate Student Example

```yaml
undergraduate_students:
  - name: "John Smith"
    photo: "members/john_smith.jpg"
    email: "jsmith@wisc.edu"
    projects:
      - data_analysis
    links:
      website: "https://johnsmith.com"
      github: "https://github.com/johnsmith"
      linkedin: "https://linkedin.com/in/johnsmith"
```

#### Alumni Example

```yaml
alumni:
  - name: "Alice Johnson"
    photo: "members/alice_johnson.jpg"
    current_position: "Assistant Professor, University of Example"
    email: "alice@example.edu"  # Optional
    website: "https://alicejohnson.com"
```

---

## Field Reference

### Required Fields

| Field | Description | Example |
|-------|-------------|---------|
| `name` | Full name | "Jane Doe" |
| `photo` | Path to photo | "members/jane_doe.jpg" |
| `email` | Email address | "janedoe@wisc.edu" |

### Optional Fields (Graduate/Undergraduate)

| Field | Description | Example |
|-------|-------------|---------|
| `projects` | List of project slugs | `- project_name` |
| `links.cv` | Path to CV PDF | "/assets/pdf/members/name_cv.pdf" |
| `links.website` | Personal website | "https://example.com" |
| `links.google_scholar` | Google Scholar profile | "https://scholar.google.com/..." |
| `links.github` | GitHub profile | "https://github.com/username" |
| `links.osf` | OSF profile | "https://osf.io/xxxxx/" |
| `links.linkedin` | LinkedIn profile | "https://linkedin.com/in/username" |
| `links.twitter` | Twitter/X profile | "https://twitter.com/username" |

### Optional Fields (Alumni)

| Field | Description | Example |
|-------|-------------|---------|
| `current_position` | Current job title and institution | "Assistant Professor, UW-Madison" |
| `email` | Email address | "alice@example.edu" |
| `website` | Personal website | "https://example.com" |

---

## Publications Auto-Population

### How It Works

The system automatically matches member names with publications in `_bibliography/papers.bib`:

1. Takes the member's name from `members.yml`
2. Searches for matching authors in `papers.bib`
3. Displays up to 3 most recent publications
4. Links to DOI or HTML URL if available

### Name Matching

The system tries multiple formats:
- "Jane Doe" matches "Jane Doe" or "Doe, Jane"
- First name + Last name combinations
- Case-insensitive matching

### Requirements

For auto-population to work:
- Member name must match exactly how it appears in `papers.bib`
- Name format in BibTeX: `author={Last, First and ...}` or `author={First Last and ...}`

### Example

**In members.yml**:
```yaml
- name: "Jane Doe"
```

**In papers.bib**:
```bibtex
@article{doe2024paper,
  author={Doe, Jane and Smith, John},  ← Will match!
  title={Paper Title},
  year={2024}
}
```

**Result**: This paper will appear under Jane Doe's profile on the people page.

---

## Linking Projects

### Project Slugs

The `projects` field links members to research projects.

**Format**: Use the project file name without extension

**Example**:
- Project file: `_projects/moral_messaging.md`
- In members.yml: `- moral_messaging`

### Setting Up Project Files

Each project in `_projects/` should have frontmatter:

```yaml
---
layout: page
title: Moral Messaging Study
description: Investigating moral appeals in health communication
slug: moral_messaging
---
```

The `slug` should match the filename.

---

## Icon Links

### Available Icons

| Link Type | Icon | Icon Code |
|-----------|------|-----------|
| CV | "cv" text | N/A (styled text) |
| Website | 🔗 | `fas fa-link` |
| Google Scholar | 🎓 | `ai ai-google-scholar` |
| GitHub | 🐙 | `fab fa-github` |
| OSF | 📊 | `ai ai-osf` |
| LinkedIn | 💼 | `fab fa-linkedin` |
| Twitter/X | 🐦 | `fab fa-x-twitter` |

### Styling

- Icons display in teal/cyan (site accent color)
- Only icons with URLs in `links:` will display
- Hover effect: color change + slight movement
- Icons appear at bottom of card

---

## Member Card Display

### Graduate & Undergraduate Students

```
+----------------------------------+
| [Round Photo]                    |
| Name                             |
| email@wisc.edu                   |
|                                  |
| projects: [project 1] [project 2]|
|                                  |
| recent publications:             |
|   • Paper Title 1 (2024)        |
|   • Paper Title 2 (2023)        |
|   • Paper Title 3 (2023)        |
|                                  |
| [cv] [🔗] [🎓] [🐙] [📊] [💼] [🐦] |
+----------------------------------+
```

### Alumni

```
+----------------------------------+
| [Round Photo]                    |
| Name                             |
| Current Position                 |
| email@institution.edu            |
| website                          |
+----------------------------------+
```

---

## Common Tasks

### Add a Graduate Student

1. Get their photo (400x400px, square)
2. Save to `/assets/img/members/firstname_lastname.jpg`
3. Edit `_data/members.yml`:
   ```yaml
   graduate_students:
     - name: "Firstname Lastname"
       photo: "members/firstname_lastname.jpg"
       email: "email@wisc.edu"
       projects:
         - project_slug
       links:
         google_scholar: "https://..."
         github: "https://..."
   ```
4. Preview: `bundle exec jekyll serve`
5. Check `/people/` in browser
6. Verify publications auto-populated correctly

### Move Student to Alumni

1. Copy the entry from `graduate_students` or `undergraduate_students`
2. Add to `alumni` section
3. Update fields:
   ```yaml
   alumni:
     - name: "Firstname Lastname"
       photo: "members/firstname_lastname.jpg"
       current_position: "Job Title, Institution"
       email: "new@email.com"  # Optional
       website: "https://..."
   ```
4. Remove from original section

### Update Publications

Publications auto-update from `papers.bib`. To add new publications:

1. Add publication to `_bibliography/papers.bib`
2. Ensure author name matches member name in `members.yml`
3. Rebuild site: `bundle exec jekyll serve`
4. Publications automatically appear on member's card

### Add Project Links

1. Ensure project exists in `_projects/project_name.md`
2. Note the project filename (without `.md`)
3. Add to member's `projects` list:
   ```yaml
   projects:
     - project_name
   ```
4. Button will link to the project page automatically

---

## Troubleshooting

### Publications Not Appearing

**Problem**: Member's publications don't show up automatically

**Solutions**:
1. Check name spelling matches exactly in both files
2. Verify name format in papers.bib: `Doe, Jane` or `Jane Doe`
3. Check that author field in BibTeX is correct
4. Try different name variants (first last, last first)

### Project Links Broken

**Problem**: Project tag shows but doesn't link

**Solutions**:
1. Check project file exists: `_projects/project_slug.md`
2. Verify slug matches filename exactly
3. Ensure project has proper frontmatter

### Photo Not Displaying

**Problem**: Placeholder icon shows instead of photo

**Solutions**:
1. Check photo path in members.yml: `members/filename.jpg`
2. Verify photo exists in `/assets/img/members/`
3. Check filename spelling and case sensitivity
4. Try rebuilding: `bundle exec jekyll serve`

### Icons Not Showing

**Problem**: Link icons missing or broken

**Solutions**:
1. Verify icon fonts loaded (Font Awesome, Academicons)
2. Check URL format is correct (full URL with https://)
3. Ensure proper indentation in YAML
4. Clear browser cache

---

## Styling Customization

Member card styles are in `_sass/_base.scss` under "People/Members Page Styles".

### Common Customizations

**Change grid columns**:
```scss
.members-grid {
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); // Adjust 280px
}
```

**Change photo size**:
```scss
.member-photo-container {
  width: 180px;  // Adjust
  height: 180px; // Adjust
}
```

**Change card hover effect**:
```scss
.member-card {
  &:hover {
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15); // More shadow
    transform: translateY(-4px); // More lift
  }
}
```

---

## File Structure

```
/
├── _data/
│   └── members.yml                 ← Member data
│
├── _includes/
│   └── member_card.liquid          ← Card template
│
├── _pages/
│   └── people.md                   ← People page
│
├── _sass/
│   └── _base.scss                  ← Styles (bottom of file)
│
├── assets/img/members/             ← Member photos
│   ├── jane_doe.jpg
│   ├── john_smith.jpg
│   └── ...
│
└── MEMBERS_GUIDE.md                ← This file
```

---

## Best Practices

✅ **DO**:
- Use square photos (1:1 ratio)
- Keep photo file sizes reasonable (< 500KB)
- Use consistent naming (lowercase, underscores)
- Update alumni when students graduate
- Check publication matching after adding members
- Preview locally before committing

❌ **DON'T**:
- Use non-square photos (will be cropped)
- Forget to add photo to `/assets/img/members/`
- Use special characters in filenames
- Leave broken project links
- Skip the preview step

---

## Quick Reference: YAML Template

```yaml
graduate_students:
  - name: "Full Name"
    photo: "members/filename.jpg"
    email: "email@wisc.edu"
    projects:
      - project_slug_1
      - project_slug_2
    links:
      cv: "/assets/pdf/members/name_cv.pdf"
      website: "https://..."
      google_scholar: "https://..."
      github: "https://..."
      osf: "https://..."
      linkedin: "https://..."
      twitter: "https://..."

undergraduate_students:
  - name: "Full Name"
    photo: "members/filename.jpg"
    email: "email@wisc.edu"
    projects:
      - project_slug
    links:
      website: "https://..."
      github: "https://..."

alumni:
  - name: "Full Name"
    photo: "members/filename.jpg"
    current_position: "Title, Institution"
    email: "email@example.edu"
    website: "https://..."
```

---

## Questions?

- Check the example entries in `_data/members.yml`
- Review `_includes/member_card.liquid` to see how data is displayed
- Test changes locally with `bundle exec jekyll serve`
- View people page at http://localhost:4000/people/

Remember: Publications auto-populate from `papers.bib`, so keep author names consistent!
