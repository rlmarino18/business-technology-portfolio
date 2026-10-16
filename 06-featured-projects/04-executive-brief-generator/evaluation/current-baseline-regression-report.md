# Current Baseline Regression Report

## Baseline Status

Current Structured Extraction Baseline:

Structured Extractor V0.7

Current Executive Brief Baseline:

Executive Brief Generator V1.3

Current Approved Pipeline:

Raw Source

→

Structured Extractor V0.7

→

Structured Records + Source Evidence

→

Validation

→

Executive Brief Generator V1.3

→

Draft Executive Brief

→

Human Approval

---

# 1. Current Baseline

## Stage 1

Structured Extractor V0.7

Status:

CURRENT BASELINE

Promotion Basis:

- E-005 ownership-inference remediation preserved
- E-006 decision-authority remediation passed
- targeted regression passed
- decision-state protection regression passed
- broader regression completed
- 10 / 10 broader-regression cases passed
- no material promotion-blocking defects remained

---

## Stage 2

Executive Brief Generator V1.3

Status:

CURRENT BASELINE

V1.3 was not modified during the V0.7 remediation and promotion cycle.

---

# 2. Superseded / Historical Versions

## Structured Extractor V0.4

Status:

HISTORICAL BASELINE — SUPERSEDED BY V0.6

Reason:

V0.4 remained vulnerable to E-005 role/context-based ownership inference.

---

## Structured Extractor V0.5

Status:

FAILED PROMOTION CANDIDATE

Reason:

V0.5 successfully addressed E-005 in targeted testing but introduced E-006 during broader regression.

E-006:

Role-supported operational imperative was incorrectly elevated to formal approval.

V0.5 remains retained for defect history and comparison.

---

# 3. V0.6 Promotion Evidence

## E-006 Targeted Regression

Test:

TC-006

Result:

PASS

Score:

20 / 20

E-006 observed:

NO

---

## Decision-State Protection Regression

Cases:

TC-001 through TC-005

Results:

TC-001 — 20 / 20 — PASS

TC-002 — 20 / 20 — PASS

TC-003 — 20 / 20 — PASS

TC-004 — 20 / 20 — PASS

TC-005 — 19 / 20 — PASS

Aggregate:

99 / 100 available evaluation points

Material regressions:

0

Automatic failures:

0

---

# 4. V0.6 Broader Regression

Results:

TC-001 — 20 / 20 — PASS

TC-002 — 20 / 20 — PASS

TC-003 — 20 / 20 — PASS

TC-004 — 20 / 20 — PASS

TC-005 — 19 / 20 — PASS

TC-006 — 20 / 20 — PASS

TC-007 — 20 / 20 — PASS

TC-008 — 19 / 20 — PASS

TC-009 — 20 / 20 — PASS

TC-010 — 20 / 20 — PASS

Cases Passed:

10 / 10

Aggregate:

198 / 200 available evaluation points

Material Defects:

0

Automatic Failures:

0

Promotion Result:

APPROVED

---

# 5. Current Defect Status

## E-005

Name:

Role / Context-Based Ownership Inference

Status:

CLOSED

Evidence:

- V0.5 targeted remediation TC-011 through TC-015 passed
- V0.6 preserved ownership controls
- broader regression completed without material E-005 recurrence

---

## E-006

Name:

Role-Supported Imperative Elevated to Formal Approval

Status:

CLOSED

Evidence:

- TC-006 V0.6 targeted regression passed
- decision-state protection passed
- broader regression completed without recurrence

---

# 6. Current Observations

## O-001

Description:

Potential overstatement of a proposal as Rejected where the source supported a current alternative outcome but did not explicitly state rejection.

First observed:

TC-005 V0.6

Severity:

Non-Material

Current Status:

MONITOR

Recurrence in TC-007 through TC-010:

None

---

## O-002

Description:

Plausible but unsupported predictive launch risk inferred from unresolved equipment and approval dependencies.

First observed:

TC-008 V0.6

Severity:

Non-Material

Current Status:

MONITOR

Recurrence:

Not observed in TC-009 or TC-010

---

# 7. Current Stage-1 Data Contract

Structured Extractor V0.7 outputs records using:

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

---

# 8. Current Record Types

Supported record types:

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

---

# 9. Current Decision-State Controls

Structured Extractor V0.7 must distinguish:

- Proposed
- Recommended
- Conditionally Approved
- Approved
- Rejected
- Deferred
- On Hold
- Superseded
- No Decision
- Not stated

Core rule:

Role, seniority, title, meeting leadership, expertise, or imperative wording alone do not establish formal approval authority.

Explicit source evidence is required.

---

# 10. Current Ownership Controls

Operational ownership must be record-specific.

Do not infer owner from:

- reporter identity,
- department,
- management title,
- functional responsibility,
- presumed hierarchy,
- organizational proximity.

Explicit assignments may establish ownership.

Approving Party and Operational Owner must remain independent.

---

# 11. Current Uncertainty Controls

Controlled certainty values include:

- Confirmed
- Approximate
- Estimated
- Unconfirmed
- Disputed
- Preliminary
- Under Investigation
- Calculated
- Reported
- Not stated

The extractor must preserve uncertainty rather than silently reconcile or strengthen source claims.

---

# 12. Current Stage-2 Controls

Executive Brief Generator V1.3 continues to use structured Stage-1 records as its source of truth.

Key controls include:

- Overall Status defaults to Not Determined unless explicitly supported
- no unsupported decisions
- no unsupported owners
- no unsupported deadlines
- no unsupported causality
- no unsupported predictions
- no scope expansion
- conflicts remain visible
- preliminary findings remain preliminary
- actions must come from supported action records
- open questions must remain source-supported
- human validation remains required

---

# 13. Claims Boundary

Current regression results support the statement:

Structured Extractor V0.7 passed the project's current internal regression and promotion controls.

They do not support claims of:

- 99% factual accuracy
- 100% accuracy
- production readiness
- autonomous reliability
- validated external-client performance
- validated time savings
- validated ROI
- zero-defect operation

Human validation remains required.

---

# 14. Current Baseline Summary

Structured Extractor:

V0.7 — CURRENT BASELINE

Executive Brief Generator:

V1.3 — CURRENT BASELINE

E-005:

CLOSED

E-006:

CLOSED

O-001:

MONITOR

O-002:

MONITOR

Broader Regression:

10 / 10 cases passed

Available Evaluation Points:

198 / 200

Production Readiness:

NOT CLAIMED

Human Review:

REQUIRED

---

REVIEW STATUS: CURRENT BASELINE UPDATED — STRUCTURED EXTRACTOR V0.7 + EXECUTIVE BRIEF GENERATOR V1.3

---

# Operational Validation Update — OVR-20260815-001

Date:

**August 15, 2026**

Baseline Evaluated:

- Structured Extractor V0.6
- Executive Brief Generator V1.3

Operational Run:

`operational-runs/OVR-20260815-001/`

Run Result:

**PASS WITH NON-MATERIAL CORRECTIONS**

---

## Why This Update Matters

The prior baseline regression result established that V0.6 / V1.3 passed the internal TC-001 through TC-010 regression suite.

That result remains valid.

However, OVR-20260815-001 introduced a fresh realistic operating-review source and evaluated the complete workflow rather than isolated regression cases.

This produced new evidence that changes how the baseline should be described.

---

## Stage-1 Operational Result

Structured Extractor V0.6:

**APPROVED — CORRECTED**

Corrections:

**8**

Material Corrections:

**0**

Automatic Failures:

**0**

Key Findings:

- E-005 ownership inference recurred in three records.
- O-001 decision-state semantic overreach recurred in four records.
- E-006 did not recur.
- O-002 did not recur.
- One new accountability-boundary behavior was observed and remains under monitoring.

E-005 Current Status:

**REOPENED**

O-001 Current Status:

**MONITOR — RECURRENCE CONFIRMED**

---

## Stage-2 Operational Result

Executive Brief Generator V1.3:

**APPROVED — CORRECTED**

Corrections:

**2**

Material Corrections:

**0**

Automatic Failures:

**0**

Key Findings:

- No unsupported material facts were introduced.
- No unsupported decisions were introduced.
- No unsupported owners were introduced.
- No unsupported deadlines were introduced.
- No unsupported client commitments were introduced.
- One attribution-compression behavior was observed.
- One leadership-attention over-prioritization behavior was observed.

Both Stage-2 behaviors remain observation candidates.

---

## End-to-End Operational Result

Final Run Status:

**PASS WITH NON-MATERIAL CORRECTIONS**

Total Human Corrections:

**10**

Material Corrections:

**0**

The workflow successfully demonstrated:

- source preservation,
- prompt-version traceability,
- original-output preservation,
- human Stage-1 validation,
- corrected Stage-1 input control,
- Stage-2 generation from validated records only,
- human Stage-2 validation,
- final approved brief creation,
- defect / observation traceability.

---

## Interpretation of Previous Regression Score

The prior result of:

**198 / 200 available evaluation points**

across TC-001 through TC-010 remains an accurate statement of the internal regression suite.

It must not be interpreted as:

- 99% real-world accuracy,
- 99% production reliability,
- a zero-defect baseline,
- proof that previously closed defects cannot recur.

OVR-20260815-001 demonstrated why broader operational validation remains necessary.

---

## Current Baseline Assessment

Structured Extractor V0.7:

**CURRENT BASELINE**

Executive Brief Generator V1.3:

**CURRENT BASELINE — STAGE-2 OBSERVATIONS UNDER MONITORING**

Product Maturity:

**Prototype — Internal Validation**

Human Review:

**REQUIRED**

Production Readiness:

**NOT CLAIMED**

Autonomous Reliability:

**NOT CLAIMED**

Client-Scale Reliability:

**NOT YET VALIDATED**

---

## Change-Control Decision

Do not modify the preserved OVR-20260815-001 artifacts.

Do not describe the current baseline as defect-free.

Future prompt changes must be evaluated separately through:

1. documented remediation,
2. targeted regression,
3. broader regression where appropriate,
4. additional operational validation.

---

# Operational Validation Update — OVR-20260815-002

Date:

**August 15, 2026**

Operational Run:

`operational-runs/OVR-20260815-002/`

Structured Extractor:

**V0.6**

Executive Brief Generator:

**V1.3**

Run Result:

**PASS WITH NON-MATERIAL CORRECTIONS**

---

## Stage-1 Result

Stage-1 Status:

**APPROVED — CORRECTED**

Total Stage-1 Corrections:

**15**

Material Corrections:

**0**

Correction Categories:

- Ownership: 6
- Decision State: 7
- Accountability: 1
- Classification: 1

Automatic Failure:

**NO**

---

## Stage-2 Result

Stage-2 Status:

**APPROVED — CORRECTED**

Total Stage-2 Corrections:

**6**

Material Corrections:

**0**

Correction Categories:

- Attribution Preservation: 1
- Leadership Prioritization: 1
- Open-Question Boundary: 4

Automatic Failure:

**NO**

---

# Cross-Run Findings

## E-005 — Role / Context-Based Ownership Inference

OVR-20260815-001:

**3 ownership corrections**

OVR-20260815-002:

**6 ownership corrections**

Current Assessment:

**REOPENED — SYSTEMATIC RECURRENCE SUPPORTED**

The original V0.6 regression closure remains historically valid, but fresh operational validation demonstrates that the defect was not behaviorally eliminated.

---

## E-007 — Unsupported Strong Decision-State Semantics

Formerly tracked as:

**O-001**

Evidence now spans:

- TC-005
- OVR-20260815-001
- OVR-20260815-002

Observed over-assigned controlled states include:

- Rejected
- No Decision
- Proposed
- Deferred

Current Assessment:

**OPEN FORMAL EXTRACTOR DEFECT**

The recurrence threshold for promotion from observation to formal defect has been met.

---

## E-006 — Role-Supported Imperative Elevated to Formal Approval

OVR-20260815-001:

**NO RECURRENCE**

OVR-20260815-002:

**NO RECURRENCE**

Current Assessment:

**CLOSED**

The V0.6 decision-authority controls continue to hold under operational validation.

---

## O-002 — Derived Predictive Risk Exceeds Literal Source

OVR-20260815-001:

**NO RECURRENCE**

OVR-20260815-002:

**NO RECURRENCE**

Current Assessment:

**MONITOR**

No evidence currently supports reopening or promotion.

---

## O-003 — Accountability-Boundary Overreach

OVR-20260815-001:

**OBSERVED**

OVR-20260815-002:

**RECURRENCE**

Current Assessment:

**FORMAL STAGE-1 OBSERVATION — MONITOR**

---

## O-004 — Attribution Compression

OVR-20260815-001:

**OBSERVED**

OVR-20260815-002:

**RECURRENCE**

Current Assessment:

**FORMAL STAGE-2 OBSERVATION — MONITOR**

---

## O-005 — Leadership-Attention Over-Prioritization

OVR-20260815-001:

**OBSERVED**

OVR-20260815-002:

**RECURRENCE**

Current Assessment:

**FORMAL STAGE-2 OBSERVATION — MONITOR**

---

# Current Single-Occurrence Candidates

## Stage 1

**Non-Contradictory Evidence Classified as Conflict**

First observed:

OVR-20260815-002

Current Status:

**MONITOR — OBSERVED ONCE**

---

## Stage 2

**Open-Question Boundary Expansion**

First observed:

OVR-20260815-002

Current Status:

**MONITOR — OBSERVED ONCE**

---

# Current Baseline Assessment

The historical V0.6 regression result remains:

**198 / 200 available evaluation points**

with:

- 10 / 10 regression cases passing
- 0 material defects in the completed regression suite
- 0 automatic failures

That result should not be reinterpreted as real-world accuracy.

Historical V0.6 operational validation established that:

- E-005 recurred under realistic operating material
- E-007 represented a systematic decision-state control issue
- O-003 recurred at Stage 1
- O-004 recurred at Stage 2
- O-005 recurred at Stage 2
- E-006 remained controlled
- O-002 did not recur operationally

Those findings informed the V0.7 remediation cycle described below.

Therefore:

Structured Extractor V0.6 remains the preserved historical baseline used for comparison and defect history.

Structured Extractor V0.7 is the current Stage-1 baseline.

V0.7 completed:

- targeted E-005 remediation validation
- targeted E-007 remediation validation
- E-006 protection validation
- broader regression
- controlled remediation
- full broader-regression rerun
- fresh operational validation
- formal promotion review

Final V0.7 validation results:

- 15 / 15 broader-regression cases passed
- 300 / 300 broader-regression points
- 5 / 5 fresh operational-validation cases passed
- 96 / 100 fresh-validation aggregate score
- 0 material defects
- 0 automatic failures
- 0 known remediated-defect recurrences
- 0 new systematic defects identified

Executive Brief Generator V1.3 remains the current Stage-2 baseline, with:

- O-004 under formal observation
- O-005 under formal observation

Human validation remains required.

---

# Product Maturity

Current Product Maturity:

**Prototype — Internal Validation**

Current evidence does not support claims of:

- production readiness
- autonomous operation
- zero-defect performance
- statistically validated accuracy
- client-ready reliability at scale

Future remediation should occur in new candidate prompt versions rather than by modifying preserved historical versions or their validation evidence.