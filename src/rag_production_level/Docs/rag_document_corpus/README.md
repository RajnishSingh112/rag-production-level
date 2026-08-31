# Nexus Document Platform — RAG Corpus

Synthetic mixed-format enterprise documentation corpus for building and evaluating a production-oriented RAG system.

## Formats
- PDF
- TXT
- Markdown
- C#
- Java
- Python
- JSON
- YAML
- SQL

## Important
This corpus is intentionally interconnected. The same concept can appear in several formats and documents.
That is useful for testing:
- simple vs semantic/structure-aware chunking
- vector vs keyword vs hybrid retrieval
- metadata filtering
- reranking
- source-code retrieval
- multi-document questions
- evaluation and regression testing

The `evaluation/questions.json` file contains a starter golden dataset. Treat its answers and source lists as evaluation ground truth and do not modify them casually.

The content is synthetic and designed for experimentation rather than production use.
