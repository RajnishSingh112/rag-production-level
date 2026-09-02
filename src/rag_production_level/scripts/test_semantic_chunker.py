from pathlib import Path

from rag_production_level.chunking.semantic_chunker import SemanticChunker
from rag_production_level.document_Loader.document_loaders import DocumentLoader
from rag_production_level.embeddings.local_embedding import LocalEmbedding



def main():

    file_path = Path(
        "/Users/rajnish/Developer/Code/RAG Production Level/src/rag_production_level/Docs/rag_document_corpus/text/troubleshooting.txt"
    )

    loader = DocumentLoader()
    embedding_model = LocalEmbedding()
    semantic_chunker = SemanticChunker(embedding_model)

    documents = loader.load_file(file_path)

    # for document in documents:

    #     sentences = semantic_chunker.split_sentences(document)

    #     embedded_sentences = semantic_chunker.embed_sentences(sentences)

    #     print(f"TOTAL Sentences: {len(sentences)}")
    #     print(f"TOTAL Embedded Sentences: {len(embedded_sentences)}")

    #     for index, (sentence, embedding) in enumerate(zip(sentences, embedded_sentences)):

    #         print(f"\nSENTENCE {index}:")
    #         print(sentence)
    #         print(f"VECTOR DIMENSION: {len(embedding)}")
    #         print(f"First 5 elements of the embedding vector: {embedding[:5]}")
    #     similarities = []
    #     for i in range(len(embedded_sentences) - 1):
    #         similarity = semantic_chunker.calculate_similarity(
    #             embedded_sentences[i], embedded_sentences[i + 1]
    #         )
    #         similarities.append(similarity)
    #         print(f"\nSIMILARITY between SENTENCE {i} and SENTENCE {i + 1}: {similarity:.4f}")


    #     boundary_indices = semantic_chunker.find_boundary(similarities)
    #     print(f"\nBOUNDARY INDICES (where similarity is below threshold): {boundary_indices}")
    
    chunks = semantic_chunker.chunk(documents)

    print("TOTAL CHUNKS:", len(chunks))

    for i, chunk in enumerate(chunks):
    
        print("\n" + "=" * 60)
        print("CHUNK:", i)
        print("TEXT:")
        print(chunk.page_content)
    
        print("METADATA:")
        print(chunk.metadata)

if __name__ == "__main__":
    main()