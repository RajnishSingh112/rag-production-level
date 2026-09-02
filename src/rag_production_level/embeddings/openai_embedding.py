from langchain_openai import OpenAIEmbeddings

class OpenAIEmbedding:
    def __init__(self):
        self.embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

    def embed_text(self, query: str) -> list[float]:
        return self.embedding_model.embed_query(query)