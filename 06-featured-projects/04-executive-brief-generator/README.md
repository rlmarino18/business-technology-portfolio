# Executive Brief Generator

**Status:** Complete — Portfolio-Grade Prototype  
**Version:** v1.0  
**Completed:** October 12, 2026

## Overview

The Executive Brief Generator is an AI-assisted operational workflow that converts messy business information into structured records and executive-ready briefs.

The system uses a two-stage architecture:

1. **Structured Extractor** — converts raw operational notes into structured, evidence-linked records.
2. **Executive Brief Generator** — transforms validated structured records into a concise executive brief.

Human review is preserved between stages so unsupported assumptions, attribution errors, decision-state mistakes, and evidence-boundary failures can be identified before final output is approved.

This project demonstrates product and technical work across:

- AI workflow design
- prompt architecture
- structured extraction
- human-in-the-loop controls
- evaluation design
- defect analysis
- regression testing
- frontend and backend integration
- API-based model execution
- product validation

## Problem

Operational updates often arrive as fragmented notes, status reports, meeting summaries, and implementation details. The core product problem is not simply summarization; it is preserving the underlying operating truth while reducing the effort required to turn that information into decision-ready output.

Common failure risks include:

- unsupported ownership assignment
- invented deadlines
- collapsed decision states
- incorrect attribution
- scope expansion
- missing dependencies
- overconfident executive summaries
- loss of important uncertainty

## Product Objective

Create an AI-assisted workflow that can transform unstructured operational information into concise executive output while preserving evidence boundaries, explicit ownership, decision state, dependencies, and uncertainty.

The system is intentionally designed with human approval gates rather than assuming autonomous reliability.

## System Architecture

The prototype uses a two-stage AI workflow with explicit human review between stages.

    Raw Operational Source
            ↓
    Structured Extractor V0.8
            ↓
    Structured Records + Source Evidence
            ↓
    Human Review / Approval
            ↓
    Executive Brief Generator V1.4
            ↓
    Draft Executive Brief
            ↓
    Final Human Review / Approval

### Stage 1 — Structured Extractor

Stage 1 converts unstructured operational input into structured records while preserving:

- source evidence
- ownership
- decision state
- deadlines
- dependencies
- approval state
- unresolved questions
- uncertainty

The current promoted Stage-1 baseline is:

`Structured Extractor V0.8`

### Stage 2 — Executive Brief Generator

Stage 2 converts approved structured records into executive-ready output while preserving the constraints established during Stage 1.

The current promoted Stage-2 baseline is:

`Executive Brief Generator V1.4`

### Human-in-the-Loop Control

Human approval is required before Stage 2 and before final output approval.

This is a deliberate product decision intended to reduce the risk of unsupported inference, attribution errors, scope expansion, and incorrect decision-state propagation.

## Evaluation Strategy

The project uses structured evaluation rather than relying on subjective review of individual outputs.

Evaluation is performed against synthetic operational test cases designed to expose failure modes that matter in real business workflows.

Core evaluation dimensions include:

- factual accuracy
- source-grounding
- ownership accuracy
- decision-state preservation
- deadline accuracy
- dependency preservation
- attribution accuracy
- scope and commitment control
- approval-gate integrity
- uncertainty preservation
- executive-brief completeness
- unsupported inference prevention

### Evaluation Process

The evaluation workflow generally follows this sequence:

    Synthetic Operational Source
            ↓
    Gold-Standard Expected Behavior
            ↓
    Stage-1 Structured Output
            ↓
    Structured Evaluation
            ↓
    Defect Identification
            ↓
    Prompt / Rule Remediation
            ↓
    Targeted Regression Testing
            ↓
    Broader Regression Testing
            ↓
    Promotion Review

### Regression Discipline

Candidate prompt versions are not promoted solely because they fix an individual failure.

Changes are tested against prior cases to detect regressions across previously validated behaviors.

This is intended to reduce the risk of improving one failure mode while introducing another.

### Promotion Gates

A candidate baseline is promoted only after completing the required validation sequence.

The current promoted baselines are:

- `Structured Extractor V0.8`
- `Executive Brief Generator V1.4`

The repository includes representative promotion reviews, defect history, evaluation criteria, regression evidence, and curated test cases that demonstrate how these baselines were validated.

## Representative Evaluation Cases

The public portfolio includes a curated subset of evaluation cases rather than the full internal regression archive.

Each representative case contains:

- source input
- gold-standard expected behavior
- structured Stage-1 output
- generated Stage-2 executive brief

The selected cases were chosen to demonstrate different product and model failure modes.

### TC-002 — Conflicting Operational Data

Tests whether the system can preserve uncertainty when operational metrics or statements conflict rather than resolving ambiguity through unsupported inference.

Key behaviors evaluated:

- conflicting metrics
- evidence preservation
- uncertainty handling
- attribution accuracy
- executive-summary restraint

### TC-005 — Decision-State Preservation

Tests whether proposals, preferences, conditional actions, rejected options, and approved decisions remain distinct.

Key behaviors evaluated:

- decision-state classification
- approval boundaries
- proposed vs. committed actions
- unsupported commitment prevention

### TC-006 — Messy and Incomplete Source Material

Tests system behavior when operational notes are fragmented, informal, or missing clear ownership and deadlines.

Key behaviors evaluated:

- incomplete information
- unresolved ownership
- missing deadlines
- evidence-boundary preservation
- open-question generation

### TC-009 — Safety and Approval-Gate Scenario

Tests higher-risk operational information where unsupported causal claims, liability assumptions, or premature external communication could create significant risk.

Key behaviors evaluated:

- factual restraint
- approval sequencing
- escalation logic
- external-communication boundaries
- evidence preservation
- unsupported causality prevention

### TC-012 — Changing Workflow and Approval State

Tests whether previously approved actions remain valid when underlying conditions change.

Key behaviors evaluated:

- approval invalidation
- workflow-state changes
- dependency tracking
- release gating
- action authorization

### Evidence Structure

Each case is organized as:

    source
        ↓
    gold standard
        ↓
    structured output
        ↓
    generated brief

These artifacts provide a traceable path from raw operational information to evaluated AI output.

## Implementation

The prototype includes a browser-based interface, a Node.js backend, and live model integration.

### Frontend

The frontend is implemented with:

- HTML
- CSS
- JavaScript

The interface supports:

- raw source submission
- Stage-1 structured output review
- human approval before Stage 2
- Stage-2 executive brief generation
- final human approval
- workflow-state preservation
- retry behavior after API failure

### Backend

The backend is implemented with Node.js and provides:

- API request handling
- prompt loading
- model invocation
- request validation
- Stage-1 execution
- Stage-2 execution
- health checks
- failure-state handling

### Model Integration

The prototype uses API-based model execution through the OpenAI SDK.

The model workflow is separated from the frontend so prompt logic, validation behavior, and model execution can evolve independently from the user interface.

### Current Prototype Stack

- Node.js
- JavaScript
- HTML
- CSS
- OpenAI SDK
- environment-based API configuration
- structured prompt pipelines
- human-in-the-loop workflow controls

### Prototype Status

The project demonstrates a working end-to-end prototype and validated internal workflow.

It should not be interpreted as a production-ready or fully autonomous system.

Additional work would be required for production deployment, including:

- authentication
- authorization
- persistent application state
- secure secret management
- production observability
- rate limiting
- scalable deployment
- automated evaluation pipelines
- broader model and data validation
- user analytics
- production-grade error handling

## Product & Delivery Briefing

### Key Product Metrics

The project is evaluated on more than output fluency.

Primary measures include:

- factual correctness
- grounding to source evidence
- ownership accuracy
- decision-state preservation
- dependency accuracy
- approval-gate integrity
- unsupported inference rate
- regression pass rate
- material defect count
- automatic failure count

### Key Failure Modes

The project surfaced several recurring failure classes:

- assigning ownership that was not explicitly supported
- converting discussion into commitment
- inventing or over-interpreting deadlines
- collapsing conditional or rejected actions into approved decisions
- expanding client requests into implementation-team commitments
- overstating unresolved risks
- losing attribution
- converting uncertainty into certainty
- propagating outdated approvals after workflow conditions changed

These failure modes directly informed prompt revisions, regression tests, and promotion gates.

### Product Decisions

Several product choices emerged from the evaluation work:

- preserve human review between Stage 1 and Stage 2
- require final human approval before output is treated as complete
- separate extraction from executive communication
- treat uncertainty and unresolved state as first-class information
- block prompt promotion when broader regression reveals new failures
- preserve failed workflow state so users can retry without restarting the entire process

### Current Bottlenecks

The current prototype still has limitations that would matter in a production environment:

- manual evaluation workflow
- limited automated observability
- no persistent multi-user state
- no authentication or authorization layer
- no production deployment architecture
- model behavior remains dependent on prompt and model-version stability
- evaluation coverage is synthetic rather than based on production user traffic
- cost and latency have not yet been optimized at scale

### Next Product Iteration

The next logical evolution is to apply the validated extraction, evidence-linking, decision-state, approval, and human-review patterns to more specialized operational workflows.

One planned extension is a Change Documentation Generator that would reuse selected architectural and evaluation lessons from this project while solving a narrower change-management and documentation problem.

## Repository Guide

This public portfolio version is intentionally curated to show the strongest implementation and evaluation evidence without reproducing the full internal development archive.

### Core Implementation

- `index.html` — browser interface
- `css/styles.css` — application styling
- `js/app.js` — frontend workflow logic
- `server/server.js` — backend API and model orchestration
- `package.json` — Node.js project configuration

### Architecture & Product Documentation

The `docs/` directory contains:

- application data model
- frontend implementation plan
- frontend validation
- backend architecture
- live Stage-1 / Stage-2 validation
- prototype user workflow
- Stage-1 / Stage-2 integration contract

### Promoted Prompt Baselines

The `prompts/` directory contains the current promoted prompt versions:

- `structured-extractor-v0.8.txt`
- `executive-brief-generator-v1.4.txt`

### Evaluation Evidence

The `evaluation/` directory contains:

- evaluation rubric
- defect log
- current baseline regression report
- Stage-1 promotion review
- Stage-2 promotion review
- five representative evaluation cases

Each representative case includes:

    source
        ↓
    gold standard
        ↓
    structured output
        ↓
    generated brief

### Development History

The `project-time-log/` directory preserves the documented development history, including estimated early work and subsequently tracked implementation, validation, regression, and integration work.
