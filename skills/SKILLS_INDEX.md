# Public Skills Index

This folder publishes a cleaned, selective view of the agent-assisted workflow used in the private research repository. It is not the full internal skill library.

The purpose of the public `skills/` surface is to make three things legible to external readers:

1. what different workflow skills are responsible for in the research system;
2. what remains under direct human researcher / orchestrator control;
3. what structured outputs make the workflow reproducible and auditable.

## Publication Boundary

Included here:

- high-level workflow structure;
- the role of skills in project management, deterministic cleaning, data integration, and release audit;
- two cleaned exemplar `SKILL.md` files that show workflow logic without exposing private assets.

Not included here:

- skills tightly bound to private data boundaries or manual browser-authenticated intake;
- project-specific prompt files and low-signal orchestration assets;
- messy internal runtime notes, path-dependent helper files, or anything that would leak private workflow surfaces.

## How To Read This Folder

- Each public `SKILL.md` is a cleaned exemplar, not a verbatim copy of the private repository file.
- Internal pathing, prompt fragments, adjudication details, and private-data handling steps have been reduced or generalized.
- The public repo exposes workflow roles and audit logic, not the entire operational stack.

## Workflow Map

| Workflow layer | What the skills do | What remains under human researcher control | Typical outputs |
|---|---|---|---|
| Project scaffold and governance | Define repository structure, version conventions, release boundaries, and workflow handoffs | Set scope, approve governance rules, decide what can enter the public release | layout specs, conventions, manifests, release boundary notes |
| Deterministic cleaning | Transform transcript snapshots into stable segment-level analysis inputs using traceable rules | Approve exclusion logic, inspect edge cases, freeze the version used downstream | cleaned segment files, cleaning logs, retention diagnostics |
| Data integration | Align metadata, cleaned text, schema, linkage, and derived variables into analyzable tables | Review ambiguous joins, approve adjudications, sign off frozen analysis tables | schema documentation, merged tables, engineering reports |
| Validation and audit | Check measurement quality, selection threats, robustness, and data lineage | Interpret failures, decide whether claims must narrow, approve sensitivity reporting | validation reports, selection audits, robustness matrices |
| Replication and release | Package shareable materials and write release-facing provenance | Approve public/private boundary, sign off on release packaging and disclosure language | provenance logs, appendices, package README, release manifests |

## Human Researcher As Orchestrator

The workflow is agent-assisted, not researcher-replaced. In this project the human researcher remains responsible for:

- defining the research question, theoretical scope, and admissible claims;
- deciding which steps may be automated and which require manual adjudication;
- freezing versions, thresholds, and release boundaries;
- approving what is public, what stays private, and what is excluded on ethics or terms-of-use grounds;
- interpreting robustness, narrowing claims when needed, and writing the final paper-facing conclusions.

In other words, the skills structure execution and documentation, but the researcher retains responsibility for theory, scope, evidence standards, and public release decisions.

## Public Exemplar Skills

This public repo currently exposes two cleaned exemplar skills:

- `data-cleaning-pipeline/`: shows how deterministic cleaning is made structured, replayable, and auditable.
- `provenance-writer/`: shows how data lineage, appendix documentation, and release audit trails are formalized.

These two were chosen because they demonstrate the workflow clearly without exposing private intake boundaries, browser-authenticated steps, or prompt-heavy internal assets.

## Relationship To The Released Replication Package

The runnable public reproduction surface is still `replication_package/`.

The purpose of `skills/` is different:

- `replication_package/` tells a replicator how to rerun the released public materials;
- `skills/` explains how agent-assisted workflow was embedded upstream in project management, cleaning, documentation, and audit.

Together they show not only the released outputs, but also the workflow logic that produced those outputs.

## Publicly Summarized But Not Fully Published

Some workflow layers are described here at a high level but are not published as raw `SKILL.md` files in this repo. That includes, for example:

- private-data-bound archive intake;
- linkage and timeline construction steps tied to manual review and source conflicts;
- low-level internal orchestration and prompt-heavy measurement assets.

That boundary is intentional. The goal of this public folder is explanatory clarity, not full operational disclosure.