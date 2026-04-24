# data-cleaning-pipeline

This is a cleaned public-facing version of an internal workflow skill. It is published to show how deterministic transcript cleaning was structured and audited in the research workflow without exposing private runtime assets.

**Phase**: Data Preparation

---

## Goal

Transform transcript snapshots into stable, analysis-ready segment files using deterministic rules, explicit logs, and replayable checks.

---

## Inputs

- transcript snapshots or transcript exports obtained under the source archive's public-access terms;
- basic interview or narrator metadata;
- stable segment or interview identifiers from the intake layer.

---

## Outputs

- cleaned segment file;
- analysis-ready segment table;
- cleaning log with reason-coded exclusions;
- retention diagnostics report.

---

## What The Human Researcher Controls

1. Defines which artifacts count as substantive speech versus removable noise.
2. Approves rule changes that would alter segment retention or boundary logic.
3. Reviews edge-case exclusions before a version is frozen.
4. Signs off the cleaned release used by downstream measurement or modeling.

---

## Steps

1. Normalize encoding, whitespace, and line breaks.
2. Preserve stable IDs and source offsets so cleaned outputs can be traced back to the intake layer.
3. Remove interviewer prompts and non-substantive artifacts with explicit, replayable rules.
4. Compute segment metrics such as word counts and quality flags.
5. Log exclusions with reason codes rather than silently dropping records.
6. Export cleaned segment outputs and sync counts across file and table representations.
7. Publish a short retention report summarizing what was kept, dropped, and why.

---

## Validation

- stable IDs remain unique after cleaning;
- no empty segments remain in the final output;
- every exclusion has a reason code;
- counts match across stored outputs;
- rerunning the same input produces the same or near-identical output.

---

## Why This Matters

This workflow makes the transition from archive material to analysis inputs inspectable. External readers can see where deterministic cleaning happened, what was excluded, and what audit trail remains.

---

## Notes

- This public file is documentation-first. It is meant to show workflow structure, not to expose every internal implementation detail.
- Private browser-assisted intake, project-specific pathing, and adjudication-bound assets are intentionally omitted here.
- In the released public repo, this skill should be read together with `skills/SKILLS_INDEX.md` and the replication-facing materials in `replication_package/`.