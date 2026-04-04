# Parking, Premium Hospitality, and Venue Marketing Compliance for Large Venues (April 2026)

## Executive Overview

Large sports and entertainment venues must navigate overlapping requirements from accessibility law (ADA), building and fire codes, liquor and food regulations, anti‑spam and advertising rules, and local sign and traffic ordinances.  In North America, the core federal frameworks are the 2010 ADA Standards for Accessible Design (U.S.), CAN‑SPAM (U.S.), CASL (Canada), and the FTC Endorsement Guides, which are then layered with provincial/state rules (e.g., AGLC in Alberta) and municipal sign and traffic codes (e.g., Calgary Land Use Bylaw 1P2007 and Edmonton sign rules).  This report synthesizes key requirements as of April 2026, with emphasis on stadium/arena‑scale venues and premium hospitality areas.[^1][^2][^3][^4][^5][^6][^7][^8]

***

## 1. ADA Parking Requirements for Large Venues

### 1.1 Core scoping: minimum accessible parking counts

The 2010 ADA Standards require accessible parking for each parking facility (lot or structure) on a site, not just in aggregate.  Section 208.2 sets minimum numbers of accessible spaces based on total spaces in each facility, and at least one of every six accessible spaces (or fraction) must be van‑accessible under section 208.2.4.  The U.S. Access Board’s parking guide reproduces the core table and explicitly shows the split between standard and van spaces.[^2][^9][^10][^11]

**Minimum accessible parking (per facility – cars and vans combined)**

| Total spaces in facility | Minimum accessible spaces (car + van) | Notes |
|--------------------------|----------------------------------------|-------|
| 1–25                     | 1                                      | All can be van if desired.[^2][^11] |
| 26–50                    | 2                                      | At least 1 van space.[^2][^11] |
| 51–75                    | 3                                      | 1 van.[^2][^11] |
| 76–100                   | 4                                      | 1 van.[^2][^11] |
| 101–150                  | 5                                      | 1 van.[^2][^11] |
| 151–200                  | 6                                      | 1 van.[^2][^11] |
| 201–300                  | 7                                      | 2 vans.[^9][^11] |
| 301–400                  | 8                                      | 2 vans.[^9][^11] |
| 401–500                  | 9                                      | 2 vans.[^9][^11] |
| 501–1,000                | 2% of total                            | Van spaces = 1/6 of accessible total.[^2][^11] |
| 1,001+                   | 20 + 1 per 100 (or fraction) >1,000    | Van spaces = 1/6 of accessible total.[^2][^11] |

Venues with multiple lots and garages must calculate accessibility separately for each facility (e.g., VIP garage, staff garage, public lot A), which is particularly important for large campuses with separated parking assets.[^12][^13][^2]

### 1.2 Van‑accessible spaces and technical criteria

The ADA Standards require at least one van‑accessible space for each six accessible spaces or fraction thereof in each facility.  The Access Board’s technical guidance for section 502 clarifies that van spaces must provide extra width and vertical clearance, either via a wider space or a wider access aisle.[^10][^11][^14][^15]

Key technical points from section 502 and related guidance:

- **Width and aisle options** – Car spaces: at least 96 inches wide with a 60‑inch wide access aisle.[^14][^15]
- **Van spaces (two approaches)**:
  - 132‑inch wide van space with a 60‑inch access aisle; or
  - 96‑inch wide van space with a 96‑inch access aisle ("universal" arrangement).[^16][^15][^14]
- **Vertical clearance** – Van spaces, their access aisles, and the vehicular route serving them must provide at least 98 inches of vertical clearance.[^15][^17]
- **Location of access aisle** – Access aisles must adjoin the accessible parking space, be on the passenger side for angled van spaces, and cannot overlap the vehicular way.[^14][^15]
- **Marking and signage** – Accessible spaces must be marked and signed; DOJ technical assistance emphasizes signs mounted in front of the space and access aisles forming part of the accessible route to the entrance.[^18][^19]

### 1.3 Accessible route from parking to entrances

Section 206.2.1 of the ADA Standards requires at least one accessible route from accessible parking spaces and passenger loading zones to the accessible entrance(s) they serve.  The route must also connect site arrival points such as public sidewalks and transit stops to accessible building entrances.[^20][^21][^22]

Key requirements:

- **Shortest accessible route** – Section 208.3.1 requires accessible spaces to be located on the shortest accessible route from parking to an entrance complying with 206.4; if multiple accessible entrances are served, accessible spaces must be dispersed among them.[^23][^2]
- **Route characteristics** – Route must comply with Chapter 4 on accessible routes (width, slopes, surfaces, curb ramps, etc.), avoiding curbs without ramps or steep cross‑slopes.[^24][^20]
- **Vehicular ways** – Where a vehicular way is used by pedestrians (e.g., through a parking lot), an accessible route along that circulation path is required; exceptions for vehicular routes do not apply where pedestrians use them to access the building.[^25][^22]

### 1.4 Temporary and event‑day parking arrangements

DOJ and accessibility planners emphasize that temporary or event‑specific parking plans must still meet ADA scoping and technical requirements.  A widely used planning guide for temporary events notes that accessible parking counts must never fall below ADA minimums, at least one in six accessible spaces must be van‑accessible, and accessible spaces must remain on an accessible route to the event entrance.[^26][^23]

Practical implications for large venues:

- **Reconfigured lots on event days** – When converting general parking to VIP or media zones, the venue must maintain required numbers of accessible and van spaces in each reconfigured facility and keep them near accessible entrances.[^23][^26]
- **Overflow and remote lots** – If shuttles are used from remote parking, shuttles must be accessible (e.g., lift‑equipped), and accessible spaces must be provided both at the main venue and in shuttle‑served lots.[^26]
- **Temporary accessible spaces** – In grass fields or overflow areas, organizers can create temporary accessible spaces using cones, barricades, and pavement marking tape, ensuring level surfaces, signage, and curb ramps or portable ramps where needed.[^26]

### 1.5 ADA parking calculation formulas and code pattern

The ADA scoping can be expressed using simple formulas that can be implemented in code.

**1.5.1 Minimum accessible spaces (total) per facility**

Let \(N\) be the total number of parking spaces in a facility.

Define \(A(N)\) as the required total accessible spaces (van + standard):

- For \(1 \le N \le 25\): \(A(N) = 1\).[^2][^10]
- For \(26 \le N \le 50\): \(A(N) = 2\).
- For \(51 \le N \le 75\): \(A(N) = 3\).
- For \(76 \le N \le 100\): \(A(N) = 4\).
- For \(101 \le N \le 150\): \(A(N) = 5\).
- For \(151 \le N \le 200\): \(A(N) = 6\).
- For \(201 \le N \le 300\): \(A(N) = 7\).
- For \(301 \le N \le 400\): \(A(N) = 8\).
- For \(401 \le N \le 500\): \(A(N) = 9\).
- For \(501 \le N \le 1000\): \(A(N) = \lceil 0.02 N \rceil\).
- For \(N > 1000\): \(A(N) = 20 + \left\lceil \frac{N - 1000}{100} \right\rceil\).[^11][^10][^2]

**1.5.2 Van‑accessible spaces per facility**

Let \(V(N)\) be required van spaces:

- \(V(N) = \max\bigl(1, \lceil A(N) / 6 \rceil\bigr)\).[^13][^10][^11]

Standard accessible spaces are then \(S(N) = A(N) - V(N)\).

**1.5.3 Example Python implementation**

```python
import math

ADA_BREAKPOINTS = [
    (25, 1),
    (50, 2),
    (75, 3),
    (100, 4),
    (150, 5),
    (200, 6),
    (300, 7),
    (400, 8),
    (500, 9),
]


def ada_accessible_spaces(total_spaces: int) -> tuple[int, int, int]:
    """Return (total_accessible, van_spaces, standard_accessible)
    based on 2010 ADA Standards §208 and Access Board guidance.
    """
    if total_spaces <= 0:
        return (0, 0, 0)

    # Discrete table up to 500
    for limit, required in ADA_BREAKPOINTS:
        if total_spaces <= limit:
            accessible = required
            break
    else:
        if total_spaces <= 1000:
            accessible = math.ceil(0.02 * total_spaces)
        else:
            accessible = 20 + math.ceil((total_spaces - 1000) / 100.0)

    van = max(1, math.ceil(accessible / 6.0))
    standard = accessible - van
    return accessible, van, standard


# Example: 6,500‑space stadium campus garage
print(ada_accessible_spaces(6500))  # (150, 25, 125)
```

This pattern implements the federal minimums; state or local codes may be more stringent and must be layered on top.[^27][^23]

***

## 2. Parking Facility Safety, Lighting, and Fire/Life Safety

### 2.1 Lighting standards (IES RP‑20 / RP‑8)

The Illuminating Engineering Society’s RP‑20 (now largely integrated into ANSI/IES RP‑8) is the main reference for parking facility lighting and is frequently incorporated by municipalities by reference.  Publicly available summaries of RP‑20‑14 show recommended maintained horizontal illuminance levels and uniformity ratios for surface lots and garages, differentiated by activity/security level and area type.[^3][^28]

Representative RP‑20‑derived recommendations:

- **Open surface parking lots** – Basic security: around 0.2 foot‑candles (≈2 lux) minimum, with a maximum‑to‑minimum uniformity ratio of 20:1; enhanced security: 0.5 foot‑candles (≈5 lux) with tighter 15:1 uniformity.[^28][^3]
- **Parking structures** – General parking/driving lanes often designed to roughly 5 foot‑candles average with about 4:1 average‑to‑minimum ratios; ramps and entrances require higher levels (around 10 foot‑candles) to account for eye adaptation and safety.[^29][^3][^28]
- **Pedestrian areas, stairwells, and elevators** – Elevated illuminance (e.g., 10 foot‑candles within 30 feet of pedestrian gathering points) and vertical illuminance recommendations to support facial recognition and CCTV performance.[^3]

Plan reviewers typically check photometric plans for minimum illuminance at calculation points, uniformity ratios, and correct use of maintained (not initial) light levels, including light loss factors in the 0.70–0.85 range for LED fixtures.[^3]

### 2.2 Ventilation in enclosed parking structures

Ventilation requirements for enclosed parking garages are addressed primarily by the International Mechanical Code (IMC), ASHRAE 62.1, and NFPA 88A.

Key elements as summarized in recent technical guidance:

- **IMC 404.1** – Enclosed parking garages must provide mechanical ventilation operating continuously or automatically controlled by carbon monoxide (CO) (and often NO₂) detectors.[^30][^31]
- **Ventilation rates** – Earlier IMC editions required systems capable of 1.5 cubic feet per minute per square foot (CFM/ft²) at full speed with a minimum of 0.05 CFM/ft²; later editions reduced the full‑speed capability requirement to approximately 0.75 CFM/ft² while maintaining the 0.05 CFM/ft² minimum for demand‑controlled operation.[^32][^33]
- **ASHRAE 62.1 pairing** – Widely referenced prescriptive rate is 0.75 CFM/ft² for enclosed commercial garages, with CO‑based demand control allowing turndown to about 0.05 CFM/ft² when pollutant levels are low, provided the system can ramp back up to the full rate when CO rises.[^30]
- **NFPA 88A (2023 edition)** – Requires all enclosed parking structures to be ventilated by a mechanical system capable of providing a minimum of 1 ft/min per ft² (equivalent to 1 CFM/ft²) during normal operation, and mandates installation per NFPA 90A.[^34][^35]

For design, engineers must reconcile the specific IMC edition adopted locally, ASHRAE 62.1, and NFPA 88A, then document airflow rates, detector setpoints, and control sequences accordingly.[^35][^30]

### 2.3 Fire protection in parking garages (NFPA 88A and related codes)

NFPA 88A is the primary standard for construction and protection of open and enclosed parking structures, covering means of egress, structural fire resistance, sprinkler systems, standpipes, and hazard control.  Recent commentary on the 2019 and 2023 editions notes significant updates to opening requirements for open garages, and removal of prior exceptions allowing certain enclosed garages without sprinklers.[^36][^37][^38]

General fire protection implications:

- **Automatic sprinklers** – The 2023 edition of NFPA 88A requires all parking garages to have sprinkler systems installed in accordance with NFPA 13, removing earlier exceptions for some enclosed garages with fire detection and ventilation.[^36]
- **Means of egress** – NFPA 88A prescribes egress path widths, travel distances, and stair/exit distribution appropriate for multi‑level parking.[^37]
- **Integration with local building/fire codes** – The International Building Code (IBC) and International Fire Code (IFC) incorporate NFPA 88A by reference in many jurisdictions, so venues must coordinate structural design, compartmentation, and sprinkler/standpipe coverage with the authority having jurisdiction (AHJ).[^38][^37]

### 2.4 Security camera use and privacy constraints

Security cameras in parking facilities are typically governed not by building codes but by privacy and data‑protection laws, plus industry best practices.

In Canada, guidance from the Office of the Information and Privacy Commissioner for Alberta (OIPC) and general privacy toolkits stress that video surveillance must be reasonable, clearly purposed (e.g., safety or loss prevention), and accompanied by notice to individuals.[^39][^40][^41]

Key best‑practice principles:

- **Purpose limitation** – Footage collected in a parking garage for safety cannot be repurposed for unrelated tracking of tenants or employees without consent.[^42][^39]
- **Notice and signage** – Businesses should post clear signage at entrances stating that video surveillance is in use, why it is used, and contact information.[^43][^41]
- **Scope limitation** – Cameras must not be aimed into areas where individuals have a heightened expectation of privacy (e.g., restrooms, residential windows).[^44][^42]
- **Retention and access** – Retain footage only as long as necessary, secure storage, limit access, and provide a process for individuals to request access to footage in which they appear.[^40][^42]

Municipalities may add specific CCTV conditions in development permits for large garages (e.g., requiring coverage of stairwells and entrances), but these are typically case‑by‑case and negotiated with the AHJ.

***

## 3. Premium Hospitality Licensing and Suite‑Level Food and Beverage

### 3.1 Liquor licensing models for suites and clubs

Liquor licensing for premium suites and clubs depends on provincial/state frameworks and how they classify spectator venues, lounges, and club spaces.

In Canadian provinces, sporting and cultural venues often require a **special facility** or similar licence category that authorizes liquor sales in arenas and stadiums, sometimes with sub‑areas such as lounges, clubs, and suites.  For example, New Brunswick uses a "special facility licence" for sporting, cultural, or theatrical establishments and trade/convention centres, with specific seating thresholds and fees.[^45][^46]

In Alberta, arenas typically operate under an Alberta Gaming, Liquor and Cannabis Commission (AGLC) Class A licence (e.g., minors allowed or minors prohibited) and may layer **Special Event Licences (SELs)** for certain private or public events.  As of late 2025, AGLC introduced a Private Non‑Sale Annual SEL allowing certain businesses without a regular liquor licence to offer occasional complimentary liquor service to private members or guests, subject to policy conditions.[^47][^4][^48]

Implications for premium suites and clubs:

- **General premises vs. private suites** – In some jurisdictions, lounge or restaurant licences cover all public areas (concourse, clubs) while private corporate suites may be treated as part of the licensed premises or require additional endorsements / event permits depending on alcohol sales vs. complimentary service.[^49][^45][^47]
- **Private events and SELs** – AGLC’s private SEL framework distinguishes private events (members/invited guests only, with free alcohol) from public events; corporate hospitality that charges for admission or liquor must use the appropriate sale‑authorized licence rather than a non‑sale SEL.[^4][^47]
- **Minors access** – Licences often distinguish minors‑allowed vs. minors‑prohibited areas, which may require different conditions for family suites vs. adult‑only clubs.[^46]

### 3.2 Food service permits and suite‑level catering

Food safety for suite catering is usually governed by provincial/state food regulations and local health authority permits.

In Calgary, for example, food establishments are regulated under Alberta Regulation 31/2006, which sets standards for hygiene, food handling, and food‑handler certification.  Any business handling food (restaurants, caterers, concessionaires, and suites served by them) must have at least one certified food handler present when six or more food handlers are on‑site, with similar obligations for smaller staffing levels.[^50]

Stadium implications:

- **Central kitchens and commissaries** – The main kitchen(s) serving suites and clubs are typically licensed as food service establishments and inspected by the local health authority; suites themselves are treated as satellite service points supplied by the licensed kitchen.[^50]
- **Third‑party caterers** – If external caterers serve suites, they must hold the requisite food premise permits and meet local training requirements.[^50]
- **Menu and service conditions** – Venue catering policies often require food orders when alcohol is requested and prohibit outside food and beverage to maintain control over food safety and liquor compliance (as illustrated by suite catering menus for university and stadium clients).[^51]

### 3.3 Health department expectations for premium areas

Health authorities apply the same food safety standards to premium hospitality as to general concessions but may scrutinize premium areas for:

- **Temperature control and holding** – Safe holding of hot and cold foods delivered to suites, including time‑stamping and procedures for discarding food after service windows.[^50]
- **Allergen and dietary management** – Processes to capture and implement allergen and dietary information noted in suite order forms (e.g., Calgary Stampede infield suites explicitly request allergy/dietary considerations on their order forms).[^52]
- **Sanitation and waste** – Safe handling of dishware, linens, and waste removal from suites to avoid pest or contamination issues.[^50]

Venue operators should maintain written HACCP or equivalent food safety plans that explicitly cover suite service workflows and training.

***

## 4. Venue Marketing: Email, Anti‑Spam, and Endorsement Rules

### 4.1 CAN‑SPAM Act (U.S.)

The CAN‑SPAM Act (15 U.S.C. § 7701 et seq.) sets national standards for commercial email in the United States and is enforced by the Federal Trade Commission.  The FTC summarizes the core requirements as seven main obligations.[^5][^53]

Key CAN‑SPAM requirements for venue marketing emails:

- **No false or misleading header information** – "From," "To," "Reply‑To," and routing info must accurately identify the sender and originating domain.[^53][^5]
- **No deceptive subject lines** – Subject lines must accurately reflect the message content.[^5][^53]
- **Identify the message as an advertisement** – The email must clearly and conspicuously indicate that it is an ad or promotional message unless an exception applies.[^5]
- **Include a valid physical postal address** – A current street address, post office box, or registered private mailbox is required.[^54][^5]
- **Provide a clear and functioning opt‑out mechanism** – Recipients must be able to opt out via a clear, easy method; opt‑out requests must be honored within 10 business days.[^53][^5]
- **Monitor third‑party senders** – Both the company whose product is promoted and any third‑party email service can be held legally responsible.[^5]

Violations can trigger civil penalties per violating email, with FTC guidance citing penalty amounts that have been periodically adjusted for inflation (well into five figures per message as of recent updates).[^5]

### 4.2 CASL (Canada’s Anti‑Spam Legislation)

CASL applies to commercial electronic messages (CEMs) sent to or from Canadian computers and devices and is enforced by the CRTC, Competition Bureau, and Office of the Privacy Commissioner.  CASL is generally stricter than CAN‑SPAM, requiring prior consent (express or implied) for most CEMs, plus specific form and content requirements.[^6][^55]

Core CASL requirements:

- **Consent first** – Under CASL, senders must have valid consent (express or implied) before sending a CEM; a message asking for consent is itself considered a CEM and requires consent unless an exemption applies.[^55][^56][^6]
- **Express vs. implied consent** – Express consent is opt‑in and requires clear disclosure of purposes, identification of the sender, and contact information; implied consent can arise from existing business relationships, non‑business relationships, or conspicuous publication of an email address in certain contexts.[^57][^6][^55]
- **Form and content of CEMs** – Messages must identify the sender and any party on whose behalf the message is sent, provide mailing and contact information, and include an unsubscribe mechanism that is simple and free to use.[^56][^6]
- **Onus of proof** – The sender bears the burden of proving consent and must maintain accurate records.[^6][^57]

Penalties under CASL can be severe (including multi‑million‑dollar administrative monetary penalties), so venues marketing to Canadian patrons typically maintain CASL‑compliant consent logs, preference centers, and unsubscribe systems.[^55][^57]

### 4.3 CAN‑SPAM vs. CASL – key contrasts for venues

| Aspect                        | CAN‑SPAM (U.S.)                                   | CASL (Canada)                                                   |
|-------------------------------|---------------------------------------------------|-----------------------------------------------------------------|
| Consent model                 | Opt‑out – consent not required to send initial CEM; must allow unsubscribe.[^5][^53] | Opt‑in – express or implied consent required before sending CEMs.[^6][^55] |
| Geographic scope              | Commercial email sent to or from U.S., or affecting U.S. consumers.[^53] | CEMs sent to or from Canadian devices or accessed in Canada.[^55][^57] |
| Identification requirements   | Accurate header, subject, and physical address.[^5][^53] | Sender identity, mailing address, and contact info must appear in CEM.[^6][^55] |
| Unsubscribe requirements      | Clear opt‑out mechanism; 10‑business‑day processing.[^5][^53] | Functional unsubscribe mechanism; must be processed without delay (within 10 business days under CRTC guidance).[^6][^57] |
| Enforcement/potential fines   | FTC civil penalties per email; can also include criminal charges for aggravated violations.[^5][^53] | Administrative monetary penalties up to millions; strict liability and due‑diligence expectations.[^55][^57] |

Venues with cross‑border marketing lists should segment and apply the stricter CASL standard for Canadian recipients to minimize compliance risk.

### 4.4 FTC Endorsement Guides and social media disclosures

The FTC’s Endorsement Guides (16 CFR Part 255) and staff documents such as "Disclosures 101 for Social Media Influencers" govern endorsements and testimonials in advertising, including social media posts by influencers, athletes, and venue partners.[^58][^59]

Key requirements for sponsored content and endorsements:

- **Material connection disclosure** – Any financial, employment, family, or other material relationship between the endorser (e.g., an athlete or influencer) and the brand or venue must be clearly disclosed.[^59][^58]
- **Clear and conspicuous placement** – Disclosures must be hard to miss and placed with the endorsement (e.g., at the beginning of a caption, on‑screen in video, verbally in audio); profile or "about" page disclosures alone are insufficient.[^60][^58][^59]
- **Hashtags and labels** – Obvious tags like #ad or #sponsored are generally acceptable when used prominently; ambiguous tags (#sp, #partner) may not be adequate.[^58][^59]
- **Truthfulness and substantiation** – Endorsements must reflect honest opinions and typical results, and advertisers must have adequate evidence for objective claims (e.g., performance claims for seats or premium experiences).[^58]

The 2023 revisions to the Endorsement Guides expanded the definition of "endorsement" to include tags, likes, or depictions of a person’s likeness where a material connection exists and reinforced enforcement against fake or manipulated reviews.[^60][^58]

### 4.5 Social media advertising and venue campaigns

For venue‑run social campaigns promoting events, suites, or partnerships:

- Posts featuring compensated influencers, sponsored teams, or exclusive suite hosts should include clear #ad/#sponsored disclosures.[^59][^58]
- If posts feature contest winners or invited guests whose travel/experience is covered by the venue or sponsor, that support is a material connection requiring disclosure.[^59][^58]
- U.S. law applies if posts are reasonably expected to reach U.S. consumers, even if posted from abroad, while foreign laws (e.g., CASL for CEMs, Canadian advertising standards) may also apply concurrently.[^59]

***

## 5. Digital Signage and Marquee Regulations

### 5.1 General local sign ordinance themes

Large venue digital signs and marquees are governed primarily by municipal sign codes, which specify sign classes, permitted locations, size/height limits, illumination and brightness caps, content restrictions (e.g., no off‑premise advertising in certain districts), and permitting processes.  For example, Calgary’s Land Use Bylaw 1P2007 includes a Division on signs that requires development permits for all signs and sets rules for digital displays, third‑party advertising signs, and comprehensive sign programs.[^61][^62][^63][^8]

Common elements in major city sign codes:

- **Permit requirement** – Most new signs and any enlargement, relocation, or alteration require a development permit or sign permit.[^63][^8]
- **Zoning constraints** – Digital and third‑party (off‑premise) signs are limited to specific land‑use districts and subject to separation distances from other digital signs and sensitive uses.[^62][^8]
- **Illumination and operating characteristics** – Codes restrict brightness, require automatic dimming, and often prohibit full‑motion video, flashing, or rapid message changes to minimize driver distraction.[^7][^61][^62]

### 5.2 Brightness limits and measurement (nits, lux, foot‑candles)

A widely adopted standard for electronic message centers (EMCs) is that night‑time brightness must not exceed 0.3 foot‑candles above ambient light at a specified measurement distance, with automatic ambient‑light controls.  Research sponsored by the International Sign Association and Sign Research Foundation recommends this 0.3‑foot‑candle threshold and the use of photocells to adjust luminance to ambient conditions.[^64][^65][^61]

Illustrative regulatory examples:

- **Edmonton sign regulations** – Digital signs must use ambient light monitors, brightness must not exceed 0.3 foot‑candles above ambient when measured from the sign face between sunset and sunrise, and luminance must not exceed 400 nits at night for certain digital sign types.[^61][^7]
- **Other Canadian municipalities** – Jurisdictions such as Toronto and Winnipeg have adopted similar 0.3‑foot‑candle thresholds, with some specifying maximum nits (e.g., 220–400 cd/m²) between sunset and sunrise.[^66][^61]
- **Calgary digital third‑party forms** – Calgary requires digital third‑party advertising sign applications to confirm that the sign can be set not to exceed 3.0 lux at specified measurement points and to specify maximum luminance in nits by land‑use district.[^67][^63]

At the federal level in the U.S., Federal Highway Administration guidance and industry standards also anchor on the 0.3‑foot‑candle method for billboards along federal‑aid highways.[^68][^65]

### 5.3 Animation, dwell times, and content restrictions

Municipal sign guidelines for digital third‑party advertising signs often:

- **Limit animation and video** – Calgary’s third‑party advertising sign guidelines, for example, recommend prohibiting animation, sequential messages, and full‑motion video on digital third‑party advertising signs to reduce driver distraction.[^62]
- **Control message dwell times** – Many cities require static images with minimum dwell times (e.g., 6–10 seconds) before changing, though the precise numbers vary by ordinance (often detailed in local zoning documents not publicly summarized beyond the animation prohibition).[^69][^62]
- **Set curfews and blackout conditions** – Some codes require de‑energizing digital signs adjacent to natural areas or residential districts between midnight and early morning hours.[^7][^61]

Content restrictions generally focus on prohibiting obscene or illegal content and limiting off‑premise advertising in certain zones; viewpoint‑based content regulation is constrained by constitutional and Charter protections.

### 5.4 Permitting and comprehensive sign programs

For large venues, municipalities often encourage or require **comprehensive sign programs** that address all on‑site signage (building signs, wayfinding, digital marquees, and third‑party advertising signs) under a unified development permit.[^8][^62]

Typical permit expectations:

- Site plans showing sign locations, separation distances from other digital signs, proximity to dwellings, and direction of illumination.[^63]
- Technical specifications including sign dimensions, mounting height, power routing (often required underground), luminance caps, ambient light sensor details, and maximum lux at property boundaries.[^67][^63]
- Operating conditions such as automatic dimming, blackout modes in case of malfunction, curfews, and restrictions on animation and dwell times.[^7][^62]

Early engagement with municipal planning and transportation departments is essential when locating large, bright marquees near arterial roads or highways.

***

## 6. Ride‑Share and Transportation Coordination for Large Events

### 6.1 Municipal regulation of ride‑share (TNC) pick‑up/drop‑off zones

Regulation of ride‑share pick‑up/drop‑off (PUDO) zones is typically embedded in municipal traffic bylaws, curb‑management policies, and, for airports and some large venues, specific operating agreements with transportation network companies (TNCs). While comprehensive TNC ordinances vary by city and were not exhaustively catalogued here, common regulatory themes include:

- **Designated PUDO zones** – Cities often require designated PUDO areas on or near event sites, with clear signage and sometimes geofenced zones in TNC apps to prevent random stops that block traffic.[^70][^71][^72]
- **Restrictions in residential areas** – Event transport plans and neighborhood festival guidance encourage locating ride‑share PUDO away from residential streets to reduce noise and congestion, in coordination with city traffic engineers.[^73][^72]
- **Safety and accessibility** – PUDO design must maintain emergency access, accessible routes between drop‑off zones and venue entrances, and compliance with ADA/accessible transport requirements for shuttles and paratransit.[^74][^71]

Venue‑specific development permits or event licences may codify PUDO arrangements, including maximum dwell times, prohibited standing zones, and staffing requirements.

### 6.2 Traffic management plans for planned special events (FHWA guidance)

The U.S. Federal Highway Administration’s "Managing Travel for Planned Special Events" provides widely used guidance for traffic management plans (TMPs) for concerts, sports, festivals, and similar large gatherings.[^71][^75][^74]

Key elements of a TMP:

- **Site access and parking plan** – Strategies for managing automobile, bus, taxi, limousine, and shuttle traffic to public parking areas, reserved/permit parking, overflow parking, and PUDO areas.[^74]
- **Pick‑up/drop‑off planning** – Designated off‑street areas for private vehicles, taxis, and limousines; queuing systems to manage vehicle arrivals and departures; and off‑site staging lots for vehicles waiting to pick up event patrons.[^71][^74]
- **Local and corridor flow routes** – Design of local flow routes around the venue and corridor routes to/from freeways and major arterials, including temporary lane controls, reversible lanes, and signal timing plans.[^75]
- **Transit and shuttle integration** – Exclusive bus routes or lanes, temporary bus stations, and clear mapping and signage for shuttle services from satellite parking.[^75][^71]

These components are typically formalized in a TMP submitted to the local DOT or traffic engineering department for review and approval as a condition of event permitting.

### 6.3 Best practices for ride‑share operations at venues

Industry case studies and festival operations guidance converge on several best practices that align with municipal expectations:

- **Official PUDO zones with geofencing** – Work with TNCs such as Uber and Lyft to geofence PUDO areas so that drivers and riders are directed there automatically, avoiding random curbside stops.[^72][^70]
- **Layout and capacity planning** – Design PUDO loops or lots with sufficient capacity for peak loads, with clearly marked in/out lanes, cones, and barriers to prevent blocking through traffic.[^70]
- **Signage and wayfinding** – Use prominent static and digital signage to guide drivers and pedestrians to PUDO zones, and include PUDO locations on venue maps, websites, and apps.[^70][^71]
- **Staffing and traffic marshals** – Deploy trained staff in high‑visibility vests to manage queues, limit dwell times, and coordinate with law enforcement and traffic control centers during ingress and egress peaks.[^71][^70]
- **Neighborhood and emergency considerations** – Design PUDO and routing to minimize impacts on adjacent neighborhoods and maintain clear emergency routes; contingency plans should address surges (e.g., sudden weather changes) and emergency access needs.[^73][^75][^70]

***

## 7. Compliance Strategy for Large Venues

Given the overlapping regulatory layers summarized above, large venues benefit from a structured compliance program that coordinates facilities, operations, legal, and marketing teams.

Key structural elements:

- **Regulatory mapping** – Maintain a matrix of applicable federal, provincial/state, and municipal requirements covering ADA, building/fire/ventilation codes (NFPA, IMC, ASHRAE), liquor and food licences, sign and zoning bylaws, privacy/CCTV rules, anti‑spam statutes, and advertising/endorsement regulations.[^1][^34][^45][^55]

---

## References

1. [2010 ADA Standards for Accessible Design](https://www.ada.gov/law-and-regs/design-standards/2010-stds/) - The 2010 Standards set minimum requirements – both scoping and technical – for newly designed and co...

2. [Chapter 2: Scoping Requirements - Access-Board.gov](https://www.access-board.gov/ada/chapter/ch02/) - ... 208 provides general scoping for accessible parking and Section 208.2.3.1 specifies the required...

3. [IES RP-20 Explained: Parking Facility Lighting Standards](https://photometricbureau.com/resources/ies-rp-20-parking-lighting-standards) - The core of RP-20's guidance is a table of recommended maintained horizontal illuminance levels, org...

4. [Special Event Licence - Private - Policies and Guidelines - AGLC](https://aglc.ca/forms/special-event-licence-private-policies-and-guidelines) - Apply for a Private SEL. You need a private SEL to sell or provide liquor at private events like wed...

5. [CAN-SPAM Compliance: A Comprehensive Guide - LashBack](https://lashback.com/can-spam-compliance-what-to-know/) - Don't use false or misleading sender information · Don't use deceptive subject lines · Identify the ...

6. [From Canada's Anti-Spam Legislation (CASL) Guidance on Implied ...](https://crtc.gc.ca/eng/com500/guide.htm) - The following guidelines provide direction and clarification on whether you can rely on implied cons...

7. [59. Sign Regulations - City of Edmonton](https://webdocs.edmonton.ca/zoningbylaw/ZoningBylaw/Part1/Development/59__Sign_Regulations.htm) - Brightness levels shall not exceed 0.3 footcandles above ambient light ... For all Sign Applications...

8. [Division 5: Signs - The City of Calgary Land Use Bylaw 1P2007](https://www.calgary.ca/planning/land-use/online-land-use-bylaw.html?part=3&div=5) - All signs, structures for signs and any enlargement, relocation, erection, construction or alteratio...

9. [Chapter 5: Parking Spaces - Access-Board.gov](https://www.access-board.gov/ada/guides/chapter-5-parking/) - At least one space for every 6 or fraction of 6 accessible spaces must be van accessible. Van spaces...

10. [Minimum Number: ADA Standard Section 208.2 - Corada](https://www.corada.com/documents/2010ADAStandards/208-2) - 208.2 Minimum Number. Parking spaces complying with 502 shall be provided in accordance with Table 2...

11. [ADA Compliance Brief: Restriping Parking Spaces](https://www.ada.gov/resources/restriping-parking-spaces/) - Minimum Number of Accessible Parking Spaces ; 9 · 2% of total parking provided in each lot or struct...

12. [208 Parking Spaces - ADA Compliance](http://www.ada-compliance.com/ada-compliance/208-and-502-parking-spaces.html) - 208.2 Minimum Number. Parking spaces complying with 502 shall be provided in accordance with Table 2...

13. [[PDF] The Americans with Disabilities Act (ADA) and](https://www.parking.org/wp-content/uploads/2016/02/TPP-2015-11-The-Americans-with-Disabilities-Act-ADA-and-Parking.pdf) - The minimum number of parking spaces required to be accessible is listed in Table 208.2 and based up...

14. [502 Parking Spaces - Corada](https://www.corada.com/documents/ada-aba-guidelines-preamble/502) - Comment. The proposed rule specified that car and van spaces be at least 8 feet wide and that access...

15. [11B-502 Parking spaces. - Corada](https://www.corada.com/documents/2016CBCPG/11b-502-parking-spaces) - Access aisles serving car and van parking spaces shall be 60 inches (1524 mm) wide minimum. 11B-502....

16. [Van Space: Wider Parking Space - Corada](https://www.corada.com/documents/guide-to-the-ada-standards/van-space-wider-parking-space) - Van accessible parking space 132” wide min. and access aisle 60” wide min · design compass icon. Rec...

17. [ADA Standards: Parking Animation - YouTube](https://www.youtube.com/watch?v=Ngvb0JVLG00) - This video is provided by the United States Access Board for ADA Standards. About ADA Inspections Na...

18. [[PDF] Technical Assistance Updates from the U.S. Department of Justice](https://www.redondochamber.org/uploads/1/3/7/1/137169629/3._ada_technical_assitance__more.pdf) - 2 of the Standards requires that accessible parking spaces, including van accessible spaces, be loca...

19. [[PDF] 1. “Design Details: Van Accessible Parki - PDH Online](https://pdhonline.com/courses/g393/ADA%20Parking%20Guidelines.pdf) - This document is a compilation of two documents from the U.S. Department of. Justice: 1. “Design Det...

20. [Chapter 4: Accessible Routes - Access-Board.gov](https://www.access-board.gov/ada/guides/chapter-4-accessible-routes/) - An accessible route must connect accessible facility entrances with all accessible spaces and elemen...

21. [Site Arrival Points [§206.2.1] - Guide to the ADA Standards - Corada](https://www.corada.com/documents/guide-to-the-ada-standards/where-required-site-arrival-points-206-2-1) - At least one accessible route must connect all accessible spaces and elements. If a circulation path...

22. [206 and Chapter 4 Accessible Routes - ADA Compliance](http://www.ada-compliance.com/ada-compliance/206-and-chapter-4-accessible-routes) - 206.2.1 Site Arrival Points. At least one accessible route shall be provided within the site from ac...

23. [ADA Accessible Vehicle Parking Facilities Scoping Requirements](https://inspectionsada.com/ada-compliance-blog/2020/12/22/ada-accessible-vehicle-parking-facilities-scoping) - Issues that must satisfy ADA requirements for accessible parking facilities include number of parkin...

24. [ADA Accessibility Guidelines (ADAAG) - Sections 1-4](https://www.statereview.com/adaag.htm) - Interior accessible routes may include corridors, floors, ramps, elevators, lifts, and clear floor s...

25. [Site Arrival Points and When Accessible Routes Are Required](https://www.coreyandpartners.com/post/understanding-ada-206-2-1-site-arrival-points-and-when-accessible-routes-are-required) - ADA 206.2.1 Site Arrival Points requires at least one accessible route within a site from site arriv...

26. [A Planning Guide for Making Temporary Events Accessible to ...](https://adata.org/guide/planning-guide-making-temporary-events-accessible-people-disabilities) - This guide provides information to assist planners, managers, operators and building owners in makin...

27. [208.2 Minimum Number - Corada](https://www.corada.com/documents/2012-FACBC-PG-v1/208-2) - 208.2.5.2 There must be one accessible parking space for each 150 metered on-street parking spaces p...

28. [Illuminance Standards for Outdoor Lighting | PDF - Scribd](https://www.scribd.com/document/229032568/Illumination-Levels) - Parking Facilities Parking Lots: (See RP-20-98 for details) Basic 1. Enhanced Security 2. Minimum Ma...

29. [Parking Garage Lighting Standards Guide | Hyperlite](https://hi-hyperlite.com/blogs/comprehensive-guides/parking-garage-lighting-standards-guide) - ... light levels required on ramps. IES RP-20 explicitly recommends 10 maintained footcandles for th...

30. [Garage Ventilation Requirements: IMC, IRC, And ASHRAE 62.1](https://www.wholehousefan.com/blogs/wholehousefans/garage-ventilation-requirements) - IMC/ASHRAE 62.1 (enclosed parking): CFM_total = 0.75 × floor_area (ft²) ; demand-control minimum ≈ 0...

31. [[PDF] International Mechanical Code 2021 - All Star Training](https://allstarce.com/wp-content/uploads/2022/09/2021-IMC-Chapter-4-Ventilation.pdf) - Ventilation systems in enclosed parking garages shall comply with Section 404 . e. Rates are per wat...

32. [[PDF] IMC 2024 CHANGES AFFECTING PARKING GARAGE ...](https://inteccontrols.com/wp-content/uploads/2025/04/IMC-2024-Changes-for-Parking-Garages.pdf) - Minimum ventilation rate of 0.05 cfm per square foot required. • System must be capable of 1.5 cfm p...

33. [[PDF] GARAGE VENTILATION](https://parking.org/wp-content/uploads/2016/01/TPP-2014-04-Garage-Ventilation.pdf) - Prior to the 1990s, the IMC mandated a design ventilation rate of 1.5 cubic feet per minute (cfm) pe...

34. [Introduction to Our White Paper on NFPA 88A Parking ...](https://www.systemair.com/en-us/expertise/blog/introduction-to-our-white-paper-on-nfpa-88a-parking-garage-requirements) - All enclosed parking structures must be ventilated by a mechanical system capable of providing a min...

35. [Introduction to Our White Paper on NFPA 88A Parking Garage ...](https://www.systemair.com/en-ca/expertise/blog/introduction-to-our-white-paper-on-nfpa-88a-parking-garage-requirements) - All enclosed parking structures must be ventilated by a mechanical system capable of providing a min...

36. [The New Standard for Parking Structures: NFPA 88A](https://hct-world.com/the-new-standard-for-parking-structures/) - A new NFPA standard, NFPA 88A, for parking structures is paving the way for fire protection solution...

37. [NFPA 88A Standard for Parking Structures, 2019 Edition](https://blog.ansi.org/ansi/nfpa-88a-standard-parking-structures-2019/) - This standard document is purposed with providing minimum fire protection standards for parking stru...

38. [NFPA 88A Standard Development](https://www.nfpa.org/codes-and-standards/nfpa-88a-standard-development/88a) - This standard covers the construction and protection of, as well as the control of hazards in, open ...

39. [Video Surveillance in the Private Sector](https://oipc.ab.ca/resource/video-surveillance/) - Private sector privacy laws require that organizations' need to conduct video surveillance must be b...

40. [[PDF] Guide to Using Surveillance Cameras in Public Areas](https://open.alberta.ca/dataset/2dab1729-0e71-4501-9788-ce8e1eb483be/resource/5188d1f6-6234-426c-b889-86bc5192f3e5/download/surveillanceguide.pdf) - This guide is intended to assist public bodies in deciding whether collection of personal informatio...

41. [Understanding CCTV Camera Laws in Canada - Smart Vision Plus](https://www.smartvisionplus.ca/blog/understanding-cctv-camera-laws-in-canada/) - Learn about CCTV camera laws in Canada with Smart Vision Plus. Stay informed on legal requirements a...

42. [Canadian CCTV Privacy Laws: Official Compliance Guidance](https://northwestsecurity.ca/canada/ontario/canadian-cctv-privacy-laws-official-compliance-guidance/) - For businesses, yes—it's mandatory. For homeowners, it's not legally required but is considered best...

43. [What You Need To Know Before Installing A CCTV Camera](https://www.calgaryalarm.com/blog/cctv-camera/what-you-need-to-know-before-installing-a-cctv-camera/) - The use of cameras (including hidden ones) is legal, and they can be used as evidence in a court of ...

44. [Guidelines for the Use of Video Surveillance of Public Places by ...](https://www.priv.gc.ca/en/privacy-topics/surveillance/police-and-public-safety/vs_060301/?wbdisable=true) - Surveillance cameras should not be aimed at or into areas where people have a heightened expectation...

45. [Liquor licences and permits - gnb.ca](https://www.gnb.ca/en/topic/laws-safety/licensing-inspections/liquor-licences-permits.html) - A special facility licence is required to sell liquor in a public place such as a sporting, cultural...

46. [Business Licence Categories - City of Edmonton](https://www.edmonton.ca/business_economy/licences_permits/business-licence-classifications) - Businesses are encouraged to apply for an AGLC liquor licence before, or during the business licence...

47. [Apply online for special event liquor licences - AGLC](https://aglc.ca/event-licence/) - Obtaining an AGLC liquor licence for a privately held event is easy with this online form with step ...

48. [Private Non-Sale Annual Special Event Licence - AGLC](https://aglc.ca/liquor-bulletins/private-non-sale-annual-sel) - You need a private SEL to sell or provide liquor at private events like weddings, family reunions or...

49. [Special occasion permits | Alcohol and Gaming Commission of Ontario](https://www.agco.ca/en/alcohol/special-occasion-permits) - You don't need a permit (also known as a special occasion permit) if you're serving alcohol to invit...

50. [Calgary Food Safety Regulations](https://www.foodsafetymarket.com/calgary-food-safety-regulations) - Alberta Regulation 31/2006, which covers everything from food handler certification to standards of ...

51. [[PDF] Stadium Suites Menu - Three Pillars Catering](https://www.threepillarscatering.com/sites/default/files/2024-08/catering-suites-fall24.pdf) - Food must be ordered if alcohol is requested. All orders are subject to 8.75% sales tax and a 10% gr...

52. [Dining & Menus - Infield Suites | Calgary Stampede](https://premiumseating.calgarystampede.com/infield-suites/dining-and-menus) - Tickets include a premium lunch or dinner selection, bottled water, soft drinks, juice, regular coff...

53. [Complying with the CAN SPAM Act | Federal Trade Commission](https://www.youtube.com/watch?v=31bX_i9p8pc) - If you use email to promote your products or services, there are seven things you need to know to co...

54. [6 Legal Requirements You NEED to Comply With to Send Marketing ...](https://www.youtube.com/watch?v=p_Xk0ZJH2ek) - legal requirements you MUST follow to stay compliant with the CAN-SPAM Act ... The CAN-SPAM Act and ...

55. [CASL - Canada's Anti-Spam Legislation](https://chamber.ca/resources/canadas-anti-spam-legislation/) - Under CASL, consent is required before sending a CEM. Yet, an electronic message that is sent to obt...

56. [Anti-Spam (& Tool Kit) - David Young - Law](https://davidyounglaw.ca/anti-spam/) - The CRTC regulations specify the required form and content of CASL-compliant CEMs as well as the for...

57. [Guide to Doing Business in Canada: CASL - Gowling WLG](https://gowlingwlg.com/en/insights-resources/guides/2023/doing-business-in-canada-casl) - Second, even where consent exists, CASL requires commercial electronic messages to contain certain d...

58. [A Startup's Guide to FTC Endorsement Guidelines (16 CFR Part 255)](https://blog.promise.legal/startup-central/a-startups-guide-to-ftc-endorsement-guidelines-16-cfr-part-255-ensuring-transparency-in-endorsements-and-testimonials/) - FTC endorsement guidelines for startups. Disclosure requirements, influencer compliance, 2023 revisi...

59. [Disclosures 101 for Social Media Influencers](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers) - One key is to make a good disclosure of your relationship to the brand. This brochure from FTC staff...

60. [FTC Proposed Updates to Endorsement Guides and .com ...](https://www.arnoldporter.com/en/perspectives/advisories/2022/06/ftc-proposed-updates-to-endorsement-guides) - FTC Proposed Updates to Endorsement Guides and .com Disclosures Guidance Signal Continued Regulatory...

61. [[PDF] Planning & Design Review of Illuminated and Electronic Signs](https://www.toronto.ca/legdocs/mmis/2015/pg/bgrd/backgroundfile-81186.pdf) - Sign brightness cannot exceed 0.3 foot candles above ambient light conditions between sunset and sun...

62. [[PDF] Calgary Third Party Advertising Sign Guidelines](https://www.calgary.ca/content/dam/www/pda/pd/documents/development/thirdpartyadvertisingsignguidelines.pdf) - The introduction of digital display screens to Third Party. Advertising Signs has changed the tradit...

63. [[PDF] Plans Digital Third Party Advertising Sign - The City of Calgary](https://www.calgary.ca/content/dam/www/pda/pd/documents/carls/development-permit/sign-digital-third-party-advertising.pdf) - NOTE: This application does not relieve the owner or the owner's authorized agent from full complian...

64. [EMC Brightness Level Recommendations](https://signs.org/codes-regulations/signcodehelp/emcs/emc-brightness-level-recommendations/) - The report recommends that EMCs not exceed 0.3 footcandles over ambient lighting conditions when mea...

65. [[PDF] RESEARCH - Daktronics](https://www.daktronics.com/web-documents/Lit/ISA_Brightness_Levels_Recommendations.pdf) - The city adopted the widely recognized standard of 0.3 footcandles above ambient light, using the di...

66. [[PDF] NOTICE OF DECISION - Regional Municipality of Wood Buffalo](https://www.rmwb.ca/media/pbsaki2u/2024-002-sdab-decision_redacted.pdf) - not exceed 0.3 footcandles above ambient light conditions when ... b) Brightness level of the Sign s...

67. [[PDF] Digital Third Party Advertising Sign Information Form](https://www.calgary.ca/content/dam/www/pda/pd/documents/carls/development-permit/sign-digital-third-party-advertising-information-form.pdf) - 10 Can the sign be set to not exceed 3.0 LUX? ❑ Yes. ❑ No. 11. Land Use District. Maximum Luminance ...

68. [Checklist for Billboard Lighting Compliance](https://www.blipbillboards.com/blog/checklist-for-billboard-lighting-compliance/) - Digital billboards must adhere to specific brightness limits, ensuring they don't exceed 0.3 foot-ca...

69. [[PDF] Comment on Methods of Measuring Sign Brightness](https://docsonline.sanantonio.gov/FileUploads/dsd/CommentonBrightness.pdf) - no greater than 0.3 foot candles over ambient light levels. • Page 71: Sec. 28-125 (b) (3) (b) Off-p...

70. [Mastering Rideshare and Drop-Off Zone Coordination for Festivals](https://www.ticketfairy.com/blog/mastering-rideshare-and-drop-off-zone-coordination-for-festivals) - Creating a designated drop-off and pickup zone near the festival entrance is critical for traffic ma...

71. [Managing Travel for Planned Special Events - FHWA Operations](https://ops.fhwa.dot.gov/publications/fhwaop04010/chapter6_04.htm) - Guidelines for Designating Pick-up and Drop-off Areas. Guideline. Utilize off-street areas for priva...

72. [Transport Plans for Neighbourhood Festivals - Ticket Fairy](https://www.ticketfairy.com/blog/transport-plans-for-neighbourhood-festivals) - Rideshare Pick-Up/Drop-Off Zones Away from Homes. Ride-hailing services like Uber, Lyft and taxis ca...

73. [[PDF] Special Event Emergency Planning Guidelines](https://www.muskokalakes.ca/media/0qejvbci/special-event-emergency-planning-guidelines.pdf) - This guide is designed to share best practices and resources, as well as to highlight regulations th...

74. [Managing Travel for Planned Special Events - FHWA Operations](https://ops.fhwa.dot.gov/publications/fhwaop04010/chapter3_05.htm) - A traffic management plan indicates how traffic, parking, and pedestrian operations will be managed ...

75. [Managing Travel for Planned Special Events - FHWA Operations](https://ops.fhwa.dot.gov/publications/fhwaop04010/chapter6_06.htm) - Local flow routes traverse the street system adjacent to the event venue and service a particular pa...

