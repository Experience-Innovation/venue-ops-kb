#!/usr/bin/env python3
"""
DELTA-004 Bibliographic Enrichment Script
Session 18 — CI / Enrichment Cycle

Adds author and publication fields to source notes where inferable
from filename, description, and URL. Leaves null where ambiguous.

Hard Rule #1: NEVER fabricate. Leave null if not confidently inferable.
"""

import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

SOURCES_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("06_Sources")

# Known organization mappings from filename prefixes
ORG_MAP = {
    "CISA": "Cybersecurity and Infrastructure Security Agency (CISA)",
    "NFPA": "National Fire Protection Association (NFPA)",
    "IAVM": "International Association of Venue Managers (IAVM)",
    "ASIS": "ASIS International",
    "GCMA": "Global Crowd Management Alliance (GCMA)",
    "NCS4": "National Center for Spectator Sports Safety and Security (NCS4)",
    "OSHA": "Occupational Safety and Health Administration (OSHA)",
    "FEMA": "Federal Emergency Management Agency (FEMA)",
    "DHS": "Department of Homeland Security (DHS)",
    "NIH": "National Institutes of Health (NIH)",
    "RAND": "RAND Corporation",
    "FDA": "U.S. Food and Drug Administration (FDA)",
    "SFCR": "Government of Canada",
    "DOL": "U.S. Department of Labor",
    "FSMA": "U.S. Food and Drug Administration (FDA)",
    "EPA": "U.S. Environmental Protection Agency (EPA)",
    "DOE": "U.S. Department of Energy (DOE)",
    "ICC": "International Code Council (ICC)",
    "ASHRAE": "ASHRAE",
    "USGBC": "U.S. Green Building Council (USGBC)",
    "ADA": "U.S. Department of Justice",
    "AVIXA": "AVIXA",
    "SMPTE": "Society of Motion Picture and Television Engineers (SMPTE)",
    "AES": "Audio Engineering Society (AES)",
    "IEEE": "Institute of Electrical and Electronics Engineers (IEEE)",
    "PCMA": "Professional Convention Management Association (PCMA)",
    "AIPC": "International Association of Convention Centres (AIPC)",
    "UFI": "UFI — The Global Association of the Exhibition Industry",
    "NPA": "National Parking Association (NPA)",
    "IPI": "International Parking & Mobility Institute (IPI)",
    "LEED": "U.S. Green Building Council (USGBC)",
    "GBCI": "Green Business Certification Inc. (GBCI)",
    "IIAR": "International Institute of Ammonia Refrigeration (IIAR)",
    "ASTM": "ASTM International",
    "ISSA": "International Sanitary Supply Association (ISSA)",
    "NRA": "National Restaurant Association",
    "ServSafe": "National Restaurant Association",
    "GCCA": "Global Cold Chain Alliance (GCCA)",
    "IFMA": "International Facility Management Association (IFMA)",
    "BOMA": "Building Owners and Managers Association (BOMA)",
    "Baldrige": "Baldrige Foundation",
    "EFQM": "European Foundation for Quality Management (EFQM)",
    "Excellence-Canada": "Excellence Canada",
    "TEAM-Coalition": "TEAM Coalition",
    "UNITE-HERE": "UNITE HERE",
    "FLSA": "U.S. Department of Labor",
    "USC": "U.S. Congress",
    "Fruin": "John J. Fruin",
}

# URL domain to publication mapping
DOMAIN_PUB = {
    "nfpa.org": "NFPA",
    "iavm.org": "IAVM",
    "osha.gov": "OSHA",
    "fema.gov": "FEMA",
    "cisa.gov": "CISA",
    "epa.gov": "EPA",
    "energy.gov": "DOE",
    "fda.gov": "FDA",
    "dol.gov": "U.S. Department of Labor",
    "ada.gov": "U.S. Department of Justice",
    "ncbi.nlm.nih.gov": "NIH / StatPearls",
    "rand.org": "RAND Corporation",
    "usgbc.org": "U.S. Green Building Council",
    "ashrae.org": "ASHRAE",
    "avixa.org": "AVIXA",
    "pcma.org": "PCMA",
    "canada.ca": "Government of Canada",
    "gc.ca": "Government of Canada",
    "gov.bc.ca": "Government of British Columbia",
    "ontario.ca": "Government of Ontario",
    "alberta.ca": "Government of Alberta",
    "prnewswire.com": "PR Newswire",
    "bloomberg.com": "Bloomberg",
    "nytimes.com": "The New York Times",
    "wsj.com": "The Wall Street Journal",
    "bbc.com": "BBC",
    "cbc.ca": "CBC",
    "forbes.com": "Forbes",
    "reuters.com": "Reuters",
}


def extract_org_from_filename(filename):
    """Extract organization abbreviation from Source-NNNN-{Org}-{Description}.md"""
    # Remove Source-NNNN- prefix and .md suffix
    name = re.sub(r'^Source-\d{4}-', '', filename)
    name = name.replace('.md', '')

    # Split by hyphens and check first 1-3 segments against ORG_MAP
    parts = name.split('-')

    # Try progressively longer prefixes
    for length in [1, 2, 3]:
        if length <= len(parts):
            candidate = '-'.join(parts[:length])
            if candidate in ORG_MAP:
                return ORG_MAP[candidate]

    return None


def extract_pub_from_url(url):
    """Extract publication from URL domain."""
    try:
        parsed = urlparse(url.strip('"').strip("'"))
        domain = parsed.netloc.lower()
        # Remove www. prefix
        domain = re.sub(r'^www\.', '', domain)

        # Check against domain map
        for pattern, pub in DOMAIN_PUB.items():
            if pattern in domain:
                return pub

        return None
    except:
        return None


def extract_author_from_description(desc, source_type):
    """Try to extract author from description text based on source_type."""
    desc = desc.strip('"').strip("'")

    # Common patterns: "Organization Name's guide/report/analysis/overview..."
    # or "Description of the Organization Name document..."

    # For vendor-documentation, look for company names at the start
    if source_type == "vendor-documentation":
        # Pattern: "CompanyName overview/analysis/platform/guide..."
        match = re.match(r'^([A-Z][A-Za-z0-9 &\-\.]+?)\s+(?:overview|analysis|platform|guide|solution|whitepaper|report|documentation|AI|product)', desc)
        if match:
            return match.group(1).strip()

    # For regulatory-document, look for agency abbreviations
    if source_type == "regulatory-document":
        # Check for known abbreviations at start of description
        for abbr, full in ORG_MAP.items():
            if desc.upper().startswith(abbr.upper() + " ") or desc.upper().startswith(abbr.upper() + "'"):
                return full
        # Pattern: "X guide/code/standard/regulation..."
        match = re.match(r'^([A-Z][A-Za-z0-9 &\-\.]+?)\s+(?:guide|code|standard|regulation|act|rule|requirement|bulletin|manual|circular|directive)', desc, re.IGNORECASE)
        if match:
            candidate = match.group(1).strip()
            if len(candidate) > 3 and len(candidate) < 80:
                return candidate

    return None


def process_file(filepath):
    """Process a single source note file."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Skip if already has author field
    if re.search(r'^author:', content, re.MULTILINE):
        return False, "already has author"

    # Extract frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return False, "no frontmatter"

    frontmatter = fm_match.group(1)

    # Extract fields
    source_type_match = re.search(r'^source_type:\s*(.+)$', frontmatter, re.MULTILINE)
    desc_match = re.search(r'^description:\s*(.+)$', frontmatter, re.MULTILINE)
    url_match = re.search(r'^url:\s*(.+)$', frontmatter, re.MULTILINE)

    if not source_type_match or not desc_match:
        return False, "missing required fields"

    source_type = source_type_match.group(1).strip().strip('"').strip("'")
    description = desc_match.group(1).strip()
    url = url_match.group(1).strip() if url_match else ""

    filename = os.path.basename(filepath)

    # Attempt author extraction (in priority order)
    author = extract_org_from_filename(filename)
    if not author:
        author = extract_author_from_description(description, source_type)

    # Attempt publication extraction
    publication = extract_pub_from_url(url)

    # If we have at least author OR publication, add them
    if author or publication:
        # Build the new fields to insert after description line
        new_fields = ""
        if author:
            new_fields += f'author: "{author}"\n'
        if publication:
            new_fields += f'publication: "{publication}"\n'

        # Insert after the description line in frontmatter
        desc_line = desc_match.group(0)
        new_content = content.replace(desc_line, desc_line + "\n" + new_fields.rstrip(), 1)

        with open(filepath, 'w') as f:
            f.write(new_content)

        return True, f"author={'Y' if author else 'N'} pub={'Y' if publication else 'N'}"

    return False, "could not infer"


def main():
    sources_dir = SOURCES_DIR
    if not sources_dir.exists():
        print(f"ERROR: {sources_dir} not found")
        sys.exit(1)

    files = sorted(sources_dir.glob("Source-*.md"))
    print(f"Processing {len(files)} source notes...")

    enriched = 0
    skipped = 0
    failed = 0

    by_type = {}

    for f in files:
        success, reason = process_file(f)
        if success:
            enriched += 1
        elif "already" in reason:
            skipped += 1
        else:
            failed += 1

        # Track by reason
        by_type[reason] = by_type.get(reason, 0) + 1

    print(f"\nResults:")
    print(f"  Enriched: {enriched}")
    print(f"  Skipped (already has author): {skipped}")
    print(f"  Could not infer: {failed}")
    print(f"\nBreakdown:")
    for reason, count in sorted(by_type.items(), key=lambda x: -x[1]):
        print(f"  {reason}: {count}")


if __name__ == "__main__":
    main()
