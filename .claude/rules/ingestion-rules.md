# Research Ingestion Rules
**Version:** 2.0 (Session 10 — aligned with 26-domain taxonomy, Q3-Q5 methodology, GLRC transparency)
**Reference:** VEP-KB-Data-Science-Methodology_v1.0.md, VOCABULARY.yaml, SCHEMA.yaml

## Five-Stage Intake Pipeline

### Stage 1: Receive
- DR output files placed in `_Pipeline/Input/`
- Register in `pipeline-state.json` with filename, research_batch ID, word count, date received

### Stage 2: Register
- Read full research file
- Log in progress.md: file received, batch ID, estimated concept count
- Check for duplicate content against existing source notes (dedup before processing)

### Stage 3: Rinse
- Strip marketing language, vendor sales claims, speculative predictions
- Flag any content specific to a single named venue's internal operations (CS exemplar policy)
- Identify all distinct concepts, standards, technologies, organizations, and people
- Note all source URLs cited in the research

### Stage 4: Ready
- Map each identified concept to its primary domain (from 26-domain taxonomy)
- Assign initial confidence tier (Q3): high / medium / low
- Create extraction manifest: list of notes to create with type, domain, sources, confidence
- **GATE: Validate manifest against VOCABULARY.yaml before proceeding to Stage 5**

### Stage 5: Route
- Execute note creation per the Processing Workflow below
- Route notes to correct folders by note_type
- Update pipeline-state.json with processing results

## Processing Workflow (per note)

### Step 1: Create Note
- Use the appropriate template from `Templates/`
- Write to the correct folder based on note_type:
  - `domain` and `concept` → `01_Domains/{domain-slug}/`
  - `standard` → `02_Standards/`
  - `technology` → `03_Technology/`
  - `organization` → `04_Organizations/`
  - `person` → `05_People/`
  - `source` → `06_Sources/`
  - `map` → `07_MOCs/`

### Step 2: Populate Frontmatter
- All universal required fields (title, note_type, status, created, updated, tags, ai_disclosure)
- All type-specific required fields per SCHEMA.yaml
- Relationship links using underscore-separated keys (parent_of, child_of, implements, governed_by, supported_by, varies_by, scales_with)
- Cross-cutting dimensions where applicable (venue_type, venue_scale, delivery_model, jurisdiction)
- GLRC transparency fields: extraction_model, research_batch

### Step 3: Create Source Notes
- For every URL cited in the research, create a corresponding note in `06_Sources/`
- Use filename pattern: `Source-NNNN-short-description.md`
- Source numbering is sequential across the entire vault (check existing sources first)
- Required: source_type, url, accessed date, description

### Step 4: Cross-Link
- Every concept note links to its parent domain overview (child_of)
- Every concept note links to its source notes (sources)
- Related concepts across domains get bidirectional `related_to` wikilinks
- Standards link to concepts they govern (governed_by / implements)
- Technologies link to concepts they support (supported_by / supports)
- Use relationship types from Decision #31 — no ad hoc relationship names

### Step 5: Validate
- Run schema validation on all created notes (per validation-rules.md)
- Check all controlled fields against VOCABULARY.yaml
- Verify no orphan notes
- Write validation report to `_Pipeline/Validation/batch-{id}-validation.md`

### Step 6: Log
- Update progress.md with: notes created, enriched, failed, skipped
- Update pipeline-state.json with batch completion status
- Log any failed approaches (prevents rework in subsequent sessions)

## File Naming Conventions

| Note Type | Pattern | Example |
|-----------|---------|---------|
| domain | `Domain-{domain-slug}.md` | `Domain-Food-and-Beverage.md` |
| concept | `{Domain-Slug}-{Concept-Name}.md` | `Food-and-Beverage-Kitchen-Operations.md` |
| standard | `Std-{standard-id}.md` | `Std-NFPA-101.md` |
| technology | `Tech-{platform-name}.md` | `Tech-Momentus-Technologies.md` |
| organization | `Org-{org-name}.md` | `Org-IAVM.md` |
| person | `Person-{full-name}.md` | `Person-Russ-Simons.md` |
| source | `Source-{NNNN}-{short-desc}.md` | `Source-0001-IAVM-Crowd-Management.md` |
| map | `Map-{scope}.md` | `Map-Venue-Operations-Ecosystem.md` |

## Deduplication

Before creating any note, check if a note with the same concept already exists:
1. Search by filename pattern
2. Search by `title` in frontmatter
3. If duplicate found: enrich the existing note with new information and sources rather than creating a new one
4. Track enrichments in progress.md

## What NOT to Extract

- Marketing claims or vendor sales language — strip and keep factual content only
- Speculative future predictions without evidence
- Content specific to a single named venue's internal operations (CS exemplar policy: tag with `cs_exemplar: true` if CS-specific, flag for Greg approval)
- Pricing or commercial terms for specific products
- Personal opinions from research authors (unless attributed as expert perspective)
- Any reference to Vivid Array, EXi clients, or EXi internal operations

## GLRC Provenance Requirements

Every note created through this pipeline carries a complete provenance chain:
1. **ai_disclosure** — "Extracted by [model] from deep research output. Human-reviewed by [name]."
2. **research_batch** — maps to specific DR prompt in Research Plan v2.0
3. **sources** — wikilinks to Source notes with original URLs
4. **extraction_model** — specific model from VOCABULARY.yaml
5. **Session audit** — progress.md logs processing lineage per session
