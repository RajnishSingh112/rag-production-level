from pathlib import Path
from rag_production_level.document_Loader.document_loaders import DocumentLoader


def main():

    file_path = Path(
        "/Users/rajnish/Developer/Code/RAG Production Level/src/rag_production_level/Docs/rag_document_corpus/text/troubleshooting.txt"
    )

    loader = DocumentLoader()

    documents = loader.load_file(file_path)

    for document in documents:

        print("=" * 60)

        print("CONTENT:")
        print(document.page_content[:500])

        print("\nMETADATA:")
        print(document.metadata)


if __name__ == "__main__":
    main()