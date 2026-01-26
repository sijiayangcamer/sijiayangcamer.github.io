#!/usr/bin/env python3
"""
Systematically verify BibTeX entries against PDFs.
"""

import re
import PyPDF2
import os
from pathlib import Path

BIB_FILE = "/Users/sijiayang/Documents/sijiayangcamer.github.io/_bibliography/papers.bib"
PDF_DIR = "/Users/sijiayang/Documents/sijiayangcamer.github.io/assets/pdf"
OUTPUT_REPORT = "/tmp/verification_report.txt"

def parse_bib_file(bib_path):
    """Parse BibTeX file and extract all entries."""
    with open(bib_path, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = []
    entry_pattern = r'@(\w+)\{([^,]+),\s*\n(.*?)\n\}'

    for match in re.finditer(entry_pattern, content, re.DOTALL):
        entry_type = match.group(1)
        key = match.group(2)
        entry_content = match.group(3)

        # Extract fields
        fields = {}
        field_pattern = r'(\w+)\s*=\s*\{([^}]+)\}'
        for field_match in re.finditer(field_pattern, entry_content):
            field_name = field_match.group(1)
            field_value = field_match.group(2)
            fields[field_name] = field_value

        entries.append({
            'type': entry_type,
            'key': key,
            'fields': fields
        })

    return entries

def extract_first_page_text(pdf_path, max_chars=4000):
    """Extract text from first page of PDF."""
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            if len(reader.pages) > 0:
                text = reader.pages[0].extract_text()
                return text[:max_chars]  # Limit to first 4000 chars
    except Exception as e:
        return f"ERROR: {str(e)}"
    return ""

def main():
    print("Verifying BibTeX entries against PDFs...")
    print("="*80)

    entries = parse_bib_file(BIB_FILE)

    report = []
    report.append("="*80)
    report.append("BIBTEX VERIFICATION REPORT")
    report.append("="*80)
    report.append("")

    for entry in entries:
        if 'pdf' not in entry['fields']:
            continue

        pdf_file = os.path.join(PDF_DIR, entry['fields']['pdf'])
        if not os.path.exists(pdf_file):
            report.append(f"\n{entry['key']}: PDF FILE NOT FOUND")
            continue

        print(f"Processing {entry['key']}...")

        # Extract first page text
        pdf_text = extract_first_page_text(pdf_file)

        report.append(f"\n{'='*80}")
        report.append(f"ENTRY: {entry['key']}")
        report.append(f"{'='*80}")
        report.append(f"\nCURRENT BIB INFO:")
        report.append(f"  Title: {entry['fields'].get('title', 'N/A')}")
        report.append(f"  Authors: {entry['fields'].get('author', 'N/A')}")
        report.append(f"  Journal: {entry['fields'].get('journal') or entry['fields'].get('booktitle', 'N/A')}")
        report.append(f"  Year: {entry['fields'].get('year', 'N/A')}")
        report.append(f"  DOI: {entry['fields'].get('doi', 'N/A')}")
        report.append(f"  Corresponding: {entry['fields'].get('corresponding', 'N/A')}")
        report.append(f"  Note: {entry['fields'].get('note', 'N/A')}")
        report.append(f"\nFIRST PAGE TEXT FROM PDF:")
        report.append(f"{pdf_text[:2000]}")  # First 2000 chars
        report.append("")

    # Write report
    with open(OUTPUT_REPORT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))

    print(f"\nVerification report generated: {OUTPUT_REPORT}")
    print("="*80)

if __name__ == '__main__':
    main()
