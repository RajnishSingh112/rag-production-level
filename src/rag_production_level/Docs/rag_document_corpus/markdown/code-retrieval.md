# Code Retrieval Guide

For source-code retrieval, index classes, methods, docstrings, and comments with metadata.

Recommended metadata:
- language
- repository
- file path
- class name
- method name
- line range
- module

Do not blindly split a method across chunks. Structure-aware chunking should prefer complete
methods or logical blocks.

See `metadata_generator.cs`, `MetadataService.java`, and `document_service.py`.
