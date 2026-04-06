#!/usr/bin/env python3
"""
DELTA-004 Bibliographic Enrichment — Pass 2
Expanded org/company mappings for remaining 152 unenriched source notes.
"""

import os
import re
import sys
from pathlib import Path

SOURCES_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("06_Sources")

# Expanded filename-prefix to author mapping
ORG_MAP = {
    # Government/Regulatory
    "CISA": "Cybersecurity and Infrastructure Security Agency (CISA)",
    "NFPA": "National Fire Protection Association (NFPA)",
    "OSHA": "Occupational Safety and Health Administration (OSHA)",
    "FEMA": "Federal Emergency Management Agency (FEMA)",
    "DHS": "Department of Homeland Security (DHS)",
    "FDA": "U.S. Food and Drug Administration (FDA)",
    "EPA": "U.S. Environmental Protection Agency (EPA)",
    "DOE": "U.S. Department of Energy (DOE)",
    "DOL": "U.S. Department of Labor",
    "DOJ": "U.S. Department of Justice",
    "FHWA": "Federal Highway Administration (FHWA)",
    "NIST": "National Institute of Standards and Technology (NIST)",
    "NWS": "National Weather Service (NWS)",
    "NOAA": "National Oceanic and Atmospheric Administration (NOAA)",
    "NIH": "National Institutes of Health (NIH)",
    "CFIA": "Canadian Food Inspection Agency (CFIA)",
    "CRTC": "Canadian Radio-television and Telecommunications Commission (CRTC)",
    "ICS-Canada": "Incident Command System Canada",
    "Ontario-Naloxone": "Government of Ontario",
    "Alberta-OIPC": "Office of the Information and Privacy Commissioner of Alberta",
    "NAIC": "National Association of Insurance Commissioners (NAIC)",
    "US-Treasury": "U.S. Department of the Treasury",
    "CAN-SPAM": "Federal Trade Commission (FTC)",
    "FirstNet": "First Responder Network Authority (FirstNet)",

    # Standards/Certification Bodies
    "ISO": "International Organization for Standardization (ISO)",
    "ANSI": "American National Standards Institute (ANSI)",
    "ASTM": "ASTM International",
    "ICC": "International Code Council (ICC)",
    "ASHRAE": "ASHRAE",
    "WELL": "International WELL Building Institute (IWBI)",
    "ILFI": "International Living Future Institute (ILFI)",
    "GBAC": "Global Biorisk Advisory Council (GBAC)",
    "SQF": "Safe Quality Food Institute (SQF)",
    "GFSI": "Global Food Safety Initiative (GFSI)",
    "TRUE": "Green Business Certification Inc. (GBCI)",
    "ETCP": "Entertainment Technician Certification Program (ETCP)",
    "ENERGY-STAR": "U.S. Environmental Protection Agency (EPA)",
    "Green-Globes": "Green Building Initiative (GBI)",
    "LEED": "U.S. Green Building Council (USGBC)",
    "IES": "Illuminating Engineering Society (IES)",
    "ISA": "International Sign Association (ISA)",

    # Trade Associations
    "IAVM": "International Association of Venue Managers (IAVM)",
    "AVIXA": "AVIXA",
    "PCMA": "Professional Convention Management Association (PCMA)",
    "AIPC": "International Association of Convention Centres (AIPC)",
    "UFI": "UFI — The Global Association of the Exhibition Industry",
    "ASIS": "ASIS International",
    "GCMA": "Global Crowd Management Alliance (GCMA)",
    "NCS4": "National Center for Spectator Sports Safety and Security (NCS4)",
    "NPA": "National Parking Association (NPA)",
    "IPI": "International Parking & Mobility Institute (IPI)",
    "ISSA": "International Sanitary Supply Association (ISSA)",
    "NRA": "National Restaurant Association",
    "ServSafe": "National Restaurant Association",
    "GCCA": "Global Cold Chain Alliance (GCCA)",
    "IFMA": "International Facility Management Association (IFMA)",
    "BOMA": "Building Owners and Managers Association (BOMA)",
    "ACF": "American Culinary Federation (ACF)",
    "AIMS": "Association of Amusement Parks and Attractions / AIMS International",
    "ALSD": "Association of Luxury Suite Directors (ALSD)",
    "BMI": "Broadcast Music, Inc. (BMI)",
    "SESAC": "SESAC (Society of European Stage Authors and Composers)",
    "ESTA": "Entertainment Services and Technology Association (ESTA)",
    "ESCA": "Exhibition Services & Contractors Association (ESCA)",
    "IAFE": "International Association of Fairs and Expositions (IAFE)",
    "IATSE": "International Alliance of Theatrical Stage Employees (IATSE)",
    "IBCCES": "International Board of Credentialing and Continuing Education Standards (IBCCES)",
    "NAFEM": "North American Association of Food Equipment Manufacturers (NAFEM)",
    "SMPTE": "Society of Motion Picture and Television Engineers (SMPTE)",
    "AES": "Audio Engineering Society (AES)",
    "IEEE": "Institute of Electrical and Electronics Engineers (IEEE)",
    "USITT": "United States Institute for Theatre Technology (USITT)",
    "TEAM-Coalition": "TEAM Coalition",
    "UNITE-HERE": "UNITE HERE",
    "MEIEA": "Music & Entertainment Industry Educators Association (MEIEA)",
    "IIAR": "International Institute of Ammonia Refrigeration (IIAR)",
    "SDVoE": "SDVoE Alliance",
    "Green-Sports": "Green Sports Alliance",
    "Green-Restaurant": "Green Restaurant Association",
    "Net-Zero-Carbon": "Joint Meetings Industry Council",
    "Events-Industry": "Events Industry Council (EIC)",
    "Baldrige": "Baldrige Foundation",
    "EFQM": "European Foundation for Quality Management (EFQM)",
    "Excellence-Canada": "Excellence Canada",
    "Shingo": "Shingo Institute",
    "Deming": "Japanese Union of Scientists and Engineers (JUSE)",
    "Alliance-Performance": "Alliance for Performance Excellence",
    "EACA": "Exhibition and Arena Contractors Association",
    "World-Travel": "World Travel Awards",
    "World-Stadiums": "World Stadiums Awards",
    "III": "Insurance Information Institute (III)",
    "KultureCity": "KultureCity",

    # Venue Operators/Companies
    "Aramark": "Aramark Corporation",
    "Delaware-North": "Delaware North Companies",
    "Sodexo": "Sodexo Live!",
    "Levy": "Levy Restaurants (Compass Group)",
    "Legends": "Legends Hospitality",
    "OVG": "Oak View Group (OVG)",
    "Freeman": "Freeman Company",
    "GES": "GES (Global Experience Specialists)",
    "Honeywell": "Honeywell International",
    "Siemens": "Siemens AG",
    "IBM": "IBM Corporation",
    "Momentus": "Momentus Technologies",
    "Autodesk": "Autodesk, Inc.",
    "Salesforce": "Salesforce, Inc.",
    "Zebra": "Zebra Technologies",
    "ParkMobile": "ParkMobile",
    "Avidbots": "Avidbots Corp.",
    "EcoStruxure": "Schneider Electric",
    "Leanpath": "Leanpath, Inc.",
    "YinzCam": "YinzCam, Inc.",
    "Voyage-Control": "Voyage Control",
    "WeTrack": "WeTrack",
    "Audinate": "Audinate (Dante)",
    "Thor-Broadcast": "Thor Broadcast",
    "Listen-Technologies": "Listen Technologies",
    "REALice": "REALice",
    "Events2HVAC": "Events2HVAC",
    "Prism-FM": "Prism FM",
    "FoodLogiQ": "FoodLogiQ (Aptean)",
    "247-Software": "24/7 Software",
    "247Software": "24/7 Software",
    "ALICE-Training": "Alert, Lockdown, Inform, Counter, Evacuate (ALICE) Training Institute",
    "Hussey": "Hussey Seating Company",
    "Xtract-One": "Xtract One Technologies",
    "IntelliSee": "IntelliSee",
    "Convergint": "Convergint Technologies",

    # Publications/Media
    "TicketFairy": "TicketFairy",
    "Pollstar": "Pollstar",
    "VenuesNow": "VenuesNow",
    "BizBash": "BizBash",
    "BusinessWire": "Business Wire",
    "SBJ": "Sports Business Journal",
    "Forbes": "Forbes Travel Guide",
    "Sports-Video": "Sports Video Group (SVG)",
    "Sports-Hospitality": "Sports Hospitality Market Analysis",
    "Sports-Venue": "Sports Venue Business",
    "TheStadiumBusiness": "TheStadiumBusiness",
    "Data-Center": "Data Center Knowledge",
    "Globe-Mail": "The Globe and Mail",
    "Fisher-Phillips": "Fisher Phillips LLP",
    "Zen-Legal": "ZenBusiness / Legal Analysis",

    # Universities/Research
    "RAND": "RAND Corporation",
    "Penn-State": "Penn State University",
    "Northeastern": "Northeastern University",
    "Fruin": "John J. Fruin",

    # Specific Venues/Programs
    "Kennedy-Center": "John F. Kennedy Center for the Performing Arts",
    "Climate-Pledge": "Climate Pledge Arena / Amazon",
    "MGM": "MGM Resorts International",
    "Ritz-Carlton": "The Ritz-Carlton Leadership Center",
    "Allegiant": "Allegiant Stadium",
    "MTCC": "Metro Toronto Convention Centre (MTCC)",
    "RBC-Convention": "RBC Convention Centre Winnipeg",
    "Hawaii-CC": "Hawaii Convention Center",
    "CaGBC-VCC": "Canada Green Building Council / Vancouver Convention Centre",
    "Second-Harvest": "Second Harvest",
    "Menus-of-Change": "Culinary Institute of America (CIA)",
    "Kigali": "United Nations Environment Programme (UNEP)",
    "Carnival": "Carnival / Exhibition Industry",
    "NHL": "National Hockey League (NHL)",

    # Named resources
    "AAA-Diamond": "AAA (American Automobile Association)",
    "JD-Power": "J.D. Power",
    "New-Gold-Standard": "Joseph A. Michelli",
    "Quarterdeck": "Disney Institute / Quarterdeck",
    "Sprintzeal": "Sprintzeal (educational content)",
    "Sweetstudy": "SweetStudy (educational content)",
    "Thunderbird": "Thunderbird School of Global Management",
    "Reliable-Plant": "Reliable Plant",
    "Tim-Review": "Technology Innovation Management Review",
    "Unleash": "UNLEASH",
    "ZipRecruiter": "ZipRecruiter",
    "Young-Centre": "Young Centre for the Performing Arts",
    "Get-Into-Theatre": "Get Into Theatre",
    "TicketPeak": "TicketPeak",
    "Stadium-Wayfinding": "Stadium Wayfinding Guide",
    "Canada-Employment": "Government of Canada",

    # Research-specific
    "Qualtrics": "Qualtrics",
    "2010-ADA": "U.S. Department of Justice",
}


def extract_author(filename):
    """Extract author from filename using expanded mapping."""
    name = re.sub(r'^Source-\d{4}-', '', filename).replace('.md', '')

    # Try progressively longer prefixes (up to 4 segments)
    parts = name.split('-')
    for length in range(min(4, len(parts)), 0, -1):
        candidate = '-'.join(parts[:length])
        if candidate in ORG_MAP:
            return ORG_MAP[candidate]

    return None


def process_file(filepath):
    """Add author field to a source note if not already present."""
    with open(filepath, 'r') as f:
        content = f.read()

    if re.search(r'^author:', content, re.MULTILINE):
        return False, "already has author"

    filename = os.path.basename(filepath)
    author = extract_author(filename)

    if not author:
        return False, "could not infer"

    # Find description line and insert author after it
    desc_match = re.search(r'^(description:\s*.+)$', content, re.MULTILINE)
    if not desc_match:
        return False, "no description"

    desc_line = desc_match.group(0)
    new_content = content.replace(desc_line, desc_line + f'\nauthor: "{author}"', 1)

    with open(filepath, 'w') as f:
        f.write(new_content)

    return True, f"author={author[:40]}"


def main():
    sources_dir = SOURCES_DIR
    files = sorted(sources_dir.glob("Source-*.md"))

    enriched = 0
    skipped = 0
    failed = 0
    failed_files = []

    for f in files:
        success, reason = process_file(f)
        if success:
            enriched += 1
        elif "already" in reason:
            skipped += 1
        else:
            failed += 1
            failed_files.append(os.path.basename(f))

    print(f"Pass 2 Results:")
    print(f"  Enriched: {enriched}")
    print(f"  Already had author: {skipped}")
    print(f"  Could not infer: {failed}")

    if failed_files:
        print(f"\nRemaining unenriched ({failed}):")
        for fn in failed_files:
            print(f"  {fn}")


if __name__ == "__main__":
    main()
