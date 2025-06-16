from database.vector_db import VectorDatabase
from utils.embeddings import get_ollama_embedding

def fetch_and_print_most_similar(vector_db, question, model="mxbai-embed-large"):
    question_vector = get_ollama_embedding(question, model=model)
    similar_docs = vector_db.query_similar(question_vector, top_n=1)
    if similar_docs:
        print("Most relevant document (human-readable):", similar_docs[0])
    else:
        print("No relevant document found.")

def fetch_and_print_all_similar(vector_db, question, top_n=3, model="mxbai-embed-large"):
    question_vector = get_ollama_embedding(question, model=model)
    similar_docs = vector_db.query_similar(question_vector, top_n=top_n)
    # Filter for documents containing the word "similar" (case-insensitive)
    filtered_docs = [doc for doc in similar_docs if "similar" in doc.lower()]
    if filtered_docs:
        print(f"Top {top_n} relevant documents containing 'similar':")
        for i, doc in enumerate(filtered_docs, 1):
            print(f"{i}. {doc}")
    else:
        print("No relevant documents found containing 'similar'.")

def main():
    # Initialize the vector database (ChromaDB)
    vector_db = VectorDatabase()

    # Add multiple example documents and store their vectors in ChromaDB
    documents = [
        "This is an example document.",
        "Python is a popular programming language.",
        "Samundar is learning about vector databases.",
        "Samundar is learning about java databases.",
        "Samundar is learning java is not a database .",
        "Samundar is learning about python databases.",
        "Ollama provides local LLM inference.",
        "all database names is SQL mongo postgresql.",
        "Vector databases are used for similarity search."
    ]
    for doc in documents:
        vector = get_ollama_embedding(doc, model="mxbai-embed-large")
        vector_db.add_document(doc, vector)

    print("All documents and their vectors have been stored in ChromaDB.")

    # Query section
    question = "databases"
    fetch_and_print_most_similar(vector_db, question)
    print("\n---\n")
    fetch_and_print_all_similar(vector_db, question, top_n=3)

if __name__ == "__main__":
    main()