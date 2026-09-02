# Production-Grade RAG Platform

> An evaluation-driven, modular Retrieval-Augmented Generation (RAG) platform designed to experiment with, measure, and optimize document retrieval quality, latency, and cost.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![RAG](https://img.shields.io/badge/AI-RAG-purple.svg)](#)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-green.svg)](https://www.langchain.com/)
[![Testing](https://img.shields.io/badge/Testing-pytest-orange.svg)](https://pytest.org/)
[![Status](https://img.shields.io/badge/Status-In%20Development-yellow.svg)](#)

---

## Overview

This project is a **production-oriented Retrieval-Augmented Generation (RAG) platform** built to explore how different document processing, chunking, embedding, retrieval, ranking, and evaluation strategies affect the quality and performance of an AI-powered knowledge system.

The goal is not simply to build a chatbot.

The primary objective is to build a system that can answer:

> **"Which RAG strategy performs better, why does it perform better, and can we prove it with measurable results?"**

The platform is designed around an **evaluation-driven architecture**, where RAG components can be replaced, tested, benchmarked, and compared independently.

The project progressively explores:

* Document ingestion
* Document loading
* Metadata normalization
* Multiple chunking strategies
* Local and cloud embedding providers
* Vector retrieval
* Keyword retrieval
* Hybrid retrieval
* Reranking
* Metadata filtering
* Source attribution and citations
* Retrieval evaluation
* Generation evaluation
* Latency and cost measurement
* Regression testing
* CI quality gates
* Observability
* API deployment
* Containerization

---

# Why This Project?

A basic RAG implementation is relatively straightforward:

```text
Documents
    ↓
Chunks
    ↓
Embeddings
    ↓
Vector Database
    ↓
Similarity Search
    ↓
LLM
    ↓
Answer
```

However, production RAG systems introduce much harder engineering problems.

For example:

* How should documents be chunked?
* Should chunking be fixed-size, recursive, semantic, or structure-aware?
* How large should a chunk be?
* How much overlap is useful?
* Should retrieval use vectors, keywords, or both?
* How do we handle exact identifiers such as error codes and class names?
* How can irrelevant retrieved documents be removed?
* How do we evaluate retrieval independently from generation?
* How do we detect when a new change makes retrieval worse?
* How do we measure latency and token usage?
* How can RAG quality become part of CI/CD?

This project is designed to investigate those questions systematically.

---

# Project Goals

## Primary Goals

### 1. Modular RAG Architecture

Every major RAG component should be replaceable without rewriting the entire system.

Examples:

```text
Embedding
├── LocalEmbedding
└── OpenAIEmbedding

Chunking
├── FixedChunker
├── RecursiveChunker
├── SemanticChunker
└── StructureAwareChunker

Retrieval
├── VectorRetriever
├── KeywordRetriever
└── HybridRetriever

Ranking
└── Reranker
```

---

### 2. Evaluation-Driven Optimization

Instead of choosing algorithms based purely on intuition, the system should measure their performance.

Example:

```text
Fixed Chunking
      │
      ├── Recall@5
      ├── MRR
      ├── Latency
      └── Cost

Recursive Chunking
      │
      ├── Recall@5
      ├── MRR
      ├── Latency
      └── Cost

Semantic Chunking
      │
      ├── Recall@5
      ├── MRR
      ├── Latency
      └── Cost
```

The best strategy should therefore be determined by data rather than assumptions.

---

### 3. Production-Oriented Engineering

The project will progressively introduce:

* Configuration management
* Logging
* Error handling
* Type hints
* Interfaces / abstractions
* Unit tests
* Integration tests
* Evaluation datasets
* Regression testing
* CI/CD
* Docker
* API layer
* Observability

---

# Architecture

The planned high-level architecture is:

```text
                         ┌─────────────────────┐
                         │   Document Sources  │
                         │ PDF / TXT / MD /    │
                         │ Code / JSON / YAML  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Document Ingestion │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Document Loader   │
                         │                     │
                         │ PDF                 │
                         │ Text                │
                         │ Markdown            │
                         │ Code                │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Chunking       │
                         │                     │
                         │ Fixed               │
                         │ Recursive           │
                         │ Semantic            │
                         │ Structure-aware     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Embedding      │
                         │                     │
                         │ Local Models        │
                         │ Cloud Models        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     Indexing        │
                         │                     │
                         │ Vector Index        │
                         │ Keyword Index       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Retrieval      │
                         │                     │
                         │ Vector              │
                         │ Keyword             │
                         │ Hybrid              │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Reranking      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Context Construction│
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    LLM Generation   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Answer + Citations │
                         └─────────────────────┘
```

---

# Current Implementation

The project is being developed incrementally.

## Implemented

### Document Loading

The current ingestion layer supports:

| File Type | Loader        |
| --------- | ------------- |
| PDF       | `PyPDFLoader` |
| TXT       | `TextLoader`  |
| Markdown  | `TextLoader`  |
| C#        | `TextLoader`  |
| Java      | `TextLoader`  |
| Python    | `TextLoader`  |
| SQL       | `TextLoader`  |

The project uses LangChain community loaders for parsing while keeping orchestration and application-level logic inside our own Python architecture.

---

## Chunking

The current chunking architecture is:

```text
BaseChunker
    │
    ├── FixedChunker
    │
    ├── RecursiveChunker
    │
    └── SemanticChunker
```

### Fixed Chunking

Splits documents according to a fixed character size and overlap.

Example configuration:

```python
chunk_size=500
chunk_overlap=50
```

---

### Recursive Chunking

Uses hierarchical separators to preserve natural document boundaries where possible.

Typical separation strategy:

```text
Paragraph
   ↓
Line
   ↓
Sentence
   ↓
Word
```

This generally provides more meaningful chunks than blindly cutting text at a fixed character boundary.

---

### Semantic Chunking

Semantic chunking attempts to detect topic transitions using sentence embeddings.

Current pipeline:

```text
Document
    ↓
Sentence Splitting
    ↓
Sentence Embeddings
    ↓
Cosine Similarity
    ↓
Similarity Distribution
    ↓
Boundary Detection
    ↓
Semantic Chunks
```

For example:

```text
Sentence A ── 0.69 ── Sentence B
                         │
Sentence B ── 0.31 ── Sentence C
                         │
Sentence C ── 0.09 ── Sentence D
                         ↓
                    Topic Change
```

The current implementation uses an adaptive percentile-based boundary approach for experimentation.

This will later be evaluated against other chunking strategies rather than being assumed to be superior.

---

# Embedding Architecture

Embedding providers are abstracted behind a common interface.

```text
BaseEmbedding
      │
      ├── LocalEmbedding
      │
      └── OpenAIEmbedding
```

This prevents the rest of the RAG pipeline from becoming tightly coupled to a single embedding provider.

Example interface:

```python
class BaseEmbedding(ABC):

    @abstractmethod
    def embed_text(self, text: str) -> list[float]:
        pass
```

---

## Local Embeddings

The current experimental implementation uses:

```text
Model:
all-MiniLM-L6-v2

Embedding dimension:
384
```

Local embeddings are useful during development because experiments can be performed without requiring paid API credits.

---

# Document Metadata

Every generated chunk receives normalized metadata.

Example:

```python
{
    "source": "/path/to/troubleshooting.txt",
    "document_id": "troubleshooting.txt",
    "chunk_index": 0,
    "chunk_id": "troubleshooting.txt_chunk_0"
}
```

This metadata will later support:

* Source attribution
* Filtering
* Debugging
* Retrieval evaluation
* Citation generation
* Observability
* Traceability

---

# Retrieval Strategy

The retrieval layer will eventually support multiple approaches.

## Vector Retrieval

Uses embedding similarity to find semantically related chunks.

```text
Query
  ↓
Query Embedding
  ↓
Vector Similarity
  ↓
Top-K Chunks
```

This is particularly useful when the query and source document use different wording but express similar concepts.

---

## Keyword Retrieval

Keyword retrieval is useful when exact terms matter.

Examples:

```text
HTTP 409
OCR_ENABLED
Metadata Service
ConnectionPool
retry_count
DocumentLoader
```

Vector similarity alone may not always be the best mechanism for exact technical identifiers.

---

## Hybrid Retrieval

Hybrid retrieval combines semantic and lexical search.

```text
                  Query
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
    Vector Search        Keyword Search
          │                   │
          └─────────┬─────────┘
                    ↓
               Fusion
                    ↓
             Ranked Results
```

The purpose is to combine:

* semantic understanding
* exact keyword matching

This is especially useful for enterprise technical documentation and source code.

---

# Reranking

Initial retrieval may return several potentially relevant chunks.

A reranker can then evaluate those candidates more precisely.

```text
Query
  ↓
Initial Retrieval
  ↓
Top 20 Candidates
  ↓
Reranker
  ↓
Top 5 Relevant Chunks
```

This creates a two-stage retrieval architecture:

```text
Stage 1:
Fast candidate retrieval

Stage 2:
More accurate ranking
```

The trade-off between retrieval quality and latency will be measured experimentally.

---

# Evaluation

Evaluation is one of the core objectives of this project.

A RAG system should not be considered production-ready simply because it produces an answer.

We need to measure whether the answer is:

* relevant
* grounded
* correct
* supported by retrieved documents

---

# Golden Dataset

The project contains a manually defined evaluation dataset containing representative questions over the document corpus.

Example:

```json
{
    "question": "What should be checked when processing jobs remain queued?",
    "expected_sources": [
        "troubleshooting.txt"
    ]
}
```

The dataset acts as a stable benchmark for comparing different RAG configurations.

---

# Retrieval Metrics

Planned retrieval metrics include:

### Recall@K

Measures whether the relevant document appears within the top K retrieved results.

```text
Recall@K =
Relevant queries with correct result in Top-K
------------------------------------------------
Total relevant queries
```

---

### Precision@K

Measures how many of the retrieved results are relevant.

```text
Precision@K =
Relevant retrieved results
--------------------------
Total retrieved results
```

---

### Mean Reciprocal Rank

MRR evaluates how high the first relevant result appears.

```text
Rank 1 → 1.0
Rank 2 → 0.5
Rank 3 → 0.33
Rank 4 → 0.25
```

Higher is better.

---

### NDCG

Normalized Discounted Cumulative Gain will be used where graded relevance is available.

This helps evaluate not only whether relevant documents were retrieved, but whether the most relevant documents were ranked higher.

---

# Generation Evaluation

Retrieval quality alone is insufficient.

The final answer will eventually be evaluated using metrics such as:

* Faithfulness
* Answer relevance
* Answer correctness
* Citation correctness
* Citation completeness

The goal is to determine whether improvements in retrieval actually translate into better answers.

---

# Performance Evaluation

The system will also measure:

```text
Latency
├── Document loading
├── Chunking
├── Embedding
├── Retrieval
├── Reranking
└── Generation

Cost
├── Embedding tokens
├── LLM tokens
└── API calls
```

This enables trade-off analysis.

For example:

```text
Strategy       Recall    Latency    Cost
------------------------------------------------
Fixed          TBD       TBD        TBD
Recursive     TBD       TBD        TBD
Semantic      TBD       TBD        TBD
Hybrid        TBD       TBD        TBD
```

Results will be populated as experiments are completed.

---

# Quality Regression Testing

A major objective is to make RAG quality part of software engineering rather than a manual activity.

Future CI workflow:

```text
Pull Request
     ↓
Run Tests
     ↓
Build / Index Evaluation Corpus
     ↓
Run Golden Questions
     ↓
Calculate Metrics
     ↓
Compare Against Baseline
     ↓
       ┌───────────────┐
       │ Quality Check │
       └───────┬───────┘
               │
        ┌──────┴──────┐
        ↓             ↓
     PASS            FAIL
        │             │
        ↓             ↓
     Merge       Block Build
```

For example:

```text
Baseline Recall@5: 0.86

New Recall@5:      0.81

Allowed regression: 0.02

Result:
FAIL
```

This allows retrieval quality to become a measurable engineering quality gate.

---

# Observability

The platform will eventually expose structured information about each RAG execution.

Example:

```text
Request ID
    │
    ├── Query
    │
    ├── Embedding latency
    │
    ├── Retrieval latency
    │
    ├── Retrieved documents
    │
    ├── Reranking latency
    │
    ├── Prompt tokens
    │
    ├── Completion tokens
    │
    ├── Total latency
    │
    └── Final answer
```

This will make it possible to investigate questions such as:

> Why did this query become slower?

or:

> Why did this answer retrieve irrelevant documents?

---

# Project Structure

The project is being organized into independent modules.

Current / planned structure:

```text
rag-production-level/
│
├── src/
│   └── rag_production_level/
│
│       ├── document_loader/
│       │   ├── __init__.py
│       │   ├── base_loader.py
│       │   ├── pdf_loader.py
│       │   ├── text_loader.py
│       │   ├── code_loader.py
│       │   └── document_loader.py
│       │
│       ├── chunking/
│       │   ├── __init__.py
│       │   ├── base_chunker.py
│       │   ├── fixed_chunker.py
│       │   ├── recursive_chunker.py
│       │   ├── semantic_chunker.py
│       │   └── structure_aware_chunker.py
│       │
│       ├── embeddings/
│       │   ├── __init__.py
│       │   ├── base_embedding.py
│       │   ├── local_embedding.py
│       │   └── openai_embedding.py
│       │
│       ├── retrieval/
│       │   ├── __init__.py
│       │   ├── vector_retriever.py
│       │   ├── keyword_retriever.py
│       │   └── hybrid_retriever.py
│       │
│       ├── ranking/
│       │   └── reranker.py
│       │
│       ├── evaluation/
│       │   ├── evaluator.py
│       │   ├── metrics.py
│       │   └── datasets/
│       │
│       ├── generation/
│       │   └── generator.py
│       │
│       ├── observability/
│       │   └── tracing.py
│       │
│       └── config/
│           └── settings.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── evaluation/
│
├── scripts/
│   ├── test_loader.py
│   ├── test_chunker.py
│   ├── test_embedding.py
│   └── ...
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── evaluation/
│
├── notebooks/
│   └── experiments/
│
├── pyproject.toml
├── uv.lock
├── .gitignore
├── README.md
└── LICENSE
```

---

# Technology Stack

## Core

* Python
* LangChain
* LangChain Community
* NumPy
* Sentence Transformers

## Planned

* Vector database / vector index
* BM25 / lexical retrieval
* Reranking model
* pytest
* Docker
* GitHub Actions
* FastAPI
* Structured logging
* Evaluation framework

The project deliberately avoids excessive framework coupling so individual components can be benchmarked independently.

---

# Development Philosophy

This project follows several engineering principles.

## 1. Measure Before Optimizing

Do not assume:

> Semantic > Recursive > Fixed

Instead:

```text
Hypothesis
    ↓
Implementation
    ↓
Experiment
    ↓
Metrics
    ↓
Decision
```

---

## 2. Separate Retrieval From Generation

RAG quality is decomposed into:

```text
Retrieval Quality
       +
Context Quality
       +
Generation Quality
```

A bad answer does not necessarily mean the LLM is the problem.

The actual problem may be:

```text
Question
   ↓
Bad Retrieval
   ↓
Bad Context
   ↓
Correctly behaving LLM
   ↓
Bad Answer
```

Therefore retrieval must be independently measurable.

---

## 3. Prefer Interfaces Over Vendor Lock-In

Components such as embedding and retrieval should be abstracted.

For example:

```text
BaseEmbedding
      │
      ├── LocalEmbedding
      └── OpenAIEmbedding
```

This allows experimentation without rewriting downstream components.

---

## 4. Build Incrementally

The project is intentionally developed in phases.

A working baseline is preferred over implementing every advanced feature simultaneously.

---

# Development Roadmap

## Phase 0 — Project Setup

* [x] Python environment
* [x] Package structure
* [x] Dependency management with `uv`
* [x] Git repository
* [x] Documentation structure

---

## Phase 1 — Baseline RAG

* [ ] Basic ingestion
* [ ] Chunking
* [ ] Embeddings
* [ ] Vector index
* [ ] Similarity retrieval
* [ ] Basic generation

---

## Phase 2 — Ingestion

* [x] PDF loader
* [x] Text loader
* [x] Markdown loader
* [x] Code loader
* [ ] JSON structured loading
* [ ] YAML structured loading
* [ ] Metadata normalization
* [ ] Ingestion validation

---

## Phase 3 — Chunking

* [x] Base chunker abstraction
* [x] Fixed chunking
* [x] Recursive chunking
* [x] Semantic sentence splitting
* [x] Sentence embeddings
* [x] Cosine similarity
* [x] Semantic boundary detection
* [x] Semantic chunk creation
* [ ] Structure-aware chunking
* [ ] Chunking benchmark

---

## Phase 4 — Retrieval

* [ ] Vector retrieval
* [ ] Keyword retrieval
* [ ] Hybrid retrieval
* [ ] Metadata filtering
* [ ] Top-K configuration
* [ ] Retrieval benchmarking

---

## Phase 5 — Reranking

* [ ] Candidate retrieval
* [ ] Reranking model
* [ ] Top-N reranking
* [ ] Reranking evaluation
* [ ] Latency comparison

---

## Phase 6 — Evaluation

* [ ] Golden dataset
* [ ] Recall@K
* [ ] Precision@K
* [ ] MRR
* [ ] NDCG
* [ ] Faithfulness
* [ ] Answer relevance
* [ ] Citation correctness

---

## Phase 7 — Quality Gates

* [ ] Evaluation baseline
* [ ] Regression thresholds
* [ ] Automated evaluation
* [ ] GitHub Actions
* [ ] CI quality gate
* [ ] Retrieval regression detection

---

## Phase 8 — Observability

* [ ] Structured logs
* [ ] Request tracing
* [ ] Retrieval traces
* [ ] Latency tracking
* [ ] Token tracking
* [ ] Cost tracking

---

## Phase 9 — Productionization

* [ ] FastAPI
* [ ] Configuration management
* [ ] Docker
* [ ] Health checks
* [ ] Error handling
* [ ] Production logging
* [ ] API documentation

---

## Phase 10 — Final Optimization

* [ ] Benchmark configurations
* [ ] Compare retrieval strategies
* [ ] Compare chunking strategies
* [ ] Compare embedding models
* [ ] Optimize latency
* [ ] Optimize cost
* [ ] Document final architecture
* [ ] Prepare technical benchmarks

---

# Example Experiment

A future experiment might compare:

```text
Configuration A
────────────────────────
Recursive Chunking
+
Local Embeddings
+
Vector Retrieval
+
Top-K = 5


Configuration B
────────────────────────
Semantic Chunking
+
Local Embeddings
+
Hybrid Retrieval
+
Reranking
+
Top-K = 5
```

Results:

```text
Metric                  A          B
------------------------------------------------
Recall@5                TBD        TBD
MRR                     TBD        TBD
NDCG                    TBD        TBD
Answer relevance        TBD        TBD
Citation accuracy       TBD        TBD
Latency                 TBD        TBD
Embedding cost          TBD        TBD
```

The objective is to determine whether the additional complexity of B provides enough quality improvement to justify its cost.

---

# Example RAG Flow

Given a query:

```text
"What should I check when processing jobs remain queued?"
```

The system should eventually perform:

```text
User Query
    ↓
Query Embedding
    ↓
Vector Retrieval
    │
    ├── troubleshooting.txt
    ├── message_broker.md
    └── metadata_service.md
    ↓
Keyword Retrieval
    │
    ├── queue
    ├── consumer
    └── processing
    ↓
Hybrid Fusion
    ↓
Reranking
    ↓
Top Relevant Context
    ↓
LLM
    ↓
Grounded Answer
    ↓
Source Citations
```

---

# Testing Strategy

Testing will exist at multiple levels.

## Unit Tests

Test individual components:

```text
DocumentLoader
Chunker
Embedding
Retriever
Metric
Reranker
```

---

## Integration Tests

Test component interactions:

```text
Loader
  ↓
Chunker
  ↓
Embedding
  ↓
Index
  ↓
Retriever
```

---

## Evaluation Tests

Run the golden question dataset and calculate retrieval and generation metrics.

---

## Regression Tests

Compare the current implementation against a known baseline.

Example:

```text
Previous Recall@5 = 0.88
Current Recall@5  = 0.87

Allowed degradation = 0.02

PASS
```

But:

```text
Previous Recall@5 = 0.88
Current Recall@5  = 0.81

Allowed degradation = 0.02

FAIL
```

---

# Engineering Decisions

## Why Python?

Python was selected because of its mature AI/ML ecosystem and strong support for:

* embeddings
* NLP
* vector search
* evaluation
* machine learning
* LLM integrations

The project also serves as an opportunity to develop production-level Python engineering skills while building an AI system.

---

## Why LangChain?

LangChain provides useful abstractions for:

* document loading
* document representation
* text splitting
* model integrations

However, the project deliberately avoids putting the entire architecture inside LangChain.

Application-level orchestration and abstractions remain under project control.

---

## Why Local Embeddings?

Local embeddings allow experiments without depending on paid API credits.

This makes it possible to repeatedly benchmark:

```text
Chunking
Retrieval
Similarity
Evaluation
```

without incurring API costs for every experiment.

Cloud embeddings can be plugged in later through the embedding abstraction.

---

# Current Results

> This section will be updated as experiments are completed.

### Semantic Chunking Experiment

Document:

```text
troubleshooting.txt
```

Number of detected sentences:

```text
16
```

Embedding dimension:

```text
384
```

Detected semantic boundaries:

```text
[6, 8, 12]
```

Generated semantic chunks:

```text
4
```

Initial observation:

Semantic similarity successfully identified significant topic transitions within the troubleshooting document.

However, this result alone does **not** establish that semantic chunking is superior.

Future retrieval evaluation will determine whether these boundaries improve retrieval performance.

---

# Resume-Relevant Skills Demonstrated

This project demonstrates practical experience in:

### AI / ML

* Retrieval-Augmented Generation
* Embeddings
* Semantic similarity
* Vector retrieval
* Hybrid retrieval
* Reranking
* LLM application architecture
* RAG evaluation

### Python

* Object-oriented programming
* Abstract base classes
* Type hints
* Modules and packages
* Dependency management
* Virtual environments
* Exception handling
* Testing
* Async programming
* Configuration management

### Software Engineering

* Modular architecture
* Interface-driven design
* Dependency injection
* Separation of concerns
* Unit testing
* Integration testing
* CI/CD
* Quality gates
* Observability
* Performance benchmarking

### Production Engineering

* Latency optimization
* Cost optimization
* Regression detection
* Containerization
* API development
* Automated evaluation

---

# Resume Description

A concise resume version of the project:

> **Production-Grade RAG Platform** — Built a modular, evaluation-driven RAG platform in Python supporting multiple document loaders, fixed/recursive/semantic chunking, local embeddings, vector and hybrid retrieval, reranking, source attribution, and automated retrieval evaluation. Designed benchmarking and regression-testing workflows using Recall@K, MRR, NDCG, latency, and cost metrics, with planned CI quality gates to prevent RAG quality degradation.

### Stronger version after the project is complete

Once we have actual benchmark numbers, this should become:

> **Production-Grade RAG Platform** — Engineered an evaluation-driven RAG platform supporting multi-format ingestion, adaptive semantic chunking, hybrid lexical/vector retrieval, reranking, and grounded generation. Improved **Recall@5 by X%** and reduced retrieval latency by **Y%** through systematic benchmarking, while implementing automated RAG regression testing and CI quality gates.

The second version is much stronger because it contains **measurable engineering impact** rather than only listing technologies.

---

# Key Design Principle

The central philosophy of this project is:

> **Don't just build a RAG system. Build a system that can prove which RAG design works better.**

The project therefore treats RAG as both:

```text
AI System
    +
Software Engineering System
    +
Evaluation System
```

---

# Future Extensions

Once the production RAG foundation is stable, the platform can potentially be extended with:

* Agentic retrieval
* Query rewriting
* Multi-query retrieval
* HyDE
* Self-query retrieval
* Context compression
* Multi-stage retrieval
* Knowledge graphs
* Conversational memory
* Multi-modal retrieval
* Feedback-driven optimization

These are intentionally deferred until the core RAG pipeline has reliable evaluation and observability.

---

# Project Status

**Current Stage:** RAG Foundation / Chunking Optimization

### Completed

* Document ingestion architecture
* Multiple document loaders
* Base chunking abstraction
* Fixed chunking
* Recursive chunking
* Semantic sentence splitting
* Local sentence embeddings
* Cosine similarity calculation
* Adaptive semantic boundary detection
* Semantic chunk creation
* Chunk metadata generation

### Next

* Baseline vector retrieval
* Retrieval evaluation
* Golden dataset execution
* Fixed vs Recursive vs Semantic benchmarking
* Retrieval metrics

---

# Learning Objective

This project is also designed as a hands-on learning environment.

Rather than treating AI frameworks as black boxes, each major component is implemented and studied individually.

The intended learning progression is:

```text
Python
  ↓
Software Architecture
  ↓
Document Processing
  ↓
Embeddings
  ↓
Semantic Similarity
  ↓
RAG
  ↓
Retrieval
  ↓
Evaluation
  ↓
Optimization
  ↓
Productionization
```

The final objective is to be able to explain not only **how the system works**, but also:

* why each component exists
* what alternatives were considered
* what trade-offs were involved
* how performance was measured
* why one implementation performed better than another
* how the system can safely evolve in production

---

# License

This project is intended primarily as a learning, experimentation, and portfolio project.
