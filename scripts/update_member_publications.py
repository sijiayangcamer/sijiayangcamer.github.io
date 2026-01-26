#!/usr/bin/env python3
"""
Automatically match publications from papers.bib to lab members in members.yml

This script:
1. Parses papers.bib to extract all publications
2. Reads members.yml to get member names
3. Matches members to publications by author name
4. Updates members.yml with matched publications (sorted by year, most recent first)

Usage:
    python scripts/update_member_publications.py
"""

import re
import yaml
from pathlib import Path
from typing import Dict, List, Set, Tuple


def parse_bibtex_file(bib_path: Path) -> List[Dict]:
    """
    Parse BibTeX file and extract publication information.

    Returns list of dicts with: title, authors, journal, year, doi, html, entry_key
    """
    publications = []

    with open(bib_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match each BibTeX entry
    entry_pattern = r'@(\w+)\{([^,]+),\s*\n(.*?)\n\}'
    entries = re.finditer(entry_pattern, content, re.DOTALL)

    for entry in entries:
        entry_type = entry.group(1)
        entry_key = entry.group(2)
        entry_content = entry.group(3)

        # Extract fields
        pub = {'entry_key': entry_key}

        # Title
        title_match = re.search(r'title\s*=\s*\{(.+?)\}', entry_content, re.DOTALL)
        if title_match:
            pub['title'] = title_match.group(1).replace('\n', ' ').strip()

        # Authors
        author_match = re.search(r'author\s*=\s*\{(.+?)\}', entry_content, re.DOTALL)
        if author_match:
            pub['authors'] = author_match.group(1).replace('\n', ' ').strip()

        # Journal (or booktitle for conference papers)
        journal_match = re.search(r'journal\s*=\s*\{(.+?)\}', entry_content, re.DOTALL)
        if journal_match:
            pub['journal'] = journal_match.group(1).replace('\n', ' ').strip()
        else:
            booktitle_match = re.search(r'booktitle\s*=\s*\{(.+?)\}', entry_content, re.DOTALL)
            if booktitle_match:
                pub['journal'] = booktitle_match.group(1).replace('\n', ' ').strip()

        # Year
        year_match = re.search(r'year\s*=\s*\{?(\d{4})\}?', entry_content)
        if year_match:
            pub['year'] = int(year_match.group(1))

        # DOI
        doi_match = re.search(r'doi\s*=\s*\{(.+?)\}', entry_content)
        if doi_match:
            pub['doi'] = doi_match.group(1).strip()

        # HTML/URL
        html_match = re.search(r'html\s*=\s*\{(.+?)\}', entry_content)
        if html_match:
            pub['html'] = html_match.group(1).strip()
        else:
            url_match = re.search(r'url\s*=\s*\{(.+?)\}', entry_content)
            if url_match:
                pub['html'] = url_match.group(1).strip()

        # PDF
        pdf_match = re.search(r'pdf\s*=\s*\{(.+?)\}', entry_content)
        if pdf_match:
            pub['pdf'] = pdf_match.group(1).strip()

        # Replication
        replication_match = re.search(r'replication\s*=\s*\{(.+?)\}', entry_content)
        if replication_match:
            pub['replication'] = replication_match.group(1).strip()

        publications.append(pub)

    return publications


def normalize_name(name: str) -> Set[str]:
    """
    Generate normalized name variants for matching.

    Returns set of possible name formats:
    - "firstname lastname"
    - "lastname, firstname"
    - "f. lastname" (first initial)
    - "firstname m. lastname" (middle initial)
    - etc.
    """
    name = name.strip()
    variants = set()

    # Handle "Lastname, Firstname" or "Lastname, Firstname M." format
    if ',' in name:
        parts = [p.strip() for p in name.split(',')]
        if len(parts) == 2:
            lastname, firstname_part = parts
            # Split firstname_part to handle middle names/initials
            firstname_parts = firstname_part.split()
            firstname = firstname_parts[0]

            # Add "Firstname Lastname"
            variants.add(f"{firstname} {lastname}".lower())
            # Add "Lastname, Firstname"
            variants.add(f"{lastname}, {firstname}".lower())

            # If there's a middle initial (e.g., "Thomas H.")
            if len(firstname_parts) > 1:
                middle = firstname_parts[1]
                # Add "Firstname M. Lastname"
                variants.add(f"{firstname} {middle} {lastname}".lower())
                # Add "Lastname, Firstname M."
                variants.add(f"{lastname}, {firstname} {middle}".lower())
                # Add with full middle name if it's an initial (H. → H)
                if middle.endswith('.'):
                    middle_initial = middle.rstrip('.')
                    variants.add(f"{firstname} {middle_initial} {lastname}".lower())
                    variants.add(f"{lastname}, {firstname} {middle_initial}".lower())
    else:
        # Handle "Firstname Middlename Lastname" format
        parts = name.split()
        if len(parts) >= 2:
            firstname = parts[0]
            lastname = parts[-1]

            # Add "Firstname Lastname"
            variants.add(f"{firstname} {lastname}".lower())
            # Add "Lastname, Firstname"
            variants.add(f"{lastname}, {firstname}".lower())
            # Add full name
            variants.add(name.lower())

            # If there's a middle name (e.g., "Thomas Hongjie Zhang")
            if len(parts) == 3:
                middlename = parts[1]
                # Add "Firstname M. Lastname" (middle initial variant)
                middle_initial = middlename[0]
                variants.add(f"{firstname} {middle_initial} {lastname}".lower())
                variants.add(f"{firstname} {middle_initial}. {lastname}".lower())
                variants.add(f"{lastname}, {firstname} {middle_initial}".lower())
                variants.add(f"{lastname}, {firstname} {middle_initial}.".lower())

    return variants


def extract_author_names(author_string: str) -> List[str]:
    """
    Extract individual author names from BibTeX author field.
    Handles "Author1 and Author2 and Author3" format.
    """
    # Split by " and "
    authors = re.split(r'\s+and\s+', author_string, flags=re.IGNORECASE)
    return [author.strip() for author in authors]


def match_member_to_publications(member_name: str, publications: List[Dict]) -> List[Dict]:
    """
    Find all publications where the member is an author.
    Returns matched publications sorted by year (most recent first).
    """
    member_variants = normalize_name(member_name)
    matched_pubs = []

    for pub in publications:
        if 'authors' not in pub:
            continue

        # Extract all authors from the publication
        pub_authors = extract_author_names(pub['authors'])

        # Check if any author matches the member
        for author in pub_authors:
            author_variants = normalize_name(author)
            if member_variants & author_variants:  # Set intersection
                matched_pubs.append(pub)
                break  # Don't add the same pub multiple times

    # Sort by year, most recent first
    matched_pubs.sort(key=lambda x: x.get('year', 0), reverse=True)

    return matched_pubs


def clean_latex_escapes(text: str) -> str:
    r"""
    Remove LaTeX escape sequences from text for HTML display.

    Common LaTeX escapes:
    - \& → &
    - \% → %
    - \$ → $
    - \# → #
    - \_ → _
    - \{ → {
    - \} → }
    """
    replacements = {
        r'\&': '&',
        r'\%': '%',
        r'\$': '$',
        r'\#': '#',
        r'\_': '_',
        r'\{': '{',
        r'\}': '}',
        r'\~': '~',
        r'\^': '^',
    }

    for latex, html in replacements.items():
        text = text.replace(latex, html)

    return text


def format_publication_for_yaml(pub: Dict) -> Dict:
    """
    Format publication dict for YAML output.
    Includes: title, journal, year, doi/html, pdf, replication
    Cleans LaTeX escape sequences for HTML display.
    """
    yaml_pub = {'title': clean_latex_escapes(pub.get('title', ''))}

    if 'journal' in pub:
        yaml_pub['journal'] = clean_latex_escapes(pub['journal'])

    if 'year' in pub:
        yaml_pub['year'] = pub['year']

    # Prefer html over doi
    if 'html' in pub:
        yaml_pub['html'] = pub['html']
    elif 'doi' in pub:
        yaml_pub['doi'] = pub['doi']

    # Add PDF link if available
    if 'pdf' in pub:
        yaml_pub['pdf'] = pub['pdf']

    # Add replication link if available
    if 'replication' in pub:
        yaml_pub['replication'] = pub['replication']

    return yaml_pub


def update_members_file(members_path: Path, bib_path: Path):
    """
    Main function to update members.yml with matched publications.
    """
    print(f"Reading bibliography from: {bib_path}")
    publications = parse_bibtex_file(bib_path)
    print(f"Found {len(publications)} publications in bibliography")

    print(f"\nReading members from: {members_path}")
    with open(members_path, 'r', encoding='utf-8') as f:
        members_data = yaml.safe_load(f)

    # Process each member category
    for category in ['graduate_students', 'undergraduate_students', 'alumni']:
        if category not in members_data:
            continue

        print(f"\nProcessing {category}:")
        for member in members_data[category]:
            member_name = member.get('name', '')

            # Match publications
            matched_pubs = match_member_to_publications(member_name, publications)

            # Format for YAML
            if matched_pubs:
                member['publications'] = [
                    format_publication_for_yaml(pub) for pub in matched_pubs
                ]
                print(f"  {member_name}: {len(matched_pubs)} publications")
            else:
                # Remove publications key if no matches
                if 'publications' in member:
                    del member['publications']
                print(f"  {member_name}: 0 publications")

    # Write updated members.yml
    print(f"\nWriting updated members to: {members_path}")
    with open(members_path, 'w', encoding='utf-8') as f:
        yaml.dump(members_data, f,
                  default_flow_style=False,
                  allow_unicode=True,
                  sort_keys=False,
                  width=120)

    print("\n✓ Successfully updated members.yml with publications from papers.bib")


if __name__ == '__main__':
    # Paths
    repo_root = Path(__file__).parent.parent
    members_path = repo_root / '_data' / 'members.yml'
    bib_path = repo_root / '_bibliography' / 'papers.bib'

    # Validate paths
    if not members_path.exists():
        print(f"Error: members.yml not found at {members_path}")
        exit(1)

    if not bib_path.exists():
        print(f"Error: papers.bib not found at {bib_path}")
        exit(1)

    # Run update
    update_members_file(members_path, bib_path)
