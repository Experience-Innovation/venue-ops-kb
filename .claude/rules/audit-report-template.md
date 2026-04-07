# Audit Report Template
**Version:** 1.0 (Session D2)
**Purpose:** Canonical template for all audit reports in `_Pipeline/Validation/`
**Authority:** SCHEMA.yaml v3.0 governance_artifacts.audit-report, CLAUDE.md v2.1 §Frontmatter

## Frontmatter (Required)

```yaml
---
title: "{Audit Title — e.g., 'Audit A-08: Field-Name Compliance'}"
audit_outcome: {PASS | FAIL | CONDITIONAL | DEFERRED}
lifecycle: active
created: {YYYY-MM-DD}
scope: "{What was audited — files, domains, artifact types, counts}"
methodology: "{Brief methodology — systematic sweep, sampling, automated check, etc.}"
---
```

**Field definitions:**
- `title:` — Descriptive title including audit ID if applicable
- `audit_outcome:` — Final outcome (from VOCABULARY.yaml audit_outcome list)
- `lifecycle:` — Governance lifecycle status (from VOCABULARY.yaml lifecycle list)
- `created:` — Date of audit completion
- `scope:` — What was examined and at what granularity
- `methodology:` — How the audit was conducted

**Note:** Audit reports do NOT carry `type:` or `note_type:` fields. They are identified by the presence of `audit_outcome:` in frontmatter.

## Body Structure

```markdown
# {Audit Title}

**Phase:** {Phase identifier}
**Date:** {YYYY-MM-DD}
**Vault version:** {version or commit ref}
**Audit scope:** {detailed scope description}

---

## Summary

| Category | Finding Count | CRITICAL | HIGH | MEDIUM | LOW |
|----------|:------------:|:--------:|:----:|:------:|:---:|
| {category} | N | N | N | N | N |
| **TOTAL** | **N** | **N** | **N** | **N** | **N** |

**Outcome:** {PASS/FAIL/CONDITIONAL — brief rationale}

---

## Findings

### {Category 1}

#### {Finding ID}: {Finding Title} [{Severity}]
- **Evidence:** {what was observed}
- **Impact:** {why it matters}
- **Resolution:** {what to do about it}

{Repeat for each finding}

---

## Gate Assessment

{Is the gate cleared? What blocks? What's next?}

---

*AI Disclosure: Audit co-produced by Claude (Anthropic) and Alex Jackson, {date}.*
```

## Usage Notes

- **Naming convention:** `audit-{id}-{description}.md` or `ci-audit-{phase}-{description}.md`
- **Location:** `_Pipeline/Validation/`
- **Batch validation reports** use a different template (see validation-rules.md) and do NOT require this frontmatter
- **This template applies to:** systematic quality audits, academic rigor audits, CI audits, final validation passes
