# Business & Technology Portfolio — Development & Time Log

This log tracks time invested across technical learning, portfolio development, evaluation, documentation.

Its purpose is to provide a clear record of:

- technical capability development
- featured-project progression
- product reasoning and decision-making
- evaluation and experimentation work
- portfolio documentation
- technical and product learning

Progress is tracked by **session number rather than calendar day**.

Multiple sessions may be completed on the same day, and gaps between sessions do not affect the learning sequence. Calendar dates are retained for time accounting and project history, while session numbers reflect the actual order of development.

---

# Summary

## Technical Learning by Area

| Category | Hours |
|---|---:|
| Foundations | 0.0 |
| Python | 7.33 |
| Data Analysis | 0.50 |
| Machine Learning | 0.0 |
| Applied AI | 1.0 |
| AI Systems | 0.0 |
| **Total Learning Time** | **8.83** |

> Learning-area hours represent the technical capability developed during portfolio work. Project hours are tracked separately below because the same session may simultaneously contribute to both technical learning and a featured project. These totals should not be added together.

---

# Portfolio Investment by Project

| Project | Status | Hours |
|---|---|---:|
| Executive Brief Generator | In Progress | 44.50 |
| Business Performance & Margin Improvement Diagnostic | In Progress | 0.50 |
| Document Q&A RAG Assistant | In Progress | 3.50 |
| Support Triage System | Complete | 7.83 |
| **Total Portfolio Project Time** |  | **56.33** |

> Portfolio project hours represent verified time invested in building, testing, evaluating, and documenting featured projects. Some projects began before the current structured session sequence; verified historical development time is included where an existing project time log is available.

> Technical Learning hours and Portfolio Project hours measure different dimensions of the work and should not be added together. Technical Learning currently reflects the structured learning sessions tracked in this portfolio, while Portfolio Project hours may also include verified development completed before those sessions began.

---

# Session Log

## September 2026

### Session 1 — Ticket Triage Foundations

**Date:** September 27, 2026  
**Area:** Python Foundations  
**Project:** Support Triage System  
**Duration:** 50 minutes

**Concept Tags:** PCEP Core · Practical / Portfolio

### Objective

Build a simple deterministic support-ticket classification system using Python.

### Work Completed

- Created ticket dataset
- Built `classify_ticket()` function
- Used `if / elif / else`
- Applied Boolean logic
- Iterated through tickets
- Counted classification outcomes
- Documented exercise in README
- Created Git feature branch
- Committed changes
- Opened and merged pull request

### Technical Concepts

- Dictionaries
- Functions
- Conditionals
- Boolean operators
- Loops
- Basic aggregation
- Git branches
- Pull requests

### Lessons Learned

Rule ordering matters when multiple conditions can match the same input.

The most restrictive or highest-priority condition should be evaluated first so that a broader rule does not incorrectly capture a case intended for a more important classification.

### Product & Strategy Application

A deterministic rules-based system can provide a transparent baseline before introducing machine learning.

This makes it possible to evaluate whether additional model complexity creates enough measurable product value to justify higher cost, lower explainability, or additional operational complexity.

---

### Session 2 — Variables, Booleans & SLA Logic

**Date:** September 27, 2026  
**Area:** Python Foundations  
**Project:** Support Triage System  
**Duration:** 30 minutes

**Concept Tags:** PCEP Core · PCAP Foundation · Practical / Portfolio

### Objective

Understand variables, data types, comparison operators, Boolean values, function return behavior, and reusable business logic by adding SLA breach detection.

### Work Completed

- Added `is_sla_breached()` function
- Retrieved values from ticket dictionaries
- Defined an SLA business-rule threshold
- Compared ticket age against the SLA threshold
- Returned Boolean SLA status
- Integrated SLA status into ticket output
- Debugged a missing dictionary brace
- Corrected indentation issues
- Reinforced the difference between `print()` and `return`
- Separated ticket priority from SLA compliance

### Technical Concepts

- Variables
- Dictionaries
- Integers
- Strings
- Booleans
- Comparison operators
- Functions
- `return`
- Type hints
- Indentation
- Syntax debugging
- Business-rule separation

### Lessons Learned

Comparison expressions return Boolean values: `True` or `False`.

Business-rule thresholds should be separated from record-specific data so the logic remains clear, reusable, and easy to modify.

A Python `SyntaxError` may point to where Python finally recognizes a problem rather than the exact location where the error originally occurred.

`print()` displays a value to the user, while `return` sends a value back to the code that called the function.

### Product & Strategy Application

Priority and SLA compliance represent different product dimensions.

Priority reflects the **business urgency** of a ticket, while SLA status reflects whether a **service commitment** has been met.

Keeping these dimensions separate makes the system easier to reason about, modify, measure, and eventually evaluate against more advanced approaches.

### Session 3 — Loops, Collections & Reusable Decision Logic

**Date:** September 29, 2026  
**Area:** Python Foundations  
**Project:** Support Triage System  
**Duration:** 30 minutes

**Concept Tags:** PCEP Core · Practical / Portfolio

### Objective

Understand how Python lists and `for` loops can repeatedly apply reusable decision logic across multiple support-ticket records.

### Work Completed

- Reviewed variables, Booleans, dictionary access, functions, and `return`
- Reinforced the distinction between values and data types
- Distinguished lists from dictionaries
- Practiced tracing `for` loops manually
- Applied `is_sla_breached()` across multiple tickets
- Added SLA-based review routing
- Consolidated classification and SLA logic into one ticket-processing loop
- Verified classification counts remained correct
- Identified a potential stale-variable / execution-scope failure mode

### Technical Concepts

- Lists
- Dictionaries
- `for` loops
- Iteration
- Dictionary key access
- Function reuse
- Boolean conditions
- `if`
- Variable scope
- Execution frequency
- Aggregation
- Code tracing
- Logical debugging

### Lessons Learned

A `for` loop processes one item from a collection at a time, with the loop variable representing the current item. Logic that must execute for every record needs to remain inside the loop.

Code can be syntactically valid while still producing incorrect behavior if logic executes at the wrong scope or frequency.

### Product & Strategy Application

The triage prototype now behaves as a simple decision pipeline: each ticket is classified, evaluated for SLA status, conditionally routed for review, and included in aggregate metrics.

This provides a deterministic baseline that can later be compared against ML-assisted classification or routing approaches.

### Session 4 — Boolean Logic & Compound Decision Rules

**Date:** September 30, 2026  
**Duration:** 30 minutes  
**Project:** Support Triage System  
**Learning Area:** Python Foundations

## Objective

Strengthen Boolean logic and combine multiple conditions to create more precise escalation decisions.

## Work Completed

- Reviewed `and`, `or`, and `not`
- Practiced compound Boolean expressions
- Combined ticket classification with SLA status
- Added escalation logic requiring both a `HIGH` classification and a breached SLA

Implemented:

    if result == "HIGH" and sla_status:
        print(ticket["id"], "requires escalation")

Validated that only `T001` and `T006` met both escalation conditions.

## Technical Concepts

- Boolean expressions
- `and`
- `or`
- `not`
- compound conditions
- nested decision logic

## Product Capability Developed

Developed the ability to combine multiple operational signals into one product decision.

The system now distinguishes between tickets requiring SLA review and tickets requiring escalation.

## Product Decision / Insight

A single signal is often insufficient for a meaningful automated decision. An SLA breach alone may not justify escalation, and a HIGH-priority ticket alone may not have breached service expectations.

## Failure Mode / Edge Case

Using `or` instead of `and` would significantly increase escalation volume by escalating tickets that satisfy only one condition.

## Lessons Learned

- `and` requires both conditions to be true
- `or` requires only one condition to be true
- Boolean operators directly encode business policy
- small logical changes can materially change product behavior

---

### Session 5 — Lists as Working Queues

**Date:** September 30, 2026  
**Duration:** 30 minutes  
**Project:** Support Triage System  
**Learning Area:** Python Foundations

## Objective

Use Python lists to persist escalation decisions and create a reusable working queue.

## Work Completed

Created an empty escalation queue:

    escalation_queue = []

Added qualifying ticket IDs:

    if result == "HIGH" and sla_status:
        escalation_queue.append(ticket["id"])
        print(ticket["id"], "requires escalation")

Added aggregate output after all tickets were processed:

    print("Escalation Queue:", escalation_queue)
    print("Escalation Count:", len(escalation_queue))

Validated:

    Escalation Queue: ['T001', 'T006']
    Escalation Count: 2

## Technical Concepts

- empty lists
- `.append()`
- `len()`
- list methods
- loop scope
- aggregation
- storing results for later use

## Product Capability Developed

Moved the system from printing individual decisions to maintaining a reusable operational output.

The escalation queue can later support:

- human review
- ticket assignment
- reporting
- workflow integrations
- escalation metrics

## Product Decision / Insight

A decision system becomes more useful when its outputs can be stored and consumed by another process. Printing a decision communicates an event; maintaining a queue creates structured output that another workflow can use.

## Failure Mode / Edge Case

Placing aggregate queue output inside the loop produces incomplete intermediate results. The queue must also be initialized outside the loop so earlier results are preserved.

## Lessons Learned

- `.append()` adds an item to a list
- `len()` returns the number of elements
- list initialization location matters
- code inside a loop executes once per item
- aggregate outputs usually belong after the loop

---

### Session 6 — Indexing, Membership & Duplicate Prevention

**Date:** September 30, 2026  
**Duration:** 30 minutes  
**Project:** Support Triage System  
**Learning Area:** Python Foundations

## Objective

Learn list indexing and membership checks while protecting the escalation workflow from duplicate entries.

## Work Completed

Reviewed:

- zero-based indexing
- `in`
- `not in`
- nested `if` statements

Added duplicate prevention:

    if result == "HIGH" and sla_status:
        if ticket["id"] not in escalation_queue:
            escalation_queue.append(ticket["id"])

        print(ticket["id"], "requires escalation")

Validated:

    Escalation Queue: ['T001', 'T006']
    Escalation Count: 2

## Technical Concepts

- zero-based indexing
- list membership
- `in`
- `not in`
- nested conditions
- duplicate prevention
- `IndexError`
- basic idempotency

## Product Capability Developed

Introduced protection against duplicate downstream actions.

This is an early example of idempotent workflow behavior: repeated processing should not create unintended duplicate effects.

## Product Decision / Insight

Duplicate prevention matters because repeated automated actions can create duplicate escalations, notifications, assignments, incorrect reporting, and unnecessary operational work.

## Failure Mode / Edge Case

Without:

    ticket["id"] not in escalation_queue

the same ticket could be added multiple times if the routing logic were executed repeatedly.

Attempting to access a list position that does not exist can also produce an `IndexError`.

## Lessons Learned

- Python indexing begins at `0`
- `in` tests whether a value exists
- `not in` tests whether a value does not exist
- nested conditions allow more precise logic
- duplicate prevention is both a programming and product-reliability concern

---

### Session 7 — Functions, Parameters & Reusable Routing Logic

**Date:** September 30, 2026  
**Duration:** 30 minutes  
**Project:** Support Triage System  
**Learning Area:** Python Foundations

## Objective

Refactor escalation logic into a reusable function and strengthen understanding of parameters, arguments, return values, and separation of concerns.

## Work Completed

Created:

    def should_escalate(result: str, sla_status: bool) -> bool:
        return result == "HIGH" and sla_status

Replaced the inline escalation condition with:

    if should_escalate(result, sla_status):
        if ticket["id"] not in escalation_queue:
            escalation_queue.append(ticket["id"])

        print(ticket["id"], "requires escalation")

Validated the complete workflow:

    T001 requires SLA review
    T001 requires escalation
    T001 -> HIGH | SLA Breached: True
    T002 -> NORMAL | SLA Breached: False
    T003 -> CRITICAL | SLA Breached: False
    T004 requires SLA review
    T004 -> NORMAL | SLA Breached: True
    T005 requires SLA review
    T005 -> NORMAL | SLA Breached: True
    T006 requires SLA review
    T006 requires escalation
    T006 -> HIGH | SLA Breached: True
    {'CRITICAL': 1, 'HIGH': 2, 'NORMAL': 3}
    Escalation Queue: ['T001', 'T006']
    Escalation Count: 2

## Technical Concepts

- function definition
- parameters
- arguments
- Boolean return values
- type hints
- reusable decision logic
- function placement
- separation of concerns
- refactoring

## Product Capability Developed

Separated escalation policy from workflow execution.

Instead of embedding the business rule directly inside the processing loop, the system now expresses it through:

    should_escalate(...)

This makes the rule easier to understand, modify, test, reuse, and explain.

## Product Decision / Insight

Business rules should be isolated from workflow execution where practical.

This improves maintainability because the escalation policy can change without requiring the entire processing loop to be redesigned.

## Failure Mode / Edge Case

Function placement and indentation matter. Defining the function in the wrong location or placing workflow logic after a `return` statement can create unreachable or incorrectly scoped code.

Parameter and argument terminology also requires continued reinforcement:

- **Parameter** = placeholder defined by the function
- **Argument** = actual value supplied when calling it

Example:

    should_escalate("HIGH", True)

Here:

- `result` and `sla_status` are parameters
- `"HIGH"` and `True` are arguments

## Lessons Learned

- functions make decision logic reusable
- parameters define what information a function needs
- arguments provide the actual values
- `return` sends a value back to the caller
- Boolean functions are useful for business decision rules
- refactoring improves readability and maintainability

### Session 8 — Input Validation & Defensive Decision Logic

**Date:** October 2, 2026  
**Duration:** 30 minutes  
**Project:** Support Triage System  
**Learning Area:** Python Foundations

## Objective

Add input validation to the ticket-triage workflow so incomplete tickets are identified before classification, SLA evaluation, and escalation logic.

## Work Completed

Created a required-fields list:

    required_fields = [
        "id",
        "category",
        "priority",
        "age_hours",
        "customer_tier"
    ]

Created a reusable validation function:

    def has_required_fields(ticket: dict) -> bool:
        for field in required_fields:
            if field not in ticket:
                return False

        return True

Tested the validation function against both an incomplete ticket and an existing valid ticket:

    print("Invalid Ticket Valid:", has_required_fields(invalid_ticket))
    print("Existing Ticket Valid:", has_required_fields(tickets[0]))

Validated the expected result:

    Invalid Ticket Valid: False
    Existing Ticket Valid: True

Integrated validation into the main processing loop:

    for ticket in tickets:
        if not has_required_fields(ticket):
            print(ticket.get("id", "UNKNOWN"), "has missing required fields")
            continue

Added an intentionally incomplete ticket:

    {
        "id": "T007",
        "category": "billing",
        "priority": 4
    }

Validated the complete workflow:

    Invalid Ticket Valid: False
    Existing Ticket Valid: True
    T001 requires SLA review
    T001 requires escalation
    T001 -> HIGH | SLA Breached: True
    T002 -> NORMAL | SLA Breached: False
    T003 -> CRITICAL | SLA Breached: False
    T004 requires SLA review
    T004 -> NORMAL | SLA Breached: True
    T005 requires SLA review
    T005 -> NORMAL | SLA Breached: True
    T006 requires SLA review
    T006 requires escalation
    T006 -> HIGH | SLA Breached: True
    T007 has missing required fields
    {'CRITICAL': 1, 'HIGH': 2, 'NORMAL': 3}
    Escalation Queue: ['T001', 'T006']
    Escalation Count: 2

## Technical Concepts

- input validation
- required fields
- dictionary membership
- `in`
- `not in`
- `.get()`
- fallback values
- Boolean validation functions
- `not`
- `continue`
- fail-fast logic
- defensive programming
- control flow

## Product Capability Developed

Added a validation layer before downstream decision logic.

Instead of assuming that every incoming ticket contains complete data, the system now checks whether the required fields exist before attempting classification.

The workflow now follows:

    Input
      ↓
    Validation
      ↓
    Valid? ── No → Flag and skip
      ↓ Yes
    Classification
      ↓
    SLA Evaluation
      ↓
    Escalation

This makes the workflow more resilient to malformed or incomplete input.

## Product Decision / Insight

Invalid inputs should be stopped before they enter downstream business logic.

Once a ticket has already been determined to be incomplete, continuing into classification or SLA processing creates unnecessary work and increases the risk of runtime errors or incorrect decisions.

Validation therefore acts as a control layer protecting the rest of the workflow.

## Failure Mode / Edge Case

Attempting to process a ticket without all required fields can cause downstream failures.

For example:

    ticket["age_hours"]

will raise a `KeyError` if `"age_hours"` does not exist.

The validation function prevents this by checking each required key before processing continues.

Dictionary membership also required reinforcement:

    "priority" in ticket

checks whether `"priority"` exists as a **key**, not whether a particular value exists.

Safe dictionary access also required reinforcement:

    ticket.get("id", "UNKNOWN")

means:

- return the value associated with `"id"` if the key exists
- return `"UNKNOWN"` if the key does not exist

`continue` changes control flow by immediately ending the current loop iteration and moving to the next ticket.

## Lessons Learned

- validate incoming data before applying business logic
- dictionary membership checks keys rather than values
- `not in` is useful for detecting missing required fields
- `.get()` provides safer dictionary access when a key may be missing
- Boolean functions can encapsulate validation rules
- `not` reverses a Boolean result
- `continue` skips the remainder of the current loop iteration
- fail-fast logic prevents unnecessary downstream processing
- validation improves reliability and makes workflow failures easier to control

### Session 9 — RAG Migration, Evaluation & Portfolio Reconciliation

**Date:** October 2, 2026  
**Duration:** 1 hour  
**Project:** Document Q&A RAG Assistant  
**Learning Area:** Applied AI

## Objective

Reconcile an existing RAG prototype with its public portfolio narrative by inspecting the implemented retrieval architecture, evaluation evidence, current limitations, and development history.

## Work Completed

- Migrated and reviewed the existing Document Q&A RAG Assistant
- Inspected the implemented retrieval pipeline
- Verified local embedding and ChromaDB retrieval architecture
- Reviewed semantic retrieval and reranking behavior
- Reviewed the existing controlled five-question retrieval evaluation
- Identified the documented 4/5 initial retrieval baseline
- Distinguished implemented capabilities from planned answer-generation features
- Documented cross-page and chunk-boundary retrieval failure modes
- Reframed the project as a retrieval-first RAG prototype
- Reconciled the README with the actual implementation state
- Added a structured evaluation narrative
- Documented current bottlenecks and production-readiness gaps

## Technical Concepts

- Retrieval-Augmented Generation
- document ingestion
- text chunking
- embeddings
- vector search
- ChromaDB
- semantic retrieval
- candidate retrieval
- reranking
- cross-encoders
- source attribution
- retrieval evaluation
- Recall@K
- Precision@K
- Mean Reciprocal Rank
- grounding
- chunk-boundary failure
- cross-page context
- regression testing

## Product Capability Developed

Strengthened the ability to evaluate an AI product based on what the system actually implements rather than what its intended architecture claims.

The project now clearly separates:

    Retrieval Layer
        ↓
    Evaluation
        ↓
    Evidence Quality
        ↓
    Future Generation Layer

This creates a more defensible product-development sequence because answer generation is intentionally deferred until retrieval quality is sufficiently understood.

## Product Decision / Insight

RAG quality is not primarily an LLM problem.

If the retrieval system supplies incomplete, irrelevant, or poorly ranked evidence, a stronger generation model cannot reliably recover information that never entered its context.

For this project, retrieval evaluation therefore precedes answer-generation development.

## Failure Modes / Edge Cases

The review identified several unresolved retrieval risks:

- relevant evidence split between chunks
- logical sections spanning PDF pages
- correct evidence appearing with excessive surrounding context
- relevant chunks retrieved but ranked too low
- heuristic evidence selection removing useful information
- small evaluation sets creating misleading confidence in retrieval quality

## Lessons Learned

- implementation evidence should determine portfolio claims
- retrieval and generation quality should be evaluated separately
- a successful retrieval result is not equivalent to a successful RAG answer
- small evaluation sets are useful for development but not sufficient for production validation
- reranking can improve relevance without fixing incomplete underlying chunks
- architecture documentation should clearly distinguish current capability from planned capability

---


### Session 10 — Value Validation & Defensive Business Rules

**Date:** October 2, 2026  
**Duration:** 30 minutes  
**Project:** Support Triage System  
**Learning Area:** Python Foundations

## Objective

Extend ticket validation beyond required-field checks by validating whether incoming values satisfy defined business rules before downstream processing.

## Work Completed

- Added an intentionally malformed ticket with invalid business values
- Demonstrated that required-field validation alone can allow invalid data downstream
- Created `has_valid_values()` as a separate validation function
- Added priority-range validation
- Added non-negative ticket-age validation
- Added supported customer-tier validation
- Tested invalid priority, age, and customer-tier scenarios
- Integrated value validation into the main processing loop
- Used `continue` to stop invalid records before classification, SLA evaluation, aggregation, or escalation
- Removed temporary validation test data after confirming expected behavior

## Technical Concepts

- value validation
- range checks
- list membership
- Boolean functions
- defensive programming
- fail-fast control flow
- `continue`
- separation of concerns
- input quality
- business-rule validation

## Product Capability Developed

Expanded the triage workflow from structural validation to layered input validation.

The processing flow now follows:

    Input
      ↓
    Required Fields Present?
      ↓
    Values Valid?
      ↓
    Classification
      ↓
    SLA Evaluation
      ↓
    Escalation

Invalid records are prevented from influencing downstream decisions or aggregate metrics.

## Product Decision / Insight

A record can be structurally complete while still containing invalid business data.

Separating required-field validation from value validation makes failures easier to diagnose, rules easier to modify, and downstream decision logic more reliable.

## Failure Modes / Edge Cases

Testing exposed several data-quality risks:

- priority values outside the supported range
- negative ticket age
- unsupported customer tiers
- syntactically valid records influencing metrics despite invalid business values
- malformed temporary test structures producing Python type errors

## Lessons Learned

- field presence and field validity are different concerns
- validation should occur before downstream decision logic
- invalid records should fail fast
- `continue` prevents rejected records from affecting later processing
- separate validation functions improve clarity and maintainability
- syntactically valid data can still be operationally invalid

---


### Session 11 — Type Validation & Defensive Input Handling

**Date:** October 3, 2026  
**Duration:** 30 minutes  
**Project:** Support Triage System  
**Learning Area:** Python Foundations


## Objective

Add explicit data-type validation so malformed values are rejected before business-value comparisons or downstream decision logic can execute.

## Work Completed

- Added `T009` with an intentionally invalid priority type
- Reproduced a `TypeError` caused by comparing a string priority against integers
- Added `has_valid_types()` using `isinstance()`
- Validated expected types for ticket ID, category, priority, age, and customer tier
- Inserted type validation between required-field validation and value validation
- Corrected validation-order bugs in the main processing loop
- Confirmed distinct failure handling for missing fields, invalid values, and invalid data types
- Verified invalid records no longer affect classification counts or escalation results

## Technical Concepts

- `isinstance()`
- Python data types
- type validation
- `TypeError`
- validation ordering
- defensive programming
- fail-fast control flow
- separation of concerns
- input contracts
- downstream dependency protection

## Product Capability Developed

Expanded the support-triage validation pipeline from two layers to three:

    Input
      ↓
    Required Fields Present?
      ↓
    Correct Data Types?
      ↓
    Values Valid?
      ↓
    Classification
      ↓
    SLA Evaluation
      ↓
    Escalation

Each validation stage establishes a guarantee required by the next stage.

## Product Decision / Insight

Validation order is part of system design.

A value-range check cannot safely execute until the system knows:

1. the required field exists
2. the field contains a compatible data type

Type validation therefore protects both business logic and system reliability.

## Failure Modes / Edge Cases

- missing keys can cause `KeyError`
- incompatible types can cause `TypeError`
- correctly typed values can still violate business rules
- incorrect validation ordering can allow malformed records downstream
- calling the wrong validation function can make error messages misleading

## Lessons Learned

- structural validity, type validity, and business-value validity are separate concerns
- `isinstance()` checks whether a value matches an expected Python type
- validation layers should execute in dependency order
- `continue` prevents rejected records from reaching downstream processing
- classification should occur only after every validation layer passes
- aggregate metrics should contain only successfully validated records

---


### Session 12 — Exceptions & Controlled Error Handling

**Date:** October 5, 2026  
**Duration:** 1.0 hour  
**Project:** Support Triage System  
**Learning Area:** Python Foundations

## Objective

Understand how Python exception handling complements preventive input validation and use controlled failure handling to keep a ticket-processing workflow operational when unexpected runtime errors occur.

## Work Completed

- reproduced an unhandled `KeyError` using direct dictionary access
- added a targeted `try / except KeyError` handler
- captured the exception object using `as error`
- compared direct dictionary access with `.get()` fallback behavior
- integrated exception handling into the main ticket-processing loop
- handled both `KeyError` and `TypeError`
- debugged a `SyntaxError` caused by using `continue` outside a loop
- corrected the exception handler's scope and placement
- injected a controlled `TypeError` into T003 to validate the recovery path
- verified the workflow continued processing subsequent tickets after the simulated failure
- observed the effect of failed processing on aggregate classification metrics
- removed the simulated failure and restored the expected baseline output

## Technical Concepts

- `try`
- `except`
- `KeyError`
- `TypeError`
- exception objects
- `raise`
- targeted exception handling
- loop control with `continue`
- dictionary access
- defensive programming
- graceful degradation
- failure isolation
- metric integrity

## Product Capability Developed

The triage workflow now separates preventive validation from runtime-failure containment.

    Raw Ticket
        ↓
    Required-Field Validation
        ↓
    Type Validation
        ↓
    Business-Value Validation
        ↓
    Protected Processing
        ↓
    Classification + SLA Evaluation
        ↓
    Runtime Failure?
       ↙       ↘
     Yes        No
      ↓          ↓
    Handle     Continue
    + Skip     Workflow
        ↓
    Metrics / Escalation

Known malformed inputs are rejected before processing, while unexpected processing failures can be contained without terminating the entire workflow.

## Product Decision / Insight

Validation and exception handling solve different reliability problems.

Validation prevents known invalid states from reaching downstream logic.

Exception handling protects the application when a runtime failure still occurs despite preventive controls.

A handled failure can preserve system availability while still changing downstream metrics. During controlled failure injection, T003 was excluded from classification results and the CRITICAL count changed from one to zero.

This demonstrates that graceful degradation must be paired with observability and explicit policies for failed records.

## Failure Modes / Edge Cases

- direct dictionary access to a missing key can raise `KeyError`
- incompatible operations can raise `TypeError`
- broad exception handling can hide unrelated defects
- `continue` cannot execute outside a loop
- incorrect indentation can place exception handling outside its intended processing scope
- failed records may silently distort aggregate metrics if failure counts are not tracked separately
- exception handling can preserve availability without guaranteeing data completeness

## Lessons Learned

- validation should remain the primary defense against known bad input
- exception handling is a secondary safety layer for runtime failures
- specific exception classes are preferable to indiscriminate exception catching
- `as error` provides access to the actual exception object
- `continue` allows one failed record to be isolated without stopping the complete batch
- controlled failure injection is useful for validating recovery behavior
- successful error handling does not automatically mean downstream metrics remain representative
- reliability design must account for both application continuity and data integrity

---


### Session 13 — File I/O & Persistent Data

**Date:** October 7, 2026  
**Duration:** 1.0 hour  
**Project:** Support Triage System  
**Learning Area:** Python Foundations

## Objective

Move the ticket-triage workflow beyond hard-coded in-memory data by introducing persistent file input/output, structured JSON ingestion, reusable file-loading logic, and controlled handling of external-data failures.

## Work Completed

- created and read an external text file using `open(..., "r")`
- used `.read()` and `.strip()` to load and clean text content
- wrote workflow results to a text file using `"w"` mode
- appended additional results using `"a"` mode
- used `with open(...)` context managers for automatic resource cleanup
- created and loaded a single JSON ticket using `json.load()`
- serialized a Python dictionary to JSON using `json.dump()`
- formatted JSON output with `indent=2`
- loaded a JSON array into a Python `list[dict]`
- accessed nested list and dictionary values
- routed JSON-loaded tickets through existing classification and SLA logic
- reused existing required-field, type, and value validation for externally loaded records
- created `process_ticket()` to establish a single reusable ticket-processing path
- moved `import json` to the module import section
- introduced `BASE_PATH` to centralize shared file-path configuration
- handled missing input files with `FileNotFoundError`
- handled malformed JSON with `json.JSONDecodeError`
- tested both failure paths using controlled failure injection
- restored valid input and confirmed normal behavior
- extracted file-loading behavior into `load_tickets_from_json()`
- added a `list[dict]` return type hint to the loader

## Technical Concepts

- file I/O
- persistent data
- `open()`
- read mode (`"r"`)
- write mode (`"w"`)
- append mode (`"a"`)
- context managers
- `.read()`
- `.write()`
- `.strip()`
- JSON
- `json.load()`
- `json.dump()`
- serialization
- deserialization
- JSON arrays
- nested data access
- `list[dict]`
- centralized configuration
- file paths
- `FileNotFoundError`
- `JSONDecodeError`
- graceful degradation
- controlled failure testing
- reusable ingestion functions
- DRY
- separation of concerns

## Product Capability Developed

The triage workflow can now consume externally stored structured data rather than depending entirely on records embedded directly in the Python source code.

The ingestion architecture now follows:

    External JSON File
            ↓
    load_tickets_from_json()
            ↓
    JSON Parsing
            ↓
    Python list[dict]
            ↓
    process_ticket()
            ↓
    Required-Field Validation
            ↓
    Type Validation
            ↓
    Value Validation
            ↓
    Classification + SLA Evaluation

File ingestion and ticket processing are now separate responsibilities.

`load_tickets_from_json()` owns external file access, JSON parsing, and file-related recovery behavior.

`process_ticket()` owns ticket validation and business processing.

This creates a cleaner boundary for replacing file-based input later with APIs, databases, queues, or uploaded files without rewriting the underlying ticket-processing logic.

## Product Decision / Insight

External inputs should not be trusted simply because they were successfully loaded.

A production-oriented ingestion workflow must account for both:

1. failures in the transport or storage layer, such as a missing file
2. failures in the data representation layer, such as malformed JSON

Successfully parsing a record also does not make that record business-valid. The existing validation pipeline must still run before automated decisions or metrics are produced.

Separating ingestion from processing reduces coupling and makes future integration changes safer.

## Failure Modes / Edge Cases

- incorrect file paths can raise `FileNotFoundError`
- a file may exist while containing malformed JSON
- malformed JSON raises `json.JSONDecodeError`
- direct list indexing after a failed load can create a secondary `IndexError`
- `"w"` mode overwrites existing file contents
- output files without a trailing newline can produce awkward terminal formatting
- duplicated processing logic can cause the same ticket to be processed multiple times
- repeated hard-coded paths increase maintenance risk
- external data may parse successfully while still failing structural, type, or business-value validation

## Lessons Learned

- `r` reads existing data
- `w` writes and replaces existing contents
- `a` appends to existing contents
- `with open(...)` automatically manages file cleanup
- `.strip()` removes leading and trailing whitespace from strings
- `json.load()` converts JSON file content into Python objects
- `json.dump()` serializes Python objects into JSON
- JSON arrays naturally map to Python lists
- JSON objects naturally map to Python dictionaries
- external records should pass through the same validation path as in-memory records
- targeted exception handling can preserve workflow continuity during ingestion failures
- controlled failure testing verifies recovery behavior rather than assuming it works
- centralized paths reduce duplicated configuration
- reusable loader and processing functions improve separation of concerns
- DRY reduces the risk of inconsistent behavior across multiple ingestion paths

---

## October 2026

### Session 14 — Modules, Imports & Basic Testing

**Date:** October 11, 2026  
**Area:** Python Foundations  
**Project:** Support Triage System  
**Duration:** 1 hour

### Objective

Strengthen the Support Triage System architecture through modularization, imports, and automated testing.

### Work Completed

- separated ticket classification, SLA, and escalation logic into reusable modules
- separated validation logic from orchestration
- introduced `main()` and the execution guard
- prevented import-time side effects
- added structured `unittest` coverage
- confirmed 9 automated tests passing
- reinforced separation of concerns

### Technical Concepts

- Python modules
- imports
- separation of concerns
- `main()`
- `if __name__ == "__main__"`
- `unittest`
- regression testing

---

### Session 15 — Support Triage v1 Completion

**Date:** October 11, 2026  
**Area:** Python Foundations / Portfolio Development  
**Project:** Support Triage System  
**Duration:** 30 minutes

### Objective

Close the Support Triage System as a completed supporting portfolio project.

### Work Completed

- ran the full automated test suite
- confirmed 9 of 9 tests passing
- completed the project README
- documented architecture, validation, testing, business value, limitations, and future opportunities
- marked Support Triage System v1 complete

---

### Session 16 — Business Performance Diagnostic & Pandas Foundations

**Date:** October 11, 2026  
**Area:** Data Analysis  
**Project:** Business Performance & Margin Improvement Diagnostic  
**Duration:** 30 minutes

### Objective

Begin the Business Performance & Margin Improvement Diagnostic while applying introductory Pandas concepts to a real business analysis.

### Work Completed

- selected Toast as the case company
- defined the management question and decision criteria
- documented project and data requirements
- created the initial 2023–2025 financial dataset
- loaded and inspected data with Pandas
- calculated gross profit and gross margin
- calculated year-over-year revenue growth
- calculated segment gross margins
- analyzed revenue mix and mix changes
- calculated gross-profit contribution by segment
- reconciled calculations to reported gross profit
- exported a processed dataset

### Technical Concepts

- Pandas DataFrames
- `read_csv()`
- `head()`
- `shape`
- `columns`
- `dtypes`
- `info()`
- calculated columns
- `pct_change()`
- `diff()`
- `to_csv()`

### Business & Product Application

- evaluated whether margin improvement may be associated with stronger segment economics and changing revenue mix
- kept findings preliminary rather than converting them into unsupported management recommendations
- established reconciliation as a control before deeper analysis

---

# Actual Time by Week

## Week Ending September 27, 2026

| Activity | Hours |
|---|---:|
| Python / Technical Learning | 1.33 |
| Product / Jira | 0.0 |
| Dedicated Portfolio Build Block | 0.0 |
| Weekly Assessment | 0.0 |
| **Total Focused Time** | **1.33** |

## Week Ending October 4, 2026

| Category | Hours |
|---|---:|
| Python / Technical Learning | 4.00 |
| Applied AI / Technical Learning | 1.00 |
| Product / Jira | 1.00 |
| Dedicated Portfolio Build Block | 0.0 |
| Weekly Assessment | 0.0 |
| **Total Focused Time** | **6.00** |


## Week Ending October 11, 2026

| Activity | Hours |
|---|---:|
| Python / Technical Learning | 1.00 |
| Data Analysis / Technical Learning | 0.50 |
| Portfolio Restructuring & Documentation | 1.00 |
| Support Triage Completion | 0.50 |
| **Total Focused Time** | **3.00** |

> Portfolio project hours overlap with technical-learning hours and are therefore tracked separately rather than added again to the weekly total.

---

# Logging Guidelines

Each training session should record:

1. Session number
2. Date
3. Area
4. Project
5. Duration
6. Concept tags
7. Objective
8. Work completed
9. Technical concepts practiced
10. Lessons learned
11. Product & strategy application

When relevant, also record:

- PCEP concepts practiced
- PCAP concepts practiced
- Jira issue or product requirement advanced
- Bugs or failure modes discovered
- Evaluation results
- Architecture or product trade-offs
- Spaced-repetition topics that need to be revisited

Time should reflect actual focused work rather than estimated project duration.

---

# Session Numbering

Training progression is session-based rather than day-based.

For example:

```text
Session 1
Session 2
Session 3
Session 4
...
```
