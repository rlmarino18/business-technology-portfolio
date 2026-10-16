# Executive Brief Generator — Prototype User Workflow

## Purpose

This document defines how a user should move through the first functional Executive Brief Generator prototype.

The goal is to translate the validated Stage 1 + Stage 2 workflow into a simple application experience without removing the required human-review gates.

---

# 1. Core User Flow

The prototype should follow this sequence:

```text
Enter Source
→ Run Stage 1
→ Review Structured Records
→ Approve Stage 1
→ Run Stage 2
→ Review Executive Brief
→ Approve Final Brief
```

The application must not collapse the workflow into:

```text
Enter Source
→ Generate Final Brief
```

The human-review gates are part of the product design.

---

# 2. Screen 1 — Source Input

The user begins by entering raw operating information.

The first prototype should support:

- a title,
- a large text area,
- plain-text operating notes,
- meeting notes,
- project updates,
- operational review content.

Required controls:

- Title field
- Source text field
- Run Stage 1 button
- Clear / Reset button

The prototype does not need file upload yet.

---

# 3. Stage 1 Execution

When the user selects:

**Run Stage 1**

the application should:

1. preserve the original source,
2. mark workflow status as `STAGE1_RUNNING`,
3. execute Structured Extractor V0.7,
4. preserve the generated structured output,
5. move the workflow to `STAGE1_REVIEW`.

The application should visibly show that Stage 1 is processing.

---

# 4. Screen 2 — Stage 1 Review

The user should see:

## Original Source

The original source remains visible or easily accessible.

## Structured Output

The Structured Extractor V0.7 result is displayed for review.

For the first prototype, this may initially be rendered as the validated human-readable structured output rather than a fully interactive record table.

The user should be able to:

- compare source and output,
- review ownership,
- review decision state,
- review deadlines,
- review certainty,
- inspect source evidence,
- correct the structured output if necessary.

---

# 5. Stage 1 Approval

The Stage 1 review screen should include:

- Edit
- Approve Stage 1
- Rerun Stage 1

The user cannot run Stage 2 until Stage 1 is approved.

When Stage 1 is approved:

```text
status → STAGE1_APPROVED
```

The application should preserve:

- approval timestamp,
- approved Stage-1 version,
- current structured output.

---

# 6. Editing After Approval

If the user edits Stage-1 output after approval:

```text
previous approval → invalid
status → STAGE1_REVIEW
```

The revised output must be approved again before Stage 2 becomes available.

This prevents Stage 2 from using structured information that the user has changed but not reapproved.

---

# 7. Stage 2 Execution

After Stage-1 approval, the user may select:

**Generate Executive Brief**

The application should:

1. use only the approved Stage-1 output,
2. mark workflow status as `STAGE2_RUNNING`,
3. execute Executive Brief Generator V1.4,
4. preserve the generated draft brief,
5. move workflow status to `FINAL_REVIEW`.

Stage 2 must not independently return to the raw source and reinterpret it.

---

# 8. Screen 3 — Executive Brief Review

The user should see:

- Draft Executive Brief
- Approved Stage-1 output
- prompt version metadata
- workflow status

The user should be able to:

- review the brief,
- edit final wording,
- verify material claims,
- compare the brief with Stage-1 records,
- approve the final output.

---

# 9. Final Approval

The final screen should include:

- Edit Brief
- Regenerate Stage 2
- Approve Final Brief

When approved:

```text
status → FINAL_APPROVED
```

The application should preserve:

- approval timestamp,
- final approved brief,
- Stage-1 version used,
- Stage-1 prompt version,
- Stage-2 prompt version.

---

# 10. Error States

## Stage 1 Error

If Stage 1 fails:

- preserve the source,
- show an error message,
- do not expose Stage 2,
- allow Stage 1 retry.

## Stage 2 Error

If Stage 2 fails:

- preserve the approved Stage-1 output,
- show an error message,
- allow Stage 2 retry,
- do not require Stage 1 to rerun.

## Invalid Workflow State

If the application detects that Stage 1 has changed after approval:

- invalidate approval,
- disable Stage 2,
- require reapproval.

---

# 11. Initial Prototype Navigation

The first prototype should remain simple.

Recommended navigation:

```text
1. Source
2. Structured Review
3. Executive Brief
```

Avoid unnecessary navigation such as:

- dashboards,
- settings pages,
- analytics pages,
- user-management pages,
- admin portals.

Those do not help validate the core workflow yet.

---

# 12. Prototype UI Priorities

The first interface should optimize for:

1. workflow clarity,
2. source visibility,
3. structured-output review,
4. human approval,
5. traceability,
6. simple error recovery.

Visual polish is secondary to workflow correctness.

---

# 13. What the User Should Always Know

At every stage, the interface should make clear:

- what step they are currently on,
- whether AI output is still a draft,
- whether human approval has occurred,
- which prompt version generated the output,
- whether Stage 2 is allowed to run,
- whether an error occurred.

---

# 14. First Prototype Success Criteria

The prototype succeeds if a user can complete this workflow:

```text
Paste source
→ Run Structured Extractor V0.7
→ Review structured output
→ Approve Stage 1
→ Run Executive Brief Generator V1.4
→ Review draft brief
→ Approve final brief
```

without manually copying information between separate prompts or applications.

---

# 15. Out of Scope for the First Prototype

Do not build yet:

- authentication,
- user accounts,
- client portals,
- database dashboards,
- PDF upload,
- DOCX upload,
- meeting transcription,
- CRM integration,
- email automation,
- role-based permissions,
- automatic executive distribution,
- autonomous approval,
- analytics dashboards.

These may become future features after the core workflow functions reliably.

---

# 16. Core UX Principle

The interface should make the validated control model visible.

The product is not:

**AI creates an executive report.**

The product is:

**AI structures → human validates → AI communicates → human approves.**