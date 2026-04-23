# Rubric Instrument v1

## Scope

This instrument codes candidate reflection segments on two analytically distinct axes:

- `what`: the substantive state-person relational injury being narrated
- `how`: the degree of narrative organization or disorganization in the telling

Reader shorthand for the `what` axis:

- `authority_schema_injury` = `failed protector`
- `shame_mediated_identity_rupture` = `stigmatizing excluder`
- `explicit_political_distrust` = `political enemy`

Use this instrument only after first deciding whether the segment is a genuine reflection segment.

In v1, rubric labels may be produced by a reasoning-backed coding pass or by direct human coding. When manual review is used, the reviewer audits the reasoning and label package rather than re-coding from scratch unless a reliability exercise explicitly requires blind re-coding.

## Step 1: Confirm Reflection Relevance

Code `reflection_relevance = yes` only if the segment does at least one of the following:

- interprets incarceration, exclusion, state action, or civic belonging in retrospective terms
- connects wartime or postwar experience to trust, identity, rights, democracy, citizenship, stigma, exclusion, or belonging
- narrates a meaningful stance toward state authority, public institutions, or collective membership

Code `reflection_relevance = no` if the segment is mainly:

- factual logistics without interpretation
- interviewer setup with little narrator substance
- biographical detail with no state-relation or belonging interpretation
- topic continuation that lacks independent codable content

If `reflection_relevance = no`, leave `what_type_rubric`, `how_composure_rubric`, and `outcome_type_3x2_rubric` blank.

## Step 2: Code `what`

Choose exactly one class.

### `authority_schema_injury`

Core idea:

- `failed protector`: the narrator frames the injury as a failure of expected protection, fairness, or institutional duty, but the main register is not yet damaged belonging or full political distrust

Typical signals:

- an authority, office, or institution failed to protect or treat the narrator fairly
- the narrator still speaks from within a baseline expectation that the polity or public order should have protected them
- the segment emphasizes failed protection or broken fairness more than stigma, membership injury, or explicit state distrust

Use when:

- the segment centers on failed protection, failed fairness, or betrayal by authorities

Do not use when:

- the main emphasis is humiliation, stigma, or not-quite-belonging
- the narrator explicitly treats the state or political order as untrustworthy, hostile, or adversarial

### `shame_mediated_identity_rupture`

Core idea:

- `stigmatizing excluder`: the main injury is damaged membership, stigma, humiliation, or a fracture in selfhood and belonging

Typical signals:

- shame, embarrassment, stigma, or exclusion
- uncertainty about being American, Japanese American, or accepted in community
- emphasis on social devaluation, damaged membership, or identity injury rather than failed protection alone

Use when:

- the segment centers on wounded belonging, damaged identity, or social devaluation

Do not use when:

- the segment is mostly about failed protection without a primary belonging wound
- the segment is mainly an explicit political judgment that the state itself is untrustworthy or adversarial

### `explicit_political_distrust`

Core idea:

- `political enemy`: the narrator explicitly treats the state, its institutions, or its political promises as untrustworthy, hostile, or adversarial objects of judgment

Typical signals:

- direct claims that government cannot be trusted
- explicit political critique, civic distrust, or oppositional interpretation
- durable skepticism toward public authority, rights guarantees, or democratic promises

Use when:

- the narrator clearly foregrounds political distrust rather than only disappointment, stigma, or membership injury

Do not use when:

- the narrator is mainly describing failed protection without explicit political distrust
- the main emphasis is on shame, humiliation, or wounded identity

Note:

- explicit political distrust does not require total loss of belonging; oppositional or claim-making belonging can still be present

## Step 3: Code `how`

Choose exactly one class.

### `composed`

Core idea:

- narration is organized, steady, and interpretively controlled

Typical signals:

- coherent sequencing
- stable tone
- reflective distance or calm framing even when content is painful

### `discomposed`

Core idea:

- narration is disrupted, unsettled, fragmented, or affectively strained in a substantively meaningful way

Typical signals:

- interruptions, breakdowns, or visible narrative strain
- abrupt restarts, confusion, or emotional flooding tied to the content
- difficulty sustaining an organized telling of the event or meaning

Do not infer `discomposed` from the topic alone. Code the narration, not just the event.

## Step 4: Map to 3x2 Type

Use the deterministic mapping below.

- `authority_schema_injury` + `composed` = `Guarded Vigilance`
- `authority_schema_injury` + `discomposed` = `Diffuse Unease`
- `shame_mediated_identity_rupture` + `composed` = `Wounded Belonging`
- `shame_mediated_identity_rupture` + `discomposed` = `Stigmatized Discomposure`
- `explicit_political_distrust` + `composed` = `Oppositional Citizenship`
- `explicit_political_distrust` + `discomposed` = `Ambivalent Estrangement`

## Required Output Fields

For each reviewed segment, record:

- `reflection_relevance`
- `what_type_rubric`
- `how_composure_rubric`
- `outcome_type_3x2_rubric`
- `justification_excerpt`
- `coder_confidence`
- `reviewer_notes`

## Confidence Scale

- `high`: clear fit with little ambiguity
- `medium`: plausible fit but one nearby class is competitive
- `low`: boundary case, insufficient context, or strong ambiguity

## Boundary Rules

- If `what` is torn between institutional betrayal and identity shame, ask what the narrator treats as the main injury.
- If `what` is torn between identity injury and explicit political distrust, ask whether the segment's center of gravity is wounded belonging or direct judgment of the state.
- If multiple interviewers are present, code only the narrator's substantive contribution.
- If the narrator response is too short to support `what` or `how`, mark `reflection_relevance = no` or `coder_confidence = low` depending on whether any interpretable substance remains.
- If the segment contains genuine reflection but only weak evidence for `how`, still code `what`, choose the best `how`, and lower confidence.

## Pilot Note

This v1 instrument is a starting point for the video-first pilot. Any recurring ambiguity should be logged and used to revise this file before broader rubric coding or evaluation.