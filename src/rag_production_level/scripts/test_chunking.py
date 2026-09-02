from pathlib import Path
from rag_production_level.chunking.fixed_chunker import FixedChunker
from rag_production_level.document_Loader.document_loaders import DocumentLoader
from rag_production_level.chunking.recursive_chunker import RecursiveChunker
def main():
    file_path = Path(
        "/Users/rajnish/Developer/Code/RAG Production Level/src/rag_production_level/Docs/rag_document_corpus/text/troubleshooting.txt"
    )

    loader = DocumentLoader()
    recursive_chunker = RecursiveChunker(chunk_size=300, chunk_overlap=50)
    fixed_chunker = FixedChunker(chunk_size=300, chunk_overlap=50)
    documents = loader.load_file(file_path)
    recursive_chunked_documents = recursive_chunker.chunk(documents)
    fixed_chunked_documents = fixed_chunker.chunk(documents)
    
    print("\nFIXED CHUNKING")
    print("=" * 60)
    for i, document in enumerate(fixed_chunked_documents):
        print("=" * 60)
        print(f"CHUNK {i + 1}:")
        print("CONTENT:")
        print(document.page_content[:500])
        print("\nMETADATA:")
        print(document.metadata)

    print("\nRECURSIVE CHUNKING")
    print("=" * 60)
    for i, document in enumerate(recursive_chunked_documents):
        print("=" * 60)
        print(f"CHUNK {i + 1}:")
        print("CONTENT:")
        print(document.page_content[:500])
        print("\nMETADATA:")
        print(document.metadata)

if __name__ == "__main__":
    main()