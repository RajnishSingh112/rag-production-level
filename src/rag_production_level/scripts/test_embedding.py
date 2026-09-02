

from rag_production_level.embeddings.local_embedding import LocalEmbedding


def main():

    embedding = LocalEmbedding()

    text = "Database connection timeout can be caused by database saturation."

    vector = embedding.embed_text(text)

    print("Vector type:", type(vector))
    print("Vector dimensions:", len(vector))
    print("First 10 values:", vector[:10])


if __name__ == "__main__":
    main()