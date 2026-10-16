# Executive Brief Generator Evaluation Rubric

## Purpose

This rubric is used to evaluate generated Executive Brief outputs against human-approved gold standards.

The purpose is not to judge whether an output sounds professional.

The purpose is to determine whether the system:

- Preserves source facts
- Correctly identifies decisions and actions
- Preserves ownership and deadlines
- Handles uncertainty correctly
- Respects scope and authority boundaries
- Produces useful executive reporting

Maximum score: 20 points

---

# Scoring Categories

## 1. Factual Accuracy — 0 to 2

### 0 — Fail
Contains one or more material factual errors, fabricated facts, incorrect numbers, or unsupported statements.

### 1 — Partial
Core facts are correct, but minor factual errors or unsupported wording appear.

### 2 — Pass
Material facts are accurately preserved and no material unsupported claims are introduced.

---

## 2. Completeness — 0 to 2

### 0 — Fail
Misses one or more material facts, decisions, actions, risks, or operating developments.

### 1 — Partial
Captures most important information but omits minor relevant items.

### 2 — Pass
Captures all material information required for the executive brief.

---

## 3. Decision Accuracy — 0 to 2

### 0 — Fail
Invents decisions, misses material decisions, or incorrectly represents decision state.

### 1 — Partial
Generally identifies decisions correctly but contains minor state or wording problems.

### 2 — Pass
Correctly distinguishes approved, rejected, conditional, deferred, on-hold, proposed, recommended, and superseded positions.

---

## 4. Action Accuracy — 0 to 2

### 0 — Fail
Invents material actions, misses material actions, or converts goals/recommendations into actions.

### 1 — Partial
Most actions are correct but minor classification or completeness issues remain.

### 2 — Pass
Only explicitly supported actions are included and material actions are captured.

---

## 5. Ownership Accuracy — 0 to 2

### 0 — Fail
Assigns actions, commitments, or responsibility to the wrong person, team, or organization.

### 1 — Partial
Minor ownership ambiguity exists but does not create a material false commitment.

### 2 — Pass
Ownership and organizational boundaries are accurately preserved.

---

## 6. Deadline Accuracy — 0 to 2

### 0 — Fail
Invents or materially changes a deadline.

### 1 — Partial
Minor ambiguity exists in relative or expected dates.

### 2 — Pass
Deadlines, expected dates, conditions, and missing dates are correctly preserved.

---

## 7. Risk / Issue Classification — 0 to 2

### 0 — Fail
Materially confuses future risks with existing issues or invents risks/issues.

### 1 — Partial
Mostly correct with minor classification weaknesses.

### 2 — Pass
Existing issues, future risks, compliance questions, and investigation states are accurately distinguished.

---

## 8. Uncertainty Handling — 0 to 2

### 0 — Fail
Turns disputed, approximate, preliminary, or missing information into false certainty.

### 1 — Partial
Most uncertainty is preserved, but some wording is overly confident.

### 2 — Pass
Approximate, disputed, preliminary, conflicting, and missing information remains visibly uncertain.

---

## 9. Dependency / Scope Control — 0 to 2

### 0 — Fail
Breaks dependency logic, ignores approval gates, or turns out-of-scope requests into commitments.

### 1 — Partial
Core boundaries are preserved but minor workflow or scope weaknesses exist.

### 2 — Pass
Dependencies, conditions, handoffs, approval gates, and scope boundaries are accurately preserved.

---

## 10. Executive Usability — 0 to 2

### 0 — Fail
Output is misleading, difficult to use, or requires substantial rewriting.

### 1 — Partial
Useful but requires meaningful human revision.

### 2 — Pass
Clear, concise, structured, and usable with minimal revision.

---

# Score Interpretation

## 18–20 — Pass

Strong enough for controlled prototype use with required human review.

## 15–17 — Conditional Pass

Useful, but meaningful corrections are still required.

## 10–14 — Fail

Not reliable enough for controlled business use without substantial correction.

## 0–9 — Critical Fail

Materially unreliable.

---

# Automatic Failure Conditions

A test fails regardless of numerical score if the output contains any material instance of:

- Invented financial figure
- Invented business decision
- Invented material owner
- Invented material deadline
- Wrong organization assigned responsibility
- Client request represented as provider commitment
- Out-of-scope work represented as committed work
- Rejected or deferred decision represented as approved
- Preliminary safety finding represented as final
- Unresolved legal or compliance matter represented as resolved
- Material conflicting data silently reconciled without authority
- Unsupported claim that could materially affect a business decision

---

# Human Review Requirement

A passing score does not make the output final.

Every generated Executive Brief remains:

REVIEW STATUS: DRAFT — HUMAN VALIDATION REQUIRED