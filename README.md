# Venue Operations Knowledge Base

An open-source, educational knowledge base mapping the complete venue operations ecosystem — from food and beverage to emergency management, from IT infrastructure to premium hospitality.

## What This Is

This knowledge base is a structured, interconnected reference covering how large venues operate. It spans convention centres, arenas, stadiums, performing arts centres, integrated resorts, theme parks, and major attractions.

Every entry is sourced from publicly available research, industry publications, regulatory documents, and trade association resources. Every claim is cited. The methodology and tools used to build it are fully documented.

## Who This Is For

Mid-to-senior venue operations professionals — general managers, VPs of operations, directors of guest experience, continuous improvement leads, and anyone working in or with large-scale venue operations.

## How to Use It

This is an [Obsidian](https://obsidian.md) vault. Open it as a vault in Obsidian to get full navigation, search, graph visualization, and interactive queries.

**Start here:**
- `07_MOCs/Map-Venue-Operations-Ecosystem.md` — the master map of all 26 domains
- `07_MOCs/Map-{Domain-Slug}.md` — curated navigation for each of 26 domains (concept clusters, cross-domain connections, reading paths for different practitioner roles)
- `01_Domains/Domain-{Slug}.md` — scope definition and key functions for each domain
- `01_Domains/{domain-slug}/` — concept notes within each domain
- `METHODOLOGY.md` — how this KB was built, what AI did, what humans did, limitations, how to trace any claim

**Two entry points per domain:**
1. **Domain overview** (`Domain-{Slug}`) — *what the domain is* (scope, functions, cross-references)
2. **Domain MOC** (`Map-{Slug}`) — *how to find content fast* (concept clusters, reading paths)

Use them together.

**Graph-based exploration:**
- Obsidian graph view visualizes relationships across all 26 domains
- Dataview queries surface real-time coverage dashboards
- Cross-domain wikilinks let you jump between related concepts

## Structure

| Folder | Contains |
|--------|----------|
| `01_Domains/` | Operational domain overviews and concept notes (26 subfolders) |
| `02_Standards/` | Regulatory standards, codes, and certifications |
| `03_Technology/` | Platforms, tools, and systems |
| `04_Organizations/` | Industry bodies and associations |
| `05_People/` | Industry practitioners and thought leaders |
| `06_Sources/` | Citation notes — one per referenced source |
| `07_MOCs/` | Maps of Content — navigational overviews |

## 26 Operational Domains

1. Guest Experience
2. People & Culture
3. Food & Beverage
4. Event Operations
5. Facilities & Building Systems
6. Safety & Risk
7. Security
8. Crowd Management
9. Sustainability & Environmental
10. Technology & Digital
11. AV & Production
12. Data & Analytics
13. Financial Operations
14. Commercial & Revenue
15. Ticketing & Box Office
16. Booking & Sales
17. Supply Chain & Procurement
18. Logistics & Warehouse
19. Parking & Transportation
20. Marketing & Communications
21. Premium & VIP
22. Legal, Compliance & Licensing
23. Inclusivity & Accessibility
24. Strategy & Governance
25. Quality & Continuous Improvement
26. Tenant & Partner Relations

## How It Was Built

This knowledge base was built through Human/AI collaboration using Claude (Anthropic). The process:

1. **Research** — Deep research reports (Perplexity Pro) covering the full venue operations landscape across 26 domains, generating 500+ citations
2. **Methodology** — Formal data science methodology (Q1-Q5) locked before any processing: classification framework, relationship taxonomy, quantification approach, completeness criteria, transparency documentation (EU AI Act aligned)
3. **Extraction** — Claude Code processed each research report through a five-stage intake pipeline (Receive, Register, Rinse, Ready, Route), extracting distinct operational concepts, standards, technologies, organizations, and people
4. **Structuring** — Each concept became a structured markdown note with YAML frontmatter, cross-links using 7 relationship types, cross-cutting dimensions (venue type, scale, delivery model, jurisdiction), and source citations
5. **Validation** — Every note validated against 34 pre-write checks (schema, vocabulary, terminology, content, link integrity). Three-layer provenance chain maintained.
6. **Linking** — Cross-domain relationships mapped using 7 relationship types. Orphan detection. Maps of Content generated. Progressive deepening across multiple sessions.

Full methodology (public statement): `METHODOLOGY.md` at vault root.
Internal methodology: `Reference/VEP-KB-Data-Science-Methodology_v1.0.md`.
Pipeline documentation: `_Pipeline/` folder.

## Current Status — v1.0.0 (2026-04-06)

| Metric | Value |
|---|:-:|
| Total notes | 650 |
| Domain overviews | 26 / 26 (100%) |
| Concept notes | 207 |
| Source notes | 390 |
| Domain MOCs (navigation layer) | 27 |
| Audit reports filed | 7 (A-01 through A-07) |
| Delta register entries | 20 (all resolved or accepted) |
| Domains at minimum viable (3+ concepts) | 26 / 26 (100%) |
| Domains at working depth (8+ concepts) | 10 / 26 (38%) |
| Domains at authoritative (15+ concepts) | 1 / 26 (4%) |
| Confidence distribution | 88.4% high, 10.6% medium, 1.0% low |
| Fabrication incidents | 0 across 21 sessions |
| Processing sessions | 21 (S4-S21, March-April 2026) |

**Academic Rigor Initiative (Phase B.5) complete** — 7 audit threads (provenance, vocabulary, citation, traceability, structural consistency, confidence defensibility, final validation), 20 delta register entries resolved. Reports in `_Pipeline/Validation/`.

**Depth-of-coverage improvement areas** (documented for post-v1.0 enrichment):
- 15 domains at minimum viable depth — candidates for deepening to working depth (8+ concepts)
- Non-concept note types (Standards, Technology, Organizations, People) at 0 — enrichment scheduled post-v1.0
- All notes at `status: draft` — human review passes scheduled for draft to reviewed to canonical progression
- 31 concepts across 4 accepted delta entries identified for supplementary source enrichment
- Parking-and-transportation has highest medium-confidence concentration (4/10 concepts)
- Logistics-and-warehouse at minimum viable floor (3 concepts)

See `METHODOLOGY.md` for the full limitations disclosure and `RELEASE-v1.0.0.md` for release details.

## AI Disclosure

This knowledge base was developed through Human/AI collaboration using Claude (Anthropic, Opus 4.6). The methodology (EU AI Act aligned transparency), confidence distribution, limitations, and reproducibility guidance are published in `METHODOLOGY.md`. Alex Jackson (Principal, Experience Innovation Inc.) holds human accountability for all content, methodology decisions, and strategic direction.

## Recommended Obsidian Plugins

| Plugin | Purpose |
|--------|---------|
| Dataview | Complex queries and relationship views |
| Bases (core) | Fast table views of frontmatter properties |

## License

This is an open educational resource. Source citations are provided for all factual content. Please respect the original sources' terms of use.

## Contact

Alex Jackson — [Experience Innovation Inc.](https://experienceinnovation.consulting)
Venue Excellence Podcast — launching 2026

---

*Built with care for the venue operations community.*
