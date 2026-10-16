# Executive Brief Generator — Stage 1 / Stage 2 Integration Contract

## Purpose

This document defines how information moves between the validated Structured Extractor V0.7 and Executive Brief Generator V1.4.

The goal is to preserve the behavior validated during prompt testing while converting the workflow into a repeatable application.

---

# 1. Active Architecture

Raw Source
→ Structured Extractor V0.7
→ Structured Stage-1 Output
→ Human Validation
→ Approved Structured Output
→ Executive Brief Generator V1.4
→ Draft Executive Brief
→ Human Approval

---

# 2. Stage 1 Input

Stage 1 receives unstructured operational information.

Examples:

- meeting notes
- operating reviews
- project updates
- client implementation notes
- financial updates
- action logs
- mixed operational narratives

Initial prototype input format:

**Plain text**

Future versions may support:

- document upload
- PDF
- DOCX
- email ingestion
- meeting transcription
- API-based inputs

These are outside the current integration scope.

---

# 3. Stage 1 Responsibility

Structured Extractor V0.7 is responsible for determining what the source explicitly supports.

Supported record types include:

- Fact
- Decision
- Issue
- Risk
- Action
- Goal / Desired Outcome
- Recommendation
- Dependency
- Handoff
- Conflict
- Open Question
- Compliance / Obligation Question
- Validation Item

Stage 1 must preserve source grounding and must not invent unsupported:

- owners
- deadlines
- decision states
- approvals
- causes
- commitments
- risks
- accountability

---

# 4. Stage 1 Output

For the initial prototype, Stage 1 may continue producing the validated human-readable structured format used during testing.

Each record can contain:

- ID
- Type
- Statement
- Source Evidence
- Source / Reporter
- Operational Owner
- Accountable Organization
- Approving Party
- Organization / Party
- Deadline
- Decision State
- Certainty
- Dependency / Condition
- Validation Required
- Notes

The application must preserve this output without silently rewriting it before human review.

---

# 5. Human Stage-1 Validation Gate

Stage 1 output must not automatically proceed to Stage 2.

The user must be able to:

- review the extracted records,
- compare them with the original source,
- identify incorrect or unsupported information,
- edit the structured output if necessary,
- approve the Stage-1 result.

Stage-2 generation becomes available only after Stage-1 approval.

Prototype principle:

**AI proposes structured information; human validates it before executive communication.**

---

# 6. Stage 2 Input

Executive Brief Generator V1.4 receives:

**The human-approved Stage-1 structured output**

It must not receive a separately rewritten interpretation of the source.

This preserves the validated Stage-1 → Stage-2 control boundary.

---

# 7. Stage 2 Responsibility

Stage 2 is responsible for:

- executive communication,
- prioritization,
- organization,
- summarization,
- action presentation,
- leadership-attention presentation.

Stage 2 must remain grounded in the approved Stage-1 records.

It must not independently invent:

- facts,
- owners,
- deadlines,
- decisions,
- approvals,
- causes,
- commitments,
- formal open questions.

---

# 8. Stage 2 Output

Stage 2 produces a:

**Draft Executive Brief**

The draft may contain sections such as:

- Executive Summary
- Key Developments
- Decisions
- Issues
- Risks
- Actions
- Leadership Attention
- Open Questions
- Compliance / Obligation Questions
- Dependencies / Handoffs

Exact sections depend on source-supported content.

No forced findings are required.

---

# 9. Human Final-Approval Gate

The Stage-2 output remains:

**Draft**

until reviewed by a human.

The user must be able to:

- review the brief,
- revise wording,
- compare material claims with structured records,
- approve the final brief.

Prototype principle:

**AI generates; human approves.**

---

# 10. Application State Model

The prototype should recognize the following workflow states:

1. Source Entered
2. Stage 1 Running
3. Stage 1 Draft Generated
4. Stage 1 Under Review
5. Stage 1 Approved
6. Stage 2 Running
7. Stage 2 Draft Generated
8. Final Review
9. Final Approved

The application must not skip the two human-review gates.

---

# 11. Error Handling

If Stage 1 fails:

- retain the original source,
- display an error,
- do not call Stage 2.

If Stage 1 is not approved:

- Stage 2 remains unavailable.

If Stage 2 fails:

- preserve the approved Stage-1 output,
- allow Stage 2 to be rerun,
- do not require Stage 1 to run again unless the user changes it.

If the user changes Stage-1 content after approval:

- previous Stage-1 approval becomes invalid,
- Stage 2 must use the newly approved version.

---

# 12. Version Control

Current prompt versions:

Stage 1:
**Structured Extractor V0.7**

Stage 2:
**Executive Brief Generator V1.4**

The application should eventually record which prompt version generated each output.

The prototype must not silently modify promoted prompt baselines.

Prompt changes require separate candidate versions and validation.

---

# 13. Current Scope

Included:

- manual text input,
- Stage-1 execution,
- Stage-1 review,
- Stage-1 approval,
- Stage-2 execution,
- Stage-2 review,
- final approval.

Not currently included:

- authentication,
- multi-user accounts,
- CRM integration,
- meeting transcription,
- automated email distribution,
- client portal,
- autonomous approval,
- production database,
- enterprise permissions,
- production monitoring.

---

# 14. Core Integration Principle

The application is not replacing the validated workflow.

It is operationalizing it.

The software layer should preserve:

**Source → Extraction → Validation → Communication → Approval**

rather than collapsing the system back into:

**Source → AI Summary**