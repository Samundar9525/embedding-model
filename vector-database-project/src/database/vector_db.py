import chromadb

class VectorDatabase:
    def __init__(self, persist_directory="chroma_db"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection("documents")

    def add_document(self, document, vector):
        self.collection.add(
            documents=[document],
            embeddings=[vector],
            ids=[str(hash(document))]
        )

    def query_similar(self, vector, top_n=1):
        results = self.collection.query(
            query_embeddings=[vector],
            n_results=top_n
        )
        # Return the actual document text(s)
        return results["documents"][0] if results["documents"] else []