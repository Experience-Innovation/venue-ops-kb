# Validation Rules
**Version:** 2.0 (Session 10 — aligned with 26-domain taxonomy, Q3-Q5 methodology, GLRC transparency)
**Reference:** VEP-KB-Data-Science-Methodology_v1.0.md, VOCABULARY.yaml, SCHEMA.yaml

## Pre-Write Validation (MUST pass before any note is written to vault)

### Schema Check
1. All `required` fields for the note's `note_type` are present (per SCHEMA.yaml)
2. All `universal` required fields are present
3. No unknown fields that aren't in `required` or `optional` for that type

### Vocabulary Check
4. `note_type` value exists in VOCABULARY.yaml `note_type` list
5. `status` value exists in VOCABULARY.yaml `status` list (draft | reviewed | canonical | archived)
6. `domain` value(s) exist in VOCABULARY.yaml `domain` list (26 domains)
7. `venue_types` values exist in VOCABULARY.yaml `venue_type` list (11 types)
8. `venue_scale` values exist in VOCABULARY.yaml `venue_scale` list (4 tiers)
9. `delivery_model` values exist in VOCABULARY.yaml `delivery_model` list (3 models)
10. `jurisdiction` values exist in VOCABULARY.yaml `jurisdiction` list (5 categories)
11. `vef_alignment` values exist in VOCABULARY.yaml `vef_alignment` list (9 values)
12. `confidence` value exists in VOCABULARY.yaml `confidence` list (high | medium | low)
13. `research_batch` value exists in VOCABULARY.yaml `research_batch` list
14. `source_type` value exists in VOCABULARY.yaml `source_type` list
15. `extraction_model` value exists in VOCABULARY.yaml `extraction_model` list
16. All relationship type keys are from Decision #31: parent_of, child_of, implements, governed_by, supported_by, related_to, varies_by, scales_with

### Format Check
17. Wikilinks in frontmatter are quoted: `"[[Note Name]]"` not `[[Note Name]]`
18. Dates are YYYY-MM-DD format
19. Lists use YAML list syntax (dash + space)
20. `title` matches the H1 heading in the body
21. Filename follows naming convention (per ingestion-rules.md)
22. Relationship keys use underscores (parent_of) not hyphens (parent-of)

### Content Check
23. `sources` field is not empty — every concept must cite at least one source
24. `description` is present and between 1-3 sentences
25. Body content exists below the frontmatter (not just a heading)
26. No references to Calgary Stampede, BMO Centre, EXi clients, or Vivid Array in body text
27. No fabricated data — every factual claim in the body has a source citation
28. `ai_disclosure` field is present and non-empty (GLRC Q5 requirement)

### Terminology Check (Hook-Enforced)
29. "Operational Excellence" is permitted as standard industry terminology (Decision #45, Session 14). The restriction applies ONLY in CS/BMO Centre engagement context (VEP-Client repo). No scan required in this KB.
30. No occurrence of "Vivid Array" or Vivid-related terms
31. No occurrence of old domain slugs (core-operations, emergency-management-and-life-safety, it-and-av-infrastructure, premium-and-vip-operations, data-systems-intelligence, supply-chain-logistics)

### Link Integrity Check
32. Every wikilink in frontmatter points to a note that exists OR is being created in this batch
33. Parent domain overview exists before creating concept notes under it
34. Source notes exist before referencing them in concept notes

## Post-Batch Validation

Run after all notes in a batch are written:

### Orphan Detection
```dataview
LIST FROM "01_Domains" OR "02_Standards" OR "03_Technology" OR "04_Organizations" OR "05_People"
WHERE length(file.inlinks) = 0
```

### Missing Sources
```dataview
LIST FROM "01_Domains" WHERE !sources OR length(sources) = 0
```

### Missing AI Disclosure
```dataview
LIST FROM "01_Domains" OR "02_Standards" OR "03_Technology" OR "04_Organizations" OR "05_People"
WHERE !ai_disclosure OR ai_disclosure = ""
```

### Domain Coverage (Q4 Completeness)
For each of the 26 domains in VOCABULARY.yaml:
- Count concept notes → check against minimum viable threshold (3+)
- Count unique sources → check diversity threshold (2+)
- Count relationship links → check density threshold (1+)
- Flag any domain with 0 concepts after its research batch is processed

### Relationship Density
```dataview
TABLE
  length(filter(file.frontmatter, (k) => contains(["parent_of","child_of","implements","governed_by","supported_by","related_to","varies_by","scales_with"], k))) as "Relationship Count"
FROM "01_Domains"
SORT file.name ASC
```

### Confidence Distribution
```dataview
TABLE confidence, length(rows) as "Count"
FROM "01_Domains"
WHERE note_type = "concept"
GROUP BY confidence
```

## Validation Report Format

Write to `_Pipeline/Validation/batch-{id}-validation.md`:

```markdown
# Validation Report: Batch {id}
**Date:** {YYYY-MM-DD}
**Research Batch:** {batch-id from VOCABULARY.yaml}
**Extraction Model:** {model used}
**Notes Created:** {count}
**Notes Enriched:** {count}
**Source Notes Created:** {count}

## Schema Violations
{list or "None"}

## Vocabulary Violations
{list or "None"}

## Terminology Violations
{list or "None — scanner passed"}

## GLRC Compliance
- AI Disclosure present on all notes: {yes/no}
- Research batch tagged: {yes/no}
- Extraction model recorded: {yes/no}
- Source provenance complete: {yes/no}

## Orphan Notes
{list or "None"}

## Missing Sources
{list or "None"}

## Domain Coverage (Q4 Thresholds)
| Domain | Concept Count | Source Count | Rel Density | Threshold |
|--------|--------------|-------------|-------------|-----------|
{table — flag domains below minimum viable}

## Confidence Distribution
| Tier | Count | % |
|------|-------|---|
{table}

## Summary
{pass/fail with details}
```

## Validation Report Types and Policies

Two distinct report types exist in `_Pipeline/Validation/`. Each follows different conventions:

### Batch Validation Reports
- **When:** After processing an extraction batch (Stage 5 Route output)
- **Template:** Use the Validation Report Format above (no YAML frontmatter — metadata captured in body)
- **Naming:** `batch-{id}-{description}-validation.md`
- **Required for:** Every extraction session that creates or enriches content notes
- **Frontmatter:** NOT required. Batch reports capture pass/fail in the Summary section body text. The `audit_outcome:` field requirement (CLAUDE.md v2.1) applies to audit reports, not batch reports.

### Audit Reports
- **When:** Systematic quality audits (academic rigor, CI audits, final validation passes)
- **Template:** See `.claude/rules/audit-report-template.md` (to be created D2)
- **Naming:** `audit-{id}-{description}.md` or `ci-audit-{phase}-{description}.md`
- **Frontmatter:** REQUIRED — must include `audit_outcome:` and `lifecycle:` fields per CLAUDE.md v2.1 governance artifact conventions
- **Canonical frontmatter pattern:** title, audit_outcome, lifecycle, created, scope, methodology

### Consolidated Reports Policy
- **Per-batch reports** are required for extraction sessions (creating content notes from DR input)
- **Consolidated reports** are acceptable when a session performs an audit or validation sweep across the full vault (not tied to a single extraction batch)
- **Hybrid sessions** (e.g., S18 CI/enrichment) may use either pattern; the audit-style frontmatter pattern is preferred for sessions that combine audit + extraction work
- **Root cause context:** S20 processed 5 DR batches but produced a consolidated A-06 audit report instead of per-batch reports (S20 OIR-6). This was acceptable because the session's primary function was confidence tier auditing, not extraction. This policy codifies that practice.
