from pathlib import Path

from rag_production_level.chunking.semantic_chunker import SemanticChunker
from rag_production_level.document_Loader.document_loaders import DocumentLoader



def main():

    file_path = Path(
        "/Users/rajnish/Developer/Code/RAG Production Level/src/rag_production_level/Docs/rag_document_corpus/text/troubleshooting.txt"
    )

    loader = DocumentLoader()
    semantic_chunker = SemanticChunker()

    documents = loader.load_file(file_path)

    for document in documents:

        sentences = semantic_chunker.split_sentences(document)

        print("=" * 60)
        print(f"TOTAL SENTENCES: {len(sentences)}")

        for index, sentence in enumerate(sentences):

            print(f"\nSENTENCE {index}:")
            print(sentence)


if __name__ == "__main__":
    main()