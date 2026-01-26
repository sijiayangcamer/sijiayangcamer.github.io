#!/usr/bin/env python3
"""
Generate detailed comparison report between BibTeX and Zotero RIS files.
"""

import re

def parse_bibtex(file_path):
    """Parse BibTeX file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = {}
    pattern = r'@(\w+)\{([^,]+),\s*\n(.*?)\n\}'

    for match in re.finditer(pattern, content, re.DOTALL):
        entry_type = match.group(1)
        key = match.group(2)
        entry_content = match.group(3)

        fields = {}
        field_pattern = r'(\w+)\s*=\s*\{([^}]+)\}'
        for field_match in re.finditer(field_pattern, entry_content):
            field_name = field_match.group(1)
            field_value = field_match.group(2)
            fields[field_name] = field_value

        entries[key] = {
            'type': entry_type,
            'fields': fields
        }

    return entries

def parse_ris(file_path):
    """Parse RIS file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = []
    current_entry = {}

    for line in content.split('\n'):
        line = line.strip()
        if not line:
            continue

        if line.startswith('TY  -'):
            if current_entry:
                entries.append(current_entry)
            current_entry = {'type': line.split('-')[1].strip()}
        elif line.startswith('ER  -'):
            if current_entry:
                entries.append(current_entry)
            current_entry = {}
        elif '  - ' in line:
            tag = line[:2]
            value = line.split('  - ', 1)[1].strip()

            if tag == 'TI':
                current_entry['title'] = value
            elif tag == 'AU':
                if 'authors' not in current_entry:
                    current_entry['authors'] = []
                current_entry['authors'].append(value)
            elif tag == 'PY':
                current_entry['year'] = value.split('/')[0]
            elif tag == 'DO':
                current_entry['doi'] = value
            elif tag == 'T2' or tag == 'JO':
                current_entry['journal'] = value
            elif tag == 'VL':
                current_entry['volume'] = value
            elif tag == 'IS':
                current_entry['issue'] = value
            elif tag == 'SP':
                current_entry['start_page'] = value
            elif tag == 'EP':
                current_entry['end_page'] = value

    return entries

def normalize_title(title):
    """Normalize title for comparison."""
    if not title:
        return ""
    title = re.sub(r'[^\w\s]', '', title.lower())
    title = re.sub(r'\s+', ' ', title).strip()
    return title

def match_entries(bibtex_entries, ris_entries):
    """Match BibTeX entries with RIS entries."""
    matches = []

    for bib_key, bib_entry in bibtex_entries.items():
        bib_title = bib_entry['fields'].get('title', '')
        bib_doi = bib_entry['fields'].get('doi', '')

        bib_title_norm = normalize_title(bib_title)

        best_match = None
        best_score = 0

        for ris_entry in ris_entries:
            ris_title_norm = normalize_title(ris_entry.get('title', ''))

            # Match by DOI
            if bib_doi and ris_entry.get('doi') == bib_doi:
                best_match = ris_entry
                best_score = 100
                break

            # Match by title similarity
            if bib_title_norm and ris_title_norm:
                bib_words = set(bib_title_norm.split())
                ris_words = set(ris_title_norm.split())

                if len(bib_words) > 0:
                    overlap = len(bib_words & ris_words)
                    score = overlap / len(bib_words) * 100

                    if score > best_score and score > 70:
                        best_score = score
                        best_match = ris_entry

        if best_match:
            matches.append((bib_key, bib_entry, best_match))

    return matches

def compare_entries(bib_key, bib_entry, ris_entry):
    """Compare a matched pair and return discrepancies."""
    discrepancies = []

    # Compare year
    bib_year = bib_entry['fields'].get('year', '')
    ris_year = ris_entry.get('year', '')
    if bib_year and ris_year and bib_year != ris_year:
        discrepancies.append({
            'field': 'year',
            'severity': 'critical',
            'bibtex': bib_year,
            'zotero': ris_year
        })

    # Compare authors count
    bib_author = bib_entry['fields'].get('author', '')
    ris_authors = ris_entry.get('authors', [])

    if bib_author and ris_authors:
        bib_author_list = [a.strip() for a in bib_author.split(' and ')]

        if len(bib_author_list) != len(ris_authors):
            discrepancies.append({
                'field': 'author_count',
                'severity': 'critical',
                'bibtex': f"{len(bib_author_list)} authors",
                'zotero': f"{len(ris_authors)} authors",
                'bib_authors': '; '.join(bib_author_list),
                'ris_authors': '; '.join(ris_authors)
            })

    # Compare title
    bib_title = bib_entry['fields'].get('title', '')
    ris_title = ris_entry.get('title', '')
    if bib_title and ris_title:
        if normalize_title(bib_title) != normalize_title(ris_title):
            # Significant difference
            if len(bib_title) < len(ris_title) * 0.8 or len(bib_title) > len(ris_title) * 1.2:
                discrepancies.append({
                    'field': 'title',
                    'severity': 'high',
                    'bibtex': bib_title,
                    'zotero': ris_title
                })

    # Compare volume/issue
    ris_volume = ris_entry.get('volume', '')
    ris_issue = ris_entry.get('issue', '')
    bib_volume = bib_entry['fields'].get('volume', '')
    bib_number = bib_entry['fields'].get('number', '')

    if ris_volume and not bib_volume:
        discrepancies.append({
            'field': 'volume',
            'severity': 'medium',
            'bibtex': 'MISSING',
            'zotero': ris_volume
        })

    if ris_issue and not bib_number:
        discrepancies.append({
            'field': 'issue/number',
            'severity': 'medium',
            'bibtex': 'MISSING',
            'zotero': ris_issue
        })

    return discrepancies

# Main execution
print("Parsing BibTeX file...")
bibtex_entries = parse_bibtex('/Users/sijiayang/Documents/sijiayangcamer.github.io/_bibliography/papers.bib')
print(f"Found {len(bibtex_entries)} BibTeX entries")

print("\nParsing Zotero RIS file...")
ris_entries = parse_ris('/Users/sijiayang/Documents/yang_zotero/yang_zotero.ris')
print(f"Found {len(ris_entries)} Zotero entries")

print("\nMatching entries...")
matches = match_entries(bibtex_entries, ris_entries)
print(f"Matched {len(matches)} entries")

print("\nComparing entries...")
all_discrepancies = {}

for bib_key, bib_entry, ris_entry in matches:
    discreps = compare_entries(bib_key, bib_entry, ris_entry)
    if discreps:
        all_discrepancies[bib_key] = discreps

print(f"\nFound {len(all_discrepancies)} entries with discrepancies\n")

# Generate report
report = []
report.append("="*80)
report.append("DETAILED BIBTEX vs ZOTERO COMPARISON REPORT")
report.append("="*80)
report.append("")

report.append(f"Total BibTeX entries: {len(bibtex_entries)}")
report.append(f"Total Zotero entries: {len(ris_entries)}")
report.append(f"Matched entries: {len(matches)}")
report.append(f"Entries with discrepancies: {len(all_discrepancies)}")
report.append("")

# Group by severity
critical = []
high = []
medium = []

for key, discreps in sorted(all_discrepancies.items()):
    severities = [d.get('severity', 'low') for d in discreps]

    if 'critical' in severities:
        critical.append((key, discreps))
    elif 'high' in severities:
        high.append((key, discreps))
    else:
        medium.append((key, discreps))

# Write critical issues
if critical:
    report.append("="*80)
    report.append(f"CRITICAL ISSUES - {len(critical)} ENTRIES")
    report.append("(Wrong years, missing/wrong authors, etc.)")
    report.append("="*80)
    report.append("")

    for key, discreps in critical:
        report.append(f"Entry: {key}")
        report.append("-" * 40)
        for d in discreps:
            report.append(f"  Field: {d['field'].upper()}")
            report.append(f"  BibTeX: {d['bibtex']}")
            report.append(f"  Zotero: {d['zotero']}")
            if 'bib_authors' in d:
                report.append(f"  BibTeX authors: {d['bib_authors']}")
                report.append(f"  Zotero authors: {d['ris_authors']}")
            report.append("")
        report.append("")

# Write high priority issues
if high:
    report.append("="*80)
    report.append(f"HIGH PRIORITY ISSUES - {len(high)} ENTRIES")
    report.append("(Title differences)")
    report.append("="*80)
    report.append("")

    for key, discreps in high:
        report.append(f"Entry: {key}")
        report.append("-" * 40)
        for d in discreps:
            report.append(f"  Field: {d['field'].upper()}")
            report.append(f"  BibTeX: {d['bibtex'][:150]}...")
            report.append(f"  Zotero: {d['zotero'][:150]}...")
            report.append("")
        report.append("")

# Write medium issues
if medium:
    report.append("="*80)
    report.append(f"MEDIUM PRIORITY ISSUES - {len(medium)} ENTRIES")
    report.append("(Missing volume/issue numbers)")
    report.append("="*80)
    report.append("")

    for key, discreps in medium:
        report.append(f"Entry: {key}")
        report.append("-" * 40)
        for d in discreps:
            report.append(f"  Field: {d['field'].upper()}")
            report.append(f"  BibTeX: {d['bibtex']}")
            report.append(f"  Zotero: {d['zotero']}")
            report.append("")
        report.append("")

# Print report
report_text = '\n'.join(report)
print(report_text)

# Save to file
with open('/tmp/zotero_bibtex_detailed_comparison.txt', 'w', encoding='utf-8') as f:
    f.write(report_text)

print("\n" + "="*80)
print(f"Report saved to: /tmp/zotero_bibtex_detailed_comparison.txt")
print("="*80)
