# Document QA RAG Assistant

## Overview

The Document Q&A RAG Assistant is an early-stage retrieval-augmented generation prototype focused on document ingestion, semantic retrieval, reranking, and evidence grounding.

The current implementation allows users to upload operational documents, index their contents locally, ask a natural-language question, and inspect the most relevant retrieved evidence before an answer-generation layer is introduced.

The project is intentionally focused on retrieval quality first because poor retrieval creates downstream hallucination and grounding risk regardless of how capable the generation model is.

Current development emphasizes:

- local document ingestion
- chunking strategy
- semantic retrieval
- reranking
- source and page attribution
- evidence-quality inspection
- retrieval failure analysis
- cross-page context preservation

## Current Objective

Build and validate a reliable retrieval layer before introducing answer generation.

The current user workflow is:

    Upload Documents
            ↓
    Extract Text
            ↓
    Chunk Documents
            ↓
    Create Local Embeddings
            ↓
    Store in ChromaDB
            ↓
    Ask a Question
            ↓
    Retrieve Candidate Chunks
            ↓
    Rerank Evidence
            ↓
    Inspect Ranked Evidence + Source Metadata

The immediate objective is to improve retrieval precision and preserve complete evidence across chunk and page boundaries.

Answer generation is intentionally deferred until the retrieval layer is sufficiently reliable.

## Initial Supported File Types

- PDF
- DOCX
- TXT

## Current Technical Stack

- Python
- Streamlit
- sentence-transformers
- `all-MiniLM-L6-v2` local embeddings
- `cross-encoder/ms-marco-MiniLM-L-6-v2` reranker
- ChromaDB
- PyMuPDF
- python-docx

### Current Retrieval Architecture

The active retrieval path is fully local:

    Documents
        ↓
    Text Extraction
        ↓
    Chunking
        ↓
    Local Embeddings
        ↓
    ChromaDB Candidate Retrieval
        ↓
    Cross-Encoder Reranking
        ↓
    Ranked Evidence + Source Metadata

No paid model API is required for the current retrieval pipeline.

## Current Validation Status

### Completed

The current prototype has demonstrated:

- PDF, DOCX, and TXT document ingestion
- text extraction and chunking
- local embedding generation
- persistent ChromaDB indexing
- semantic candidate retrieval
- source, page, and chunk metadata display
- retrieval-distance inspection
- keyword and proximity-aware reranking experiments
- cross-encoder reranking
- controlled retrieval testing across five questions
- a 4/5 initial retrieval baseline before reranker refinement
- improved ranking after switching to a local cross-encoder
- identification of cross-page and chunk-boundary failure modes

### Current Bottleneck

The main unresolved issue is preserving complete evidence when a logical section spans multiple pages or adjacent chunks.

A `chunk_merger.py` utility has been created as the next remediation path, but it is not yet integrated into the primary retrieval workflow.

### Not Yet Implemented

The project does not yet include:

- final answer generation
- production-grade insufficient-evidence handling
- automated end-to-end RAG evaluation
- calibrated confidence scoring
- production deployment
- multi-user state
- authentication or authorization
- scaled latency or cost optimization

The next major development milestone is to improve evidence completeness before adding the generation layer.

## Evaluation Approach

Evaluation is currently lightweight and manually controlled rather than a mature automated benchmark.

The project uses known-question retrieval tests against indexed documents to determine whether the evidence needed to answer a question appears near the top of the retrieved results.

### Evaluation Loop

    Controlled Question
            ↓
    Candidate Retrieval
            ↓
    Ranked Evidence Inspection
            ↓
    Compare Against Expected Evidence
            ↓
    Identify Retrieval Failure
            ↓
    Adjust Chunking / Retrieval / Reranking
            ↓
    Retest

### Retrieval Experiments

Development has included several retrieval approaches:

1. baseline semantic retrieval using local embeddings
2. cosine-distance inspection
3. expanded candidate retrieval from Top 8 to Top 15
4. keyword-aware reranking
5. proximity-aware reranking
6. sentence- and section-aware evidence-selection experiments
7. local cross-encoder reranking

The evidence-selection experiment was removed from the primary retrieval path after testing showed that it could reduce evidence quality.

The current reranking approach uses:

`cross-encoder/ms-marco-MiniLM-L-6-v2`

### Observed Failure Modes

Testing exposed several retrieval problems that are important for downstream RAG quality:

- relevant evidence split across adjacent chunks
- logical sections spanning PDF page boundaries
- correct evidence retrieved with excessive surrounding context
- relevant chunks appearing in the candidate set but ranking too low
- heuristic evidence selection removing useful context

These failures reinforced a core product decision:

> Retrieval quality should be validated before introducing answer generation.

### Current Evaluation Limitation

The existing test coverage is small and should not be treated as a production-quality benchmark.

The current evidence consists of controlled development tests and manual retrieval inspection. Future work should introduce:

- a larger golden question set
- expected source/chunk labels
- Recall@K
- Precision@K
- Mean Reciprocal Rank
- reranker comparison
- evidence-completeness scoring
- automated regression testing
- eventual grounded-answer evaluation
