# Executive Brief Generator — Front-End Implementation Plan

## Purpose

This document defines the first working front-end prototype for the Executive Brief Generator.

The objective is to build the smallest browser-based interface that can demonstrate the validated workflow:

Source
→ Stage 1
→ Human Review
→ Stage 2
→ Human Approval

The first implementation should prioritize workflow correctness over visual polish.

---

# 1. First Prototype Objective

The first front-end prototype should allow one user to:

1. enter raw operating source text,
2. run or simulate Stage 1,
3. review Stage-1 structured output,
4. approve Stage 1,
5. run or simulate Stage 2,
6. review the executive brief,
7. approve the final brief.

The user should not need to manually move information between separate interfaces.

---

# 2. Current Technical Starting Point

The existing repository already contains:

- `index.html`
- `css/`
- `js/`
- validated prompts
- test data
- evaluation artifacts
- documentation

The first prototype should continue using the existing lightweight front-end stack.

Initial stack:

```text
HTML
CSS
Vanilla JavaScript
```

No framework is required yet.

Reasons:

- faster implementation,
- easier to understand,
- fewer dependencies,
- sufficient for the current prototype,
- keeps attention on workflow behavior rather than framework configuration.

---

# 3. Important Integration Reality

The browser cannot securely contain a production AI API key.

Therefore, the implementation should occur in phases.

## Phase A — Front-End Workflow Prototype

Build the complete user experience using controlled mock outputs.

Purpose:

- prove navigation,
- prove application state,
- prove approval gates,
- prove edit behavior,
- prove Stage-1 → Stage-2 workflow.

No live AI API is required for this phase.

## Phase B — AI Integration

Once the front-end workflow functions correctly:

- add a secure server-side API layer,
- call the selected AI provider from the server,
- load the promoted prompt versions,
- return generated output to the browser.

API keys must remain server-side.

---

# 4. Prototype Screens

The first interface should have three primary workflow views.

## View 1 — Source Input

Purpose:

Collect raw operational material.

Required components:

- page / product title,
- source title input,
- large source-text area,
- `Run Stage 1` button,
- `Clear` button,
- workflow-status indicator.

Example:

```text
Executive Brief Generator

Step 1 of 3 — Source

Source Title
[ Weekly Operating Review               ]

Operating Source
[                                           ]
[ Raw meeting notes...                      ]
[                                           ]

[ Run Stage 1 ]   [ Clear ]
```

---

# 5. View 2 — Structured Review

Purpose:

Allow human validation of Structured Extractor output.

Required components:

- workflow step indicator,
- original source panel,
- Stage-1 output panel,
- editable structured-output field,
- prompt version,
- approval state,
- `Rerun Stage 1`,
- `Approve Stage 1`.

Example:

```text
Step 2 of 3 — Structured Review

Stage 1
Structured Extractor V0.7

Original Source
--------------------------------
[source text]
--------------------------------

Structured Output
--------------------------------
[editable Stage-1 output]
--------------------------------

Status: Draft — Human Review Required

[ Rerun Stage 1 ]   [ Approve Stage 1 ]
```

---

# 6. View 3 — Executive Brief

Purpose:

Generate and approve Stage-2 executive communication.

Required components:

- approved Stage-1 output,
- Stage-2 prompt version,
- generated executive brief,
- editable final brief,
- `Regenerate`,
- `Approve Final Brief`.

Example:

```text
Step 3 of 3 — Executive Brief

Stage 2
Executive Brief Generator V1.4

Executive Brief
--------------------------------
[editable generated brief]
--------------------------------

Status: Draft — Human Approval Required

[ Regenerate ]   [ Approve Final Brief ]
```

After approval:

```text
Status: Final Approved
```

---

# 7. Recommended Page Structure

The initial application can remain a single HTML page.

Recommended structure:

```text
index.html
│
├── App Header
├── Workflow Progress
│
├── Source Section
├── Stage-1 Review Section
├── Stage-2 Review Section
│
└── Status / Error Area
```

JavaScript controls which section is active.

We do not need three separate HTML pages.

---

# 8. Application State

The JavaScript application should maintain an internal state object.

Conceptual example:

```javascript
const appState = {
  status: "SOURCE_ENTERED",
  source: {
    title: "",
    content: ""
  },
  stage1: {
    output: "",
    approved: false,
    version: 1,
    promptVersion: "structured-extractor-v0.7"
  },
  stage2: {
    output: "",
    approved: false,
    promptVersion: "executive-brief-generator-v1.4"
  }
};
```

This is an application implementation structure.

It does not replace the formal product data model.

---

# 9. Stage-1 Prototype Behavior

For Phase A, clicking:

```text
Run Stage 1
```

should:

1. validate that source text exists,
2. change status to `STAGE1_RUNNING`,
3. display a loading state,
4. generate a controlled mock Stage-1 output,
5. display the Structured Review view,
6. set status to `STAGE1_REVIEW`.

The mock result should look like a real Structured Extractor output so the UI can be tested realistically.

---

# 10. Stage-1 Approval Behavior

When the user selects:

```text
Approve Stage 1
```

the application should:

1. save the current structured output,
2. set:

```text
stage1.approved = true
```

3. record the approved Stage-1 version,
4. change status to:

```text
STAGE1_APPROVED
```

5. enable:

```text
Generate Executive Brief
```

Stage 2 remains disabled before this point.

---

# 11. Stage-1 Edit Protection

If the user modifies Stage-1 output after approval:

```text
stage1.approved = false
```

and:

```text
status = STAGE1_REVIEW
```

The application should inform the user:

```text
Stage-1 approval was invalidated because the structured output changed.
Reapprove Stage 1 before generating a new executive brief.
```

This is an important implementation of the human-review control model.

---

# 12. Stage-2 Prototype Behavior

For Phase A, clicking:

```text
Generate Executive Brief
```

should:

1. verify Stage 1 is approved,
2. set status to `STAGE2_RUNNING`,
3. display a loading state,
4. generate a controlled mock Executive Brief,
5. display the Executive Brief view,
6. set status to `FINAL_REVIEW`.

The mock Stage-2 output should use the approved Stage-1 information.

---

# 13. Final Approval Behavior

When the user selects:

```text
Approve Final Brief
```

the application should:

```text
stage2.approved = true
status = FINAL_APPROVED
```

The interface should clearly display:

```text
Final Approved
```

The approved output should remain visible.

---

# 14. Reset Behavior

The `Clear` or `Start New Brief` action should reset:

- source,
- Stage-1 output,
- Stage-1 approval,
- Stage-2 output,
- Stage-2 approval,
- workflow status.

The user should receive confirmation before clearing an in-progress workflow if useful.

---

# 15. Error Handling

The first implementation should support basic errors.

Examples:

## Missing Source

```text
Enter operating source information before running Stage 1.
```

## Stage 2 Before Approval

```text
Stage 1 must be approved before generating the executive brief.
```

## Invalidated Approval

```text
Stage-1 content changed after approval. Reapproval is required.
```

## Generation Failure

```text
Generation failed. Your current source and approved information have been preserved.
```

---

# 16. Workflow Progress Indicator

The interface should always show where the user is.

Example:

```text
1. Source
2. Structured Review
3. Executive Brief
```

Possible states:

```text
Current
Complete
Locked
```

Example after Stage-1 approval:

```text
✓ Source
✓ Structured Review
3. Executive Brief
```

---

# 17. Version Visibility

The interface should display the active prompt versions.

Example:

```text
Stage 1: Structured Extractor V0.7
Stage 2: Executive Brief Generator V1.4
```

Purpose:

- traceability,
- transparency,
- easier debugging,
- portfolio demonstration.

---

# 18. Human-Review Messaging

The interface should avoid language suggesting autonomous reliability.

Preferred:

```text
AI-generated draft
Human review required
Stage 1 approved
Final approved
```

Avoid:

```text
Verified by AI
Automatically approved
Guaranteed accurate
Final without review
```

---

# 19. Files Expected for First Implementation

The first build should primarily modify:

```text
index.html
css/styles.css
js/app.js
```

If the existing CSS or JavaScript files use different names, preserve the existing repository naming convention.

Additional files should only be created when necessary.

---

# 20. Phase-A Definition of Done

The first front-end workflow is complete when:

- source text can be entered,
- Stage 1 can be triggered,
- structured output appears,
- Stage-1 output can be edited,
- Stage 1 can be approved,
- editing after approval invalidates approval,
- Stage 2 cannot run before Stage-1 approval,
- Stage 2 can be triggered after approval,
- executive brief appears,
- final brief can be edited,
- final brief can be approved,
- workflow progress is visible,
- prompt versions are visible,
- basic errors are handled,
- the entire workflow works in the browser.

No live AI integration is required to satisfy Phase A.

---

# 21. Phase-B Definition of Done

AI integration is complete when:

- the browser sends source information to a secure backend,
- the backend runs Structured Extractor V0.7,
- the returned Stage-1 output enters the review workflow,
- only approved Stage-1 output can be sent to Stage 2,
- the backend runs Executive Brief Generator V1.4,
- the returned executive brief enters final review,
- API credentials remain server-side,
- failures preserve the current workflow state.

---

# 22. Core Implementation Principle

Do not connect AI before the application workflow itself is correct.

The implementation sequence is:

```text
Workflow
→ State
→ Review Gates
→ Mock Generation
→ Browser Testing
→ AI Integration
→ Measurement
```

not:

```text
API Call
→ Hope the rest works
```