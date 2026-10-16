# TC-012 Gold Standard

## Test Metadata

Test ID: TC-012
Business / Client: HarborView Property Services
Scenario: Changing Decisions and Partial Completion
Meeting Date: August 12, 2026
Difficulty: Level 2 — Difficult

Validation Phase:
Phase 2 — Unseen Validation

Baseline To Be Tested:

Structured Extractor V0.4

↓

Executive Brief Generator V1.3

Gold Standard Status:

LOCKED BEFORE FIRST EXECUTION

---

# 1. Test Objective

TC-012 evaluates whether the current baseline can correctly handle:

- revised dates,
- partially completed work,
- approved decisions that are later held or superseded,
- ambiguous authority,
- informal imperative language,
- dependencies,
- expectations versus formal targets,
- incomplete ownership,
- partially completed implementation activity.

The system should preserve the latest valid state without erasing relevant history.

---

# 2. Expected Material Facts

## Pilot Timing

- The pilot was originally planned for August 18.
- The pilot was moved to August 21.
- August 21 is the current target.
- The move occurred because two supervisors will be unavailable earlier in the week.

---

## Pilot Setup Checklist

- The setup checklist contains 24 items.
- 17 items are complete.
- Four items are in progress.
- Three items have not started.

The system should not represent the checklist as complete.

---

## Supervisor Training

- Training was originally scheduled for Friday.
- That timing became unsuitable because one supervisor is unavailable.
- Jenna suggested moving training to next Monday.
- Alicia approved moving training to next Monday.
- Training materials are already complete.

The current approved training timing is:

Next Monday

The original Friday timing is superseded.

---

## Access Permissions

- The access-permission update is still in progress.
- Owen said IT told him the permission changes should be finished tomorrow.
- Owen has not received confirmation.
- IT did not commit to a formal completion date.
- The pilot cannot begin until the access-permission update is complete.
- Jenna will verify permissions once IT confirms the change.

Expected interpretation:

Tomorrow is reported expected timing, not a committed IT deadline.

---

## Client Notification Email

- Owen drafted the client notification email last week.
- Alicia previously approved the draft.
- Marcus later requested that the email be held until the pilot date is confirmed.
- Alicia agreed to hold the notification.
- The prior approval to send the email is no longer active.
- Owen should not send the notification until Alicia authorizes release.

Expected interpretation:

The previous send approval is superseded / on hold.

The current state is:

Do not send.

No release authorization currently exists.

---

## Pilot Spending

- Pilot-related spending is approximately $14,600.
- Original pilot budget was $18,000.
- Temporary labor may add approximately $2,000 to $3,000 depending on next week's staffing.

Approximate values must remain approximate.

---

## Temporary Labor

- Marcus said, "Approve the extra labor if we need it."
- Alicia explicitly said no additional labor spending should be approved yet.
- Alicia requested a staffing estimate first.
- No additional temporary-labor budget was approved.
- Ravi will provide the staffing-cost estimate by Friday.

Expected interpretation:

Marcus's imperative statement must not be treated as final approval.

Alicia's later explicit direction controls.

---

## Contract Coordinators

- Marcus asked whether two contract coordinators could be added for the first week of the pilot.
- Jenna said that would probably help.
- No owner was assigned to evaluate the request.
- No decision was made.

Expected interpretation:

Do not create:
- an approved addition,
- an assigned evaluation action,
- an owner.

---

## Legacy Work-Order Forms

- Three legacy work-order forms are still being used by one field team.
- Marcus said, "Stop using those forms tomorrow."
- It is unclear whether Marcus had authority to issue that as a directive.
- Alicia did not explicitly approve or reject it.
- Jenna will confirm the transition plan with the field supervisor before changing anything.
- Jenna will report back at the next review.

Expected interpretation:

Marcus's statement must not be classified as Approved.

Expected decision state:

Not stated / unresolved authority.

The supported action is Jenna's confirmation of the transition plan.

---

## Dashboard Usage

- The new intake dashboard is already live for the pilot group.
- Usage is around 70%.
- Jenna expects usage to be above 90% by the end of next week.
- That is an expectation, not a formal target.

Expected interpretation:

Do not create an approved KPI target of 90%.

---

## User Feedback

- Several users told Owen the dashboard is easier to use than the old spreadsheet.
- No formal user-satisfaction survey has been completed.

Expected interpretation:

This is reported qualitative feedback, not validated satisfaction data.

---

## Next Review

- The next implementation review was originally August 19.
- Alicia approved moving it to August 20.
- August 19 is superseded.
- August 20, 2026 is the current review date.

---

# 3. Expected Decisions

## Approved

### Pilot Date

The current pilot target is August 21.

Expected Decision State:

Approved / current direction

---

### Supervisor Training Date

Move supervisor training to next Monday.

Expected Decision State:

Approved

---

### Hold Client Notification

Do not send the client notification until Alicia authorizes release.

Expected Decision State:

Approved current direction

The previous send approval is no longer active.

---

### Next Review Date

Move the next implementation review from August 19 to August 20.

Expected Decision State:

Approved

August 19 is superseded.

---

## No Decision / Not Approved

### Additional Temporary Labor Budget

No additional temporary-labor budget was approved.

Expected Decision State:

No Decision

The source explicitly blocks approval pending more information.

---

### Contract Coordinators

No decision was made to add two contract coordinators.

Expected Decision State:

No Decision

---

### Legacy Form Directive

Marcus's "Stop using those forms tomorrow" statement does not establish an approved decision.

Expected Decision State:

Not stated

Reason:

Authority and approval are unclear.

---

# 4. Expected Issues

The following may appropriately be represented as current issues:

## Pilot Setup Incomplete

Seven checklist items are not complete:

- four in progress,
- three not started.

---

## Access Permissions Incomplete

The permission update remains in progress.

---

## Legacy Forms Still in Use

Three legacy forms remain in use by one field team.

---

## Dashboard Adoption

Usage is around 70%.

This may be treated as a current adoption condition, but not automatically as an issue unless the source frames it negatively.

---

# 5. Expected Risks

No material future risk is explicitly stated as a formal risk.

The system should not automatically create risks from:

- incomplete permissions,
- staffing uncertainty,
- dashboard adoption,
- legacy-form usage.

These are current conditions, dependencies, or unresolved items.

---

# 6. Expected Actions

## A — Verify Access Permissions

Action:

Verify permissions once IT confirms the change.

Owner:

Jenna

Timing:

After IT confirmation

Dependency:

IT completes and confirms permission changes.

---

## B — Staffing Cost Estimate

Action:

Provide the temporary-labor staffing-cost estimate.

Owner:

Ravi

Deadline / Timing:

Friday

---

## C — Confirm Transition Plan

Action:

Confirm the legacy-form transition plan with the field supervisor before making changes.

Owner:

Jenna

Deadline / Timing:

Before any change to the legacy forms

---

## D — Report Back on Transition Plan

Action:

Report back on the legacy-form transition plan.

Owner:

Jenna

Deadline / Timing:

Next implementation review

---

# 7. Expected Partially Completed Work

The system should preserve progress state.

## Pilot Setup Checklist

24 total

17 complete

4 in progress

3 not started

Expected behavior:

Do not reduce this to "17 of 24 complete" if doing so causes loss of the in-progress/not-started distinction.

---

## Access Permissions

Status:

In progress

Expected behavior:

Do not mark complete based on IT's expected timing.

---

# 8. Expected Recommendations

## Training Date

Jenna recommended moving training to next Monday.

This recommendation was subsequently approved by Alicia.

The recommendation should not remain the latest decision state if the system tracks both history and current state.

---

## Contract Coordinators

Jenna said adding two contract coordinators would probably help.

Expected classification:

Recommendation / opinion

Decision Status:

No Decision

Do not convert into an action.

---

# 9. Expected Dependencies

## Pilot Start

Pilot cannot begin until access permissions are complete.

---

## Permission Verification

Jenna's verification depends on IT confirming the permission changes.

---

## Client Notification

Sending the client notification depends on Alicia authorizing release.

---

## Temporary Labor

Any future consideration of additional temporary labor depends on Ravi providing the staffing-cost estimate and subsequent approval.

---

## Legacy Form Change

Any change to legacy-form usage depends on Jenna confirming the transition plan with the field supervisor.

---

# 10. Expected Superseded States

The system should preserve latest state accurately.

## Pilot Date

Original:
August 18

Current:
August 21

August 18 should be treated as superseded.

---

## Training Date

Original:
Friday

Current:
Next Monday

Friday should be treated as superseded.

---

## Client Notification Approval

Original:
Alicia previously approved the draft for sending.

Current:
Notification is held.

The earlier send approval is superseded / inactive.

---

## Implementation Review

Original:
August 19

Current:
August 20

August 19 is superseded.

---

# 11. Ambiguous Authority Control

Marcus said:

"Stop using those forms tomorrow."

Expected behavior:

Do not classify as Approved.

Why:

- speaker authority for this action is unclear,
- Alicia did not approve or reject it,
- Jenna intends to confirm the transition plan before changing anything.

Expected state:

Not stated / unresolved.

---

# 12. Imperative Override Control

Marcus said:

"Approve the extra labor if we need it."

Alicia later said:

No additional labor spending should be approved yet.

Expected behavior:

The later explicit direction controls.

The system must not preserve Marcus's statement as an approved spending authorization.

---

# 13. Approximate Value Controls

Preserve:

- approximately $14,600 spent,
- approximately $2,000 to $3,000 possible temporary-labor cost,
- dashboard usage around 70%.

Do not strengthen these into exact confirmed values.

---

# 14. Expected Goal / Expectation Control

Jenna expects dashboard usage to exceed 90% by the end of next week.

Expected behavior:

Classify as:

Expectation / reported forecast

Do not classify as:

- approved target,
- formal goal,
- committed KPI,
- action deadline.

---

# 15. Expected Open Questions

Material unresolved questions may include:

- When will IT actually complete and confirm the permission changes?
- Will two contract coordinators be added?
- Is Marcus's directive to stop using the legacy forms authorized?

The system should avoid manufacturing additional open questions.

---

# 16. Expected Validation Controls

The final structured output should preserve or flag:

1. August 18 is superseded by August 21.
2. Friday training is superseded by next Monday.
3. 17 checklist items complete, 4 in progress, 3 not started.
4. IT's "tomorrow" timing is expected, not committed.
5. Pilot depends on permission completion.
6. Jenna verifies permissions only after IT confirms.
7. Client email send approval is no longer active.
8. Owen must not send until Alicia authorizes release.
9. Approximately $14,600 remains approximate.
10. Additional $2,000–$3,000 remains conditional and approximate.
11. Marcus's extra-labor imperative is overridden by Alicia's explicit direction.
12. No extra labor budget was approved.
13. No contract-coordinator decision was made.
14. No owner was assigned to evaluate contract coordinators.
15. Marcus's legacy-form imperative is not approved due to unclear authority.
16. Jenna must confirm transition plan before changes.
17. Dashboard usage around 70% remains approximate.
18. Above-90% usage is an expectation, not a target.
19. User feedback is qualitative and not survey-validated.
20. August 19 review is superseded by August 20.

---

# 17. Automatic-Fail Conditions Specific to TC-012

The test should automatically fail if the final brief materially:

- reports August 18 as the current pilot date,
- reports Friday as the current training date,
- marks access permissions complete,
- treats IT's "tomorrow" statement as a committed deadline,
- states the client notification is approved to send,
- states additional temporary labor was approved,
- assigns an owner to evaluate contract coordinators without support,
- states contract coordinators were approved,
- treats Marcus's legacy-form statement as an approved directive,
- treats 90% dashboard usage as a formal target,
- reports August 19 as the current implementation-review date,
- erases the distinction between complete, in-progress, and not-started checklist items.

---

# 18. Expected Executive-Brief Behavior

A successful Stage 2 output should allow leadership to understand:

- current pilot timing,
- implementation progress,
- incomplete permissions,
- client-communication hold,
- temporary-labor approval gate,
- unresolved coordinator request,
- ambiguous legacy-form directive,
- dashboard adoption,
- current review date.

It should clearly distinguish:

- what is complete,
- what is in progress,
- what is approved,
- what has been superseded,
- what is unresolved,
- what is merely expected.

---

# 19. Gold Standard Lock

This gold standard was established before the first V0.4 extraction of TC-012.

After the first execution begins:

- do not modify the standard to fit model output,
- preserve all first-run discrepancies,
- document defects separately,
- keep V0.4 / V1.3 locked for the current unseen batch.

Gold Standard Status:

LOCKED