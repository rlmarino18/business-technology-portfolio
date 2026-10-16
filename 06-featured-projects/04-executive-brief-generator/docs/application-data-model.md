# Executive Brief Generator — Application Data Model

## Purpose

This document defines the minimum data structures required to operationalize the validated Executive Brief Generator workflow.

The objective is to translate the existing prompt-based records into application-friendly structures without changing the underlying business logic.

---

# 1. Core Principle

The application should preserve the validated information contract.

The software representation should make it easier to:

- render records in the UI,
- edit them,
- validate them,
- approve them,
- pass them between Stage 1 and Stage 2,
- store version metadata,
- preserve source traceability.

The data model must not weaken the source-grounding rules established during prompt validation.

---

# 2. Source Record

A source record represents the raw operational information submitted by the user.

Recommended structure:

```json
{
  "sourceId": "SRC-001",
  "title": "Weekly Operating Review",
  "content": "Raw meeting notes or operating update...",
  "createdAt": "2026-08-21T00:00:00Z"
}
```

## Required Fields

### sourceId

Unique identifier for the submitted source.

### title

Human-readable label for the input.

### content

Original unstructured operating material.

### createdAt

Timestamp showing when the source entered the application.

---

# 3. Structured Stage-1 Record

Each extracted item should be represented as an independent structured record.

Recommended structure:

```json
{
  "id": "A-001",
  "type": "ACTION",
  "statement": "Jordan will confirm the final client roster.",
  "sourceEvidence": "Jordan said he will confirm the final client roster tomorrow.",
  "sourceReporter": "Jordan",
  "operationalOwner": "Jordan",
  "accountableOrganization": null,
  "approvingParty": null,
  "organizationParty": null,
  "deadline": "Tomorrow",
  "decisionState": "Not stated",
  "certainty": "Confirmed",
  "dependencyCondition": null,
  "validationRequired": false,
  "notes": null
}
```

---

# 4. Supported Record Types

The application should use the same controlled record types as Structured Extractor V0.7:

```text
FACT
DECISION
ISSUE
RISK
ACTION
GOAL
RECOMMENDATION
DEPENDENCY
HANDOFF
CONFLICT
OPEN_QUESTION
COMPLIANCE_OBLIGATION_QUESTION
VALIDATION_ITEM
```

These values should be treated as controlled data rather than arbitrary labels.

---

# 5. Decision-State Values

Supported decision states:

```text
Proposed
Recommended
Conditionally Approved
Approved
Rejected
Deferred
On Hold
Superseded
No Decision
Not stated
```

The application should not create additional decision states without a future schema/version change.

---

# 6. Certainty Values

Supported certainty states:

```text
Confirmed
Approximate
Estimated
Unconfirmed
Disputed
Preliminary
Under Investigation
Calculated
Reported
Not stated
```

These values preserve the uncertainty controls validated during Stage 1 testing.

---

# 7. Missing Information

For the application layer, missing values should preferably be stored as:

```json
null
```

rather than converting every missing field into text such as:

```text
Not stated
```

The UI may display:

```text
Not stated
```

to the user.

This creates a useful separation:

```text
Stored value → null
Displayed value → Not stated
```

Exception:

Controlled semantic values such as Decision State = `Not stated` or Certainty = `Not stated` remain explicit controlled values because `Not stated` is itself part of those schemas.

---

# 8. Stage-1 Output Object

A complete Stage-1 run can be represented as:

```json
{
  "runId": "RUN-001",
  "sourceId": "SRC-001",
  "promptVersion": "structured-extractor-v0.7",
  "status": "STAGE1_DRAFT",
  "records": [],
  "generatedAt": "2026-08-21T00:00:00Z",
  "approvedAt": null
}
```

---

# 9. Workflow Status

Recommended controlled workflow states:

```text
SOURCE_ENTERED
STAGE1_RUNNING
STAGE1_DRAFT
STAGE1_REVIEW
STAGE1_APPROVED
STAGE2_RUNNING
STAGE2_DRAFT
FINAL_REVIEW
FINAL_APPROVED
ERROR
```

These states directly implement the integration contract.

---

# 10. Stage-1 Approval

Stage-1 approval should be stored separately from the generated records.

Recommended structure:

```json
{
  "approved": true,
  "approvedAt": "2026-08-21T00:00:00Z",
  "approvedBy": "prototype-user",
  "recordVersion": 2
}
```

The `recordVersion` allows the application to detect whether records were edited after approval.

If records change:

```text
recordVersion increases
Stage-1 approval becomes invalid
```

Stage 2 should only run against the currently approved record version.

---

# 11. Stage-2 Run Object

Recommended structure:

```json
{
  "runId": "RUN-001-S2",
  "stage1RunId": "RUN-001",
  "stage1ApprovedVersion": 2,
  "promptVersion": "executive-brief-generator-v1.4",
  "status": "STAGE2_DRAFT",
  "brief": "Generated executive brief...",
  "generatedAt": "2026-08-21T00:00:00Z",
  "approvedAt": null
}
```

This establishes traceability between:

```text
Source
→ Stage-1 Run
→ Approved Stage-1 Version
→ Stage-2 Run
```

---

# 12. Final Approval

Recommended structure:

```json
{
  "approved": true,
  "approvedAt": "2026-08-21T00:00:00Z",
  "approvedBy": "prototype-user"
}
```

The output should not be represented as final until this approval exists.

---

# 13. Validation Flags

The application should eventually support validation flags on individual Stage-1 records.

Example:

```json
{
  "humanValidationStatus": "APPROVED",
  "humanValidationNote": null
}
```

Suggested values:

```text
PENDING
APPROVED
CORRECTED
REJECTED
```

For the first prototype, this can remain lightweight.

---

# 14. Traceability Metadata

Each run should eventually retain:

- source ID,
- prompt version,
- generation timestamp,
- record version,
- approval state,
- approval timestamp,
- associated Stage-2 run,
- application version.

Future versions may also include:

- model name,
- model parameters,
- token usage,
- latency,
- user ID,
- error logs.

Those are not required for the first functional prototype.

---

# 15. Initial Prototype Storage

The initial prototype does not require a production database.

Acceptable early storage options include:

- application memory during a session,
- browser local storage,
- local JSON files during development.

A database should be introduced when persistence, multi-user access, pilot history, or reporting requires it.

---

# 16. JSON as the Application Boundary

Although the validated prompts currently produce human-readable structured records, the application should progressively move toward JSON as the machine-readable boundary between components.

Target future flow:

```text
Raw Source
→ Stage 1 LLM
→ JSON Structured Records
→ Application Validation / UI
→ Approved JSON
→ Stage 2 LLM
→ Executive Brief
```

Why JSON:

- predictable structure,
- easier field validation,
- easier UI rendering,
- easier API integration,
- easier persistence,
- easier automated testing.

The transition to JSON must be validated separately before replacing the currently promoted Stage-1 output format.

---

# 17. Important Change-Control Boundary

Structured Extractor V0.7 was promoted using the existing output contract.

Changing Stage 1 to emit JSON directly is therefore:

**an interface change**

and potentially:

**a behavior change**

It should not be silently introduced into V0.7.

A future JSON-output candidate should be versioned and tested separately.

For the first application prototype, the safest approach is:

1. Run the promoted V0.7 prompt.
2. Preserve its validated output.
3. Parse or display that output in the application.
4. Introduce native JSON generation only through a controlled future candidate.

---

# 18. Core Data-Model Principle

The application should make the validated workflow easier to execute without changing what the validated workflow means.

Software structure should reinforce:

**source grounding, explicit ownership, controlled decisions, preserved uncertainty, human validation, and traceability.**