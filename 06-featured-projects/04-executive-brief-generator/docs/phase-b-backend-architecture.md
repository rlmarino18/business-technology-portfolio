# Executive Brief Generator — Phase-B Backend Architecture

## Purpose

This document defines the proposed backend architecture for replacing the Phase-A mock generation with live AI execution.

The purpose is to establish the technical design, security boundaries, cost implications, and implementation sequence before any paid API service is activated.

---

# 1. Current State

Phase A currently operates as:

```text
Browser
→ Mock Structured Extractor Output
→ Human Review
→ Mock Executive Brief Output
→ Human Approval
```

The browser workflow is functional.

The AI generation layer is not yet connected.

---

# 2. Proposed Phase-B Architecture

Recommended architecture:

```text
User Browser
→ Front-End Application
→ Secure Server-Side Function
→ AI API
→ Secure Server-Side Function
→ Front-End Application
```

For the current application stack, the proposed server-side layer is:

```text
Netlify Functions
```

The front end remains:

```text
HTML
CSS
Vanilla JavaScript
```

---

# 3. Why a Backend Is Required

An AI API requires a private credential.

That credential must not be stored in:

- index.html,
- browser JavaScript,
- public GitHub files,
- client-side configuration,
- visible browser requests.

If an API key is placed in browser-side code, users could extract and reuse it.

The secure backend therefore acts as the controlled intermediary between the browser and the AI provider.

---

# 4. Security Boundary

Target flow:

```text
Browser
    |
    | Source content
    v
Netlify Function
    |
    | API key stays here
    | Prompt loaded here
    v
AI Provider
    |
    | Generated output
    v
Netlify Function
    |
    v
Browser
```

The browser receives the model output.

The browser never receives the API key.

---

# 5. Stage-1 Live Flow

The user enters raw operating information.

The application sends:

```text
source content
```

to the Stage-1 backend function.

The backend function:

1. receives the source,
2. loads Structured Extractor V0.7,
3. combines the promoted prompt with the source,
4. sends the request to the AI model,
5. receives the generated structured output,
6. returns that output to the browser.

The browser then enters:

```text
STAGE1_REVIEW
```

No automatic transition to Stage 2 occurs.

---

# 6. Stage-1 Human Gate

The user reviews and may edit Stage-1 output.

Only after:

```text
STAGE1_APPROVED
```

may the application send Stage-1 content to the Stage-2 backend function.

If Stage-1 content changes after approval:

```text
approval → invalid
Stage 2 → locked
```

This behavior already exists in Phase A and must remain unchanged.

---

# 7. Stage-2 Live Flow

The browser sends only:

```text
human-approved Stage-1 output
```

to the Stage-2 backend function.

The backend:

1. receives approved Stage-1 content,
2. loads Executive Brief Generator V1.4,
3. combines the prompt with approved structured records,
4. sends the request to the AI model,
5. receives the executive brief,
6. returns the draft to the browser.

The browser then enters:

```text
FINAL_REVIEW
```

Human approval remains required.

---

# 8. Proposed Backend Endpoints

Initial implementation may use two backend functions:

```text
/.netlify/functions/stage1
/.netlify/functions/stage2
```

Stage 1 responsibility:

```text
Raw Source
→ Structured Extractor V0.7
→ Structured Draft
```

Stage 2 responsibility:

```text
Approved Structured Output
→ Executive Brief Generator V1.4
→ Executive Brief Draft
```

Keeping these functions separate reinforces the two-stage architecture.

---

# 9. Prompt Storage

Promoted prompts should remain version-controlled in the repository.

Conceptual structure:

```text
prompt-library/
├── structured-extractor-v0.7.txt
└── executive-brief-generator-v1.4.txt
```

The backend should load these files rather than duplicating prompt text inside browser JavaScript.

Benefits:

- version control,
- traceability,
- easier prompt updates,
- reduced duplication,
- clearer release history.

---

# 10. API Credential Storage

The AI API credential should be stored as a Netlify environment variable.

Conceptual variable:

```text
OPENAI_API_KEY
```

The actual secret value must not be committed to GitHub.

The backend retrieves the credential from the server environment when making a request.

---

# 11. Initial Error Handling

If Stage 1 fails:

```text
Preserve source
Show error
Allow retry
Do not unlock Stage 2
```

If Stage 2 fails:

```text
Preserve approved Stage-1 content
Show error
Allow retry
Do not rerun Stage 1 automatically
```

If the API returns no usable output:

```text
Treat the request as failed
Do not silently substitute generated content
```

---

# 12. Initial Cost Controls

Before enabling live AI:

- create a dedicated API project,
- use a project-specific API key,
- select an appropriate model,
- configure a small operating budget,
- monitor usage during development,
- avoid unrestricted public API exposure.

The first objective is controlled testing, not production-scale usage.

---

# 13. Prototype Cost Model

One complete EBG execution requires approximately:

```text
1 Stage-1 model call
+
1 Stage-2 model call
```

Additional calls may occur when a user selects:

```text
Rerun Stage 1
Regenerate Stage 2
```

Therefore the application should eventually track:

- Stage-1 calls,
- Stage-2 calls,
- model used,
- input tokens,
- output tokens,
- estimated cost.

This telemetry is not required for the first live integration but should be planned.

---

# 14. Phase-B Implementation Sequence

Recommended sequence:

```text
1. Approve AI provider and cost
2. Create API project
3. Create project API key
4. Store secret securely
5. Configure Netlify environment variable
6. Create Stage-1 backend function
7. Test Stage-1 API independently
8. Connect Stage 1 to browser
9. Validate Stage-1 behavior
10. Create Stage-2 backend function
11. Test Stage-2 API independently
12. Connect Stage 2 to browser
13. Run end-to-end validation
14. Compare live outputs against promoted validation expectations
15. Document defects and remediation
```

---

# 15. What Phase B Changes

Phase B changes:

```text
generation mechanism
```

from:

```text
mock JavaScript output
```

to:

```text
live model output through a secure backend
```

Phase B should not change:

- Stage-1 review requirement,
- Stage-1 approval gate,
- approval invalidation,
- Stage-2 gating,
- final review requirement,
- final human approval,
- promoted prompt versions,
- source-grounding rules.

---

# 16. Definition of Done

Phase B is complete when:

- Stage 1 runs through a secure backend,
- Stage 1 uses Structured Extractor V0.7,
- API credentials remain server-side,
- live Stage-1 output appears in the review UI,
- human approval remains required,
- only approved Stage-1 content can reach Stage 2,
- Stage 2 runs through a secure backend,
- Stage 2 uses Executive Brief Generator V1.4,
- live executive brief output appears in the review UI,
- final human approval remains required,
- API failures preserve workflow state,
- end-to-end live validation is completed,
- no blocking regression is introduced.

---

# 17. Core Architecture Principle

The backend exists to securely operationalize the validated AI workflow.

It must preserve:

```text
Source
→ AI Extraction
→ Human Validation
→ AI Communication
→ Human Approval
```

The technology layer should strengthen the control model, not bypass it.
