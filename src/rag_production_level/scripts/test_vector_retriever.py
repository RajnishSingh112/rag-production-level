from pathlib import Path

from rag_production_level.chunking.recursive_chunker import RecursiveChunker
from rag_production_level.document_Loader.document_loaders import DocumentLoader
from rag_production_level.embeddings.local_embedding import LocalEmbedding
from rag_production_level.retrieval.vector_retriever import VectorRetriever

DATA_PATH = Path(__file__).parent.parent / "Docs" / "rag_document_corpus" / "text" / "troubleshooting.txt"

#1 Load the document
loader = DocumentLoader()
documents = loader.load_file(DATA_PATH)
print(f"Loaded {len(documents)} document(s) from {DATA_PATH}")

# 2 Chunk the document
chunker = RecursiveChunker(chunk_size=300, chunk_overlap=50)
chunked_documents = chunker.chunk(documents)
print(f"Chunked into {len(chunked_documents)} chunks")

# 3 Create the embedding model
embedding_model = LocalEmbedding()

# 4 Create the vector retriever
retriever = VectorRetriever(embedding_model)

# 5 Test the retriever with a sample query
query = "How to troubleshoot database connection timeout?"

#6 Retrieve the top 3 most relevant chunks based on the query
retrieved_documents = retriever.retrieve(query, chunked_documents, top_k=3)

#7 Print the retrieved documents
print("\nQuery:", query)
print("\nRetrieved Results:")

for i, doc in enumerate(retrieved_documents):
    print("\n" + "=" * 60)
    print("Rank", i + 1)
    print("Source:", doc.metadata.get("source", "Unknown"))
    print("Chunk Index:", doc.metadata.get("chunk_index", "Unknown"))
    print("Text:", doc.page_content[:500])  # Print first 500 characters of the chunk