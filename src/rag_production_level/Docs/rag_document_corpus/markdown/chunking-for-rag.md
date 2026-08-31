# RAG Chunking Notes

Technical documentation contains headings, lists, code examples, tables, and cross-references.

Fixed-size chunking is simple but can split a procedure across unrelated boundaries.
Recursive chunking attempts to preserve paragraph and heading boundaries.

Semantic chunking groups text based on semantic similarity. Structure-aware chunking uses
document headings and code boundaries.

For this corpus, preserve:
- document name
- section heading
- page number where available
- version
- source path
- language for source code

Chunk IDs should remain stable when possible so evaluation can identify retrieved evidence.
