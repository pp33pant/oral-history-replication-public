# provenance-writer

This is a cleaned public-facing version of an internal workflow skill. It is published to show how data lineage, release documentation, and audit trails were formalized without exposing private workflow surfaces.

**Phase**: Replication And Release Audit

---

## Goal

Document the provenance of released materials: where inputs came from, how they were transformed, which versions were frozen, and what was included or excluded from the public release.

---

## Inputs

- raw-source manifests or intake summaries;
- processed data files and model outputs intended for release;
- release-facing documentation such as README files, appendix notes, and package manifests.

---

## Outputs

- provenance log or lineage file;
- release-facing data appendix;
- transformation summary;
- public/private boundary notes;
- execution or release audit log.

---

## What The Human Researcher Controls

1. Confirms which sources and transformations belong in the release lineage.
2. Approves the public/private boundary and any redactions.
3. Signs off the version freeze used for release.
4. Decides whether the resulting audit supports the claims made in the paper and release notes.

---

## Steps

1. Trace each released artifact back to its immediate upstream source.
2. Check that the lineage has no unexplained gaps between source, transformation, and released output.
3. Summarize the released dataset, release scope, and access conditions in short appendix-style notes.
4. Record version identifiers, hashes, or manifests needed to distinguish one frozen release from another.
5. Write an execution log showing which workflow stages were run, what they consumed, and what they produced.
6. Cross-check that release-facing documentation matches the actual files included in the public package.

---

## Validation

- every primary released artifact has a documented upstream lineage;
- public/private boundaries are stated explicitly;
- release documentation is consistent with the actual shipped files;
- version identifiers and hashes are recorded where needed for auditability;
- the release log is sufficient for an external reader to understand how the public package was assembled.

---

## Why This Matters

Agent-assisted workflow is only useful for scholarly release if it leaves an inspection trail. Provenance writing turns hidden execution history into explicit documentation that reviewers and replicators can examine.

---

## Notes

- This public file is a cleaned exemplar rather than a verbatim internal release script.
- Internal appendices, project-specific paths, and prompt-heavy runtime details are intentionally omitted.
- In this public repo, the provenance role connects the workflow explanation in `skills/SKILLS_INDEX.md` to the runnable release surface in `replication_package/`.