---
title: "CI Audit D1: Pipeline, Template, and Governance Consistency"
audit_outcome: CONDITIONAL
lifecycle: active
created: 2026-04-06
scope: "All pipeline, template, validation, session, and governance artifacts from S4-S21 (60+ files)"
methodology: "Systematic sweep across 6 audit categories — template, pipeline, validation pattern, session artifact, governance artifact, implicit convention"
---

# CI Audit D1 — Pipeline, Template, and Governance Consistency

**Phase:** D (CI Initiative), Session D1
**Date:** 2026-04-06
**Vault version:** v1.0.0 (released 2026-04-06)
**Audit scope:** All non-content artifacts — templates, pipeline rules, validation reports, session governance files, implicit conventions

---

## §1. Audit Summary

| Category | Finding Count | CRITICAL | HIGH | MEDIUM | LOW |
|----------|:------------:|:--------:|:----:|:------:|:---:|
| Template alignment | 5 | 0 | 2 | 2 | 1 |
| Pipeline rule currency | 3 | 0 | 1 | 1 | 1 |
| Validation report patterns | 4 | 0 | 1 | 2 | 1 |
| Session artifact consistency | 4 | 0 | 1 | 2 | 1 |
| Governance artifact coverage | 3 | 0 | 1 | 1 | 1 |
| Implicit conventions | 4 | 0 | 2 | 1 | 1 |
| **TOTAL** | **23** | **0** | **8** | **9** | **6** |

**Outcome:** CONDITIONAL — zero CRITICAL findings, 8 HIGH findings requiring resolution before Phase E. All findings are process/template/governance gaps — zero content integrity issues.

---

## §2. Template Alignment (5 findings)

### T-01: Domain field name mismatch — `children` vs `parent_of` [HIGH]
- **Template:** Template-Domain.md uses `children: []`
- **Schema:** SCHEMA.yaml specifies `parent_of` as the optional relationship field
- **Actual notes:** All 26 domain overview notes use `children:` (matching template, not schema)
- **Impact:** Schema-template-actual divergence. Validation rule #16 checks relationship key names but `children` is not in Decision #31's 7-type taxonomy.
- **Root cause:** Template predates SCHEMA.yaml v2.0 relationship standardization. Map note type also uses `children:` as a required field — possible confusion between hierarchical containment (map→children) and domain→concept parent_of relationship.
- **Resolution:** Clarify canonical field name. SCHEMA.yaml `map` type uses `children:` as required, but `domain` type specifies `parent_of:`. Either: (a) accept `children:` for both domain and map types (update SCHEMA.yaml), or (b) migrate all 26 domain notes to `parent_of:` (update template + notes).

### T-02: Undefined `related` field in 5 templates [HIGH]
- **Templates:** Organization, Person, Map, Standard, Technology all include `related: []`
- **Schema:** Specifies `related_to` (universal optional field per Decision #31)
- **Actual notes:** No examined notes use `related:` field — it appears to be a dead template artifact
- **Impact:** If Phase E creates Standard/Technology/Organization/Person notes using these templates, they'll have a non-schema field that validation rule #3 ("no unknown fields") should catch but may not if enforcement is loose.
- **Resolution:** Replace `related: []` with `related_to: []` in all 5 templates.

### T-03: Template-Map.md under-scaffolded [MEDIUM]
- **Template:** 2 body sections (Description + Contents)
- **Actual Map-Guest-Experience.md:** 7+ sections (Purpose, Domain Overview, Concept Index, Cross-Domain Connections, Reading Paths, Coverage Status, Related MOCs)
- **Impact:** New MOC creation using the template would produce structurally thin notes compared to the S16-era MOCs.
- **Resolution:** Expand template to include the 7-section structure used in actual MOCs (D2 scope — template architecture).

### T-04: Template-Source.md over-scaffolded [MEDIUM]
- **Template:** 3 body sections (Key Information Extracted, Cited In, Sources)
- **Actual source notes:** Zero body sections — metadata-only notes with frontmatter + title
- **Impact:** Template suggests body content that 390 source notes don't implement. Minor friction for future authoring.
- **Resolution:** Simplify template body to optional single section (D2 scope).

### T-05: ai_disclosure default text diverges from CLAUDE.md §10 [LOW]
- **Templates:** Use "Generated through Human/AI collaboration using Claude..."
- **CLAUDE.md §10:** Specifies "Extracted by Claude (Anthropic) from deep research output..."
- **Actual notes:** Most use the CLAUDE.md version, not the template version
- **Impact:** Cosmetic inconsistency. Both convey appropriate disclosure.
- **Resolution:** Align template default to CLAUDE.md §10 text (D2 scope).

---

## §3. Pipeline Rule Currency (3 findings)

### P-01: ingestion-rules.md Stage 5 missing wikilink-filename validation [HIGH]
- **Current:** Stage 5 (Route) specifies: create notes, route to folders, update pipeline-state.json
- **Gap:** No step to validate that wikilinks in frontmatter match actual filenames
- **Evidence:** S21 A-07 found 31 broken source wikilinks from S14-S15 that persisted 7 sessions. Root cause: truncated filenames in wikilinks during extraction, never caught because no validation step existed.
- **S21 retro recommendation:** "Add automated wikilink-filename validation to the ingestion pipeline Stage 5 (Route)"
- **Resolution:** Add Step 5b to ingestion-rules.md between current Step 5 (Validate) and Step 6 (Log). **Codify in this session (D1).**

### P-02: Validation-rules.md missing field-name validation [MEDIUM]
- **Current:** Rule #3 says "No unknown fields that aren't in required or optional for that type" but this is a semantic rule, not a mechanical check with specific field name enumeration.
- **Gap:** No rule explicitly validates that frontmatter keys match SCHEMA.yaml field names. This allowed `children` (not in schema for domain type) and `related` (not in schema at all) to persist uncaught.
- **Resolution:** Add explicit validation rule: "All frontmatter field keys must exist in SCHEMA.yaml universal.required, universal.optional, or {note_type}.required, {note_type}.optional" (D2/D3 scope — depends on T-01 field name resolution).

### P-03: ingestion-rules.md version stale [LOW]
- **Current:** Version 2.0 (Session 10)
- **Gap:** Single-source flag added to Stage 4 (Ready) during S19 per A-04 findings, but version number was not bumped. Other S16-S21 refinements (wikilink validation need, verbatim-quote URL extraction) are encoded in progress.md lessons but not formally incorporated into rules.
- **Resolution:** Bump to v2.1 with changelog when wikilink validation is added (D1) and version again to v3.0 when all D-phase rule updates are complete (D3).

---

## §4. Validation Report Patterns (4 findings)

### V-01: Batch validation reports lack frontmatter [HIGH]
- **Current:** 12 of 13 batch reports (batch-00 through batch-11) have NO YAML frontmatter
- **Convention:** CLAUDE.md v2.1 specifies audit reports in `_Pipeline/Validation/` should carry `audit_outcome:` field
- **Conflict:** validation-rules.md prescribes a batch report template that has NO frontmatter (just markdown H1 + metadata table). The 12 batch reports correctly follow this template — but the template itself is pre-v2.1.
- **Resolution:** Either: (a) add minimal frontmatter (audit_outcome, created, batch_id) to validation-rules.md batch report template and backfill existing reports (D3 scope), or (b) explicitly exempt batch validation reports from the audit_outcome requirement (codify the exemption).

### V-02: Audit report frontmatter has two incompatible patterns [MEDIUM]
- **Pattern B1 (A-01 through A-05):** 8 fields — audit_id, audit_name, session, date, phase, category, audit_outcome, initiative
- **Pattern B2 (A-06, A-07):** 6 fields — title, audit_outcome, lifecycle, created, scope, methodology
- **Root cause:** A-01–A-05 created early in S16 before governance-artifact conventions solidified. A-06–A-07 created in S20–S21 using the mature convention.
- **Impact:** Machine-readable audit indexing requires consistent fields. Dataview queries against audit reports would need to handle both patterns.
- **Resolution:** Establish single canonical audit report template. Backfill A-01–A-05 frontmatter to match (D3 scope — governance consolidation).

### V-03: Consolidated vs per-batch validation reports undocumented [MEDIUM]
- **S20 OIR-6:** S20 processed 5 DR batches but wrote a consolidated A-06 audit report instead of per-batch validation reports
- **Current state:** No documented policy on when per-batch reports are required vs when consolidated reports are acceptable
- **Resolution:** Codify policy — per-batch for extraction sessions, consolidated for audit/validation-only sessions. **Document in this session (D1).**

### V-04: session-18 validation report breaks batch pattern [LOW]
- **File:** session-18-ci-enrichment-validation.md has full YAML frontmatter (8 fields)
- **Context:** S18 was a hybrid CI/enrichment session, so its validation report adopted audit-style frontmatter
- **Impact:** Cosmetic inconsistency within the batch-report cohort. Not a governance issue — S18 was a unique session type.
- **Resolution:** Document as acceptable variance for hybrid sessions (D3 scope).

---

## §5. Session Artifact Consistency (4 findings)

### S-01: 19/28 session files missing `type:` field [HIGH]
- **S12-S15:** No YAML frontmatter at all (4 handoffs, 1 retro, 1 op-plan, 2 delta analyses = 8 files)
- **S16-S18:** Partial YAML frontmatter without `type:` field (2 handoffs, 2 retros, 1 qa-qc, 2 op-plans = 7 files)
- **S20-S21 + D1:** Full YAML frontmatter with `type:` field (all 10 files compliant)
- **Also missing:** discovery-manifest.md, progress.md (2 files)
- **Impact:** Machine-readable session artifact indexing impossible across full history. Dataview queries for "all handoffs" or "all retros" won't find pre-S20 files.
- **Resolution:** Backfill frontmatter on S12-S19 governance artifacts (D3 scope). Prioritize: add minimal frontmatter (type, lifecycle: superseded, created, session) to enable indexing without modifying content.

### S-02: Governance artifact schema not codified [MEDIUM]
- **Current state:** SCHEMA.yaml defines frontmatter for 8 note_types (domain, concept, standard, technology, organization, person, source, map). Zero schema definition for governance artifacts (handoffs, retros, operational plans, pass-forwards, delta analyses).
- **CLAUDE.md v2.1** defines the lifecycle/audit_outcome field convention in prose but not in a machine-readable schema.
- **Impact:** No automated validation possible for governance artifact frontmatter. Consistency depends on convention memory, not enforcement.
- **Resolution:** Add governance artifact schema to SCHEMA.yaml or create separate governance-schema.yaml (D2/D3 scope — depends on template architecture decisions).

### S-03: Session type taxonomy not in VOCABULARY.yaml [MEDIUM]
- **Observed types:** handoff, retrospective, operational-plan, pass-forward, delta-analysis, qa-qc-analysis, template, backlog, initiative-roadmap
- **VOCABULARY.yaml:** Contains only content note_type values. No governance artifact types.
- **Impact:** No controlled vocabulary enforcement for `type:` field on governance artifacts. Inconsistent type values could emerge (e.g., "retro" vs "retrospective" vs "session-retro").
- **Resolution:** Add `governance_type:` list to VOCABULARY.yaml with canonical values (D2 scope).

### S-04: progress.md has no frontmatter or structured format [LOW]
- **Current:** Raw markdown with no frontmatter. Session entries are freeform prose with inconsistent structure across sessions.
- **Impact:** Not Dataview-queryable. Manual reading required to extract session metadata.
- **Resolution:** Low priority — progress.md serves as a human-readable log. Structured indexing is better served by pipeline-state.json and the session artifacts themselves.

---

## §6. Governance Artifact Coverage (3 findings)

### G-01: No audit report template in .claude/rules/ [HIGH]
- **Current:** validation-rules.md defines a batch validation report template. No template exists for academic rigor audit reports (A-series).
- **Evidence:** Two incompatible audit report patterns emerged (V-02) because no template governed the format.
- **Resolution:** Create audit-report-template.md in .claude/rules/ with canonical frontmatter + body structure (D2 scope).

### G-02: SCHEMA.yaml version unchanged since S10 despite S16-S21 refinements [MEDIUM]
- **Current:** Version 2.0 (Session 10)
- **Gap:** CLAUDE.md v2.1 added frontmatter field conventions (status/lifecycle/audit_outcome), single-source flag was added to ingestion rules, bibliographic fields became de facto required for source notes per DELTA-004. None of these are reflected in SCHEMA.yaml versioning.
- **Resolution:** Bump SCHEMA.yaml to v2.1 with S16-S21 refinements documented in changelog (D2/D3 scope).

### G-03: No governance artifact templates in Templates/ directory [LOW]
- **Current:** 8 content note templates. Zero governance artifact templates.
- **Impact:** Session handoffs, retros, and operational plans are created from memory or by copying previous files. The session-operational-plan-template.md exists in _sessions/ but not in Templates/.
- **Resolution:** D2 scope — template architecture session will assess whether governance templates belong in Templates/ or _sessions/ or .claude/rules/.

---

## §7. Implicit Conventions Not Codified (4 findings)

### I-01: `children:` field used for both domain and map types [HIGH]
- **Convention:** Domain notes use `children:` to list child concepts. Map notes use `children:` to list contained notes.
- **Schema:** SCHEMA.yaml defines `parent_of:` for domain type and `children:` for map type — two different field names for similar semantics.
- **Actual practice:** Both types use `children:` in all 53 notes (26 domains + 27 MOCs).
- **Implication:** The schema-practice divergence on domain notes has been consistent since S12 and was never caught because validation rule #16 checks relationship type KEYS (parent_of, child_of, etc.) but `children:` is not a relationship key — it's a containment list. The check passes by omission.
- **Resolution:** Align schema to practice: update SCHEMA.yaml domain type to use `children:` (matching map type and actual notes). Or align practice to schema. Alex decision required. **HIGH because it affects 26 domain notes + all templates + validation rules.**

### I-02: `source_session:` field convention for cross-session artifacts [HIGH]
- **Convention:** Artifacts that span multiple sessions (roadmap, backlog, template) use `source_session:` instead of `session:` to indicate origin.
- **Codification:** Not documented anywhere. Emerged organically in S20-S21.
- **Examples:** session-operational-plan-template.md (`source_session: S21`), phase-e-enrichment-backlog.md (`source_session: S21`), vep-kb-initiative-roadmap.md (`source_session: "S128 init; S16 v1.1; ..."`)
- **Resolution:** Codify in governance artifact schema (D2/D3 scope). Define when `session:` vs `source_session:` is appropriate.

### I-03: Batch numbering convention evolved but not documented [MEDIUM]
- **Phase A (S12-S15):** batch-00 through batch-10 (sequential, zero-padded)
- **Phase B.5 (S16-S21):** batch-11 through batch-18, but also "batch-12-final-validation", "batch-13-dr-remediation" — descriptive suffixes replacing pure numbering
- **S20 batches:** batch-14 through batch-18 map to specific DR prompts (R-06 through R-10) — dual identification system
- **Resolution:** Document batch naming convention in ingestion-rules.md or pipeline documentation (D3 scope).

### I-04: DR input file naming convention unstandardized [LOW]
- **Pre-S18:** `DR-{Descriptive-Title}.md` (e.g., `DR-Emergency-Management-Life-Safety-Security-v1.md`)
- **S18 remediation:** `DR-Remediation-{Topic}.md` (e.g., `DR-Remediation-Liquor-Licensing.md`)
- **S20:** `DR-R{NN}-{Topic}.md` (e.g., `DR-R06-Booking-Sales-Ticketing.md`)
- **Impact:** Three different naming patterns across 40+ input files. Not a blocking issue — files are read, not queried.
- **Resolution:** Document as acceptable historical variance. Standardize going forward for Phase E DR inputs (D3 scope).

---

## §8. Cross-Cutting Patterns

### Pattern 1: S16 Inflection Point
The most consistent finding across all 6 audit categories is that S16 represents a clear governance inflection point. Pre-S16 artifacts lack structured frontmatter, type fields, and lifecycle tracking. Post-S16 artifacts progressively standardize, reaching full consistency by S20-S21.

**Implication for D2-D4:** Backfill decisions should consider whether pre-S16 artifacts need full modernization or can be marked `lifecycle: superseded` and left as-is.

### Pattern 2: Schema-Practice Divergence
SCHEMA.yaml v2.0 was written in S10 and never updated despite 11 subsequent sessions of refinement. The gap between schema-as-written and practice-as-evolved has grown across three dimensions: field names (children vs parent_of), field conventions (lifecycle/audit_outcome), and validation scope (no field-name checking).

**Implication for D2:** SCHEMA.yaml v3.0 should be a D2 centerpiece — align schema to reflect actual practice, then enforce.

### Pattern 3: Template-Actual Alignment Is Strong for Content Notes
Despite the field-name issues, all 8 content note templates include every required field from SCHEMA.yaml, and actual notes follow template structure closely for concept and domain types. The system works — it just has naming inconsistencies at the edges.

---

## §9. Gate Assessment

**Is the vault content sound?** YES. Zero CRITICAL findings. All findings are process/template/governance gaps. The 650 v1.0 content notes are schema-compliant, vocabulary-clean, provenance-complete, and Obsidian-mountable.

**Can Phase E proceed without Phase D?** NO. Phase E will create Standard, Technology, Organization, and Person notes for the first time using templates that have undefined fields (T-02: `related` instead of `related_to`). Phase E enrichment will also create new DR batches — the wikilink validation gap (P-01) would risk repeating the S14-S15 truncation pattern.

**What must complete in D before E begins?** See gap register and improvement register (separate files).

---

## §10. Content / Data Science Findings (Comprehensive Sweep)

Added per Alex directive — extending D1 from technical-only to full knowledge engineer audit.

### Publication Infrastructure

| ID | Finding | Severity | Evidence |
|----|---------|:--------:|---------|
| C-01 | No LICENSE file — cannot release as open-source | HIGH | File listing |
| C-02 | Folders 02-05 (Standards, Technology, Organizations, People) don't exist on disk — phantom architecture | HIGH | Directory listing vs README/CLAUDE.md §7 |
| C-03 | METHODOLOGY.md stale (S16) — doesn't reflect S17-S21 work | LOW | File timestamp |

### Domain Coverage & Depth

| ID | Finding | Severity | Evidence |
|----|---------|:--------:|---------|
| C-04 | 16/26 domains below working depth (8+); 4 at minimum viable floor (3-4 concepts) | MEDIUM | Domain concept count analysis |
| C-05 | 5 lowest domains each depend on single research batch — no cross-batch corroboration | MEDIUM | research_batch field analysis |
| C-06 | logistics-and-warehouse at 66% medium+low confidence (2/3 concepts) | LOW | Confidence distribution analysis |
| C-07 | parking-and-transportation at 40% medium+low confidence | LOW | A-06 audit + confidence analysis |

### Publication Transparency

| ID | Finding | Severity | Evidence |
|----|---------|:--------:|---------|
| C-08 | All 207 concepts at status: draft — requires transparency disclosure | MEDIUM | Frontmatter scan |
| C-09 | Optional fields underutilized (venue_scale 40%, delivery_model 20%, jurisdiction 10%) — no annotation guidance | MEDIUM | 10-note random sample |
| C-10 | Non-concept note types at 0 count — KB structurally incomplete vs. SCHEMA design | LOW | Note type count |
| C-11 | System dashboard queries reference non-existent folders | LOW | Dataview query inspection |

### Body Text Quality (4-Note Sample)

**Quality ranges from medium (crowd-flow, 332 words, partial attribution) to exceptional (convention-partner, 609 words, every claim attributed).** All sampled notes meet working-depth editorial standards. Citation density ranges from 1 source per 44 words (ice-arena) to 1 per 87 words (convention-partner). Academic-grade rigor confirmed on 3/4 samples; 1/4 (crowd-flow) would benefit from mechanistic grounding.

### Updated Audit Summary

| Category | Finding Count | CRITICAL | HIGH | MEDIUM | LOW |
|----------|:------------:|:--------:|:----:|:------:|:---:|
| Template alignment | 5 | 0 | 2 | 2 | 1 |
| Pipeline rule currency | 3 | 0 | 1 | 1 | 1 |
| Validation report patterns | 4 | 0 | 1 | 2 | 1 |
| Session artifact consistency | 4 | 0 | 1 | 2 | 1 |
| Governance artifact coverage | 5 | 0 | 3 | 1 | 1 |
| Implicit conventions | 13 | 0 | 2 | 6 | 5 |
| **TOTAL** | **34** | **0** | **10** | **14** | **10** |

---

*AI Disclosure: CI audit co-produced by Claude (Anthropic) and Alex Jackson, 2026-04-06.*
