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

def get_top_n_records(vector_db, question, top_n=10, model="mxbai-embed-large"):
    question_vector = get_ollama_embedding(question, model=model)
    similar_docs = vector_db.query_similar(question_vector, top_n=30)
    keywords = [word.lower() for word in question.split() if len(word) > 2]
    filtered_docs = []
    for doc in similar_docs:
        doc_lower = doc.lower()
        if any(keyword in doc_lower for keyword in keywords):
            filtered_docs.append(doc)
    # Remove duplicates while preserving order
    seen = set()
    unique_docs = []
    for doc in filtered_docs:
        if doc not in seen:
            unique_docs.append(doc)
            seen.add(doc)
        if len(unique_docs) == top_n:
            break
    if unique_docs:
        print(f"Top {top_n} relevant documents for your question:")
        for i, doc in enumerate(unique_docs, 1):
            print(f"{i}. {doc}")
    else:
        print("No relevant documents found for your question.")

def main():
    # Initialize the vector database (ChromaDB)
    vector_db = VectorDatabase()

    # Add multiple example documents and store their vectors in ChromaDB
    documents = [
        "Samundar is learning about vector databases.",
        "Python is a popular programming language.",
        "Samundar is learning about java databases.",
        "Samundar is learning java is not a database.",
        "Samundar is learning about python databases.",
        "Ollama provides local LLM inference.",
        "All database names are SQL, Mongo, and PostgreSQL.",
        "Vector databases are used for similarity search.",
        "Samundar enjoys hiking in the mountains.",
        "Samundar loves eating pizza.",
        "Samundar likes to eat spicy noodles.",
        "Samundar is a fan of Italian pasta.",
        "Samundar enjoys sushi with friends.",
        "Samundar is learning about neural networks.",
        "Data science combines statistics and programming.",
        "Samundar is learning about REST APIs.",
        "The capital of France is Paris.",
        "Samundar is learning about Docker containers.",
        "Deep learning uses neural networks with many layers.",
        "Samundar is learning about Kubernetes.",
        "The quick brown fox jumps over the lazy dog.",
        "Samundar is learning about data visualization.",
        "Big data technologies include Hadoop and Spark.",
        "Samundar is learning about SQL joins.",
        "Natural language processing enables chatbots.",
        "Samundar is learning about time series analysis.",
        "The stock market fluctuates daily.",
        "Samundar is learning about reinforcement learning.",
        "Quantum computing is an emerging field.",
        "Samundar is learning about blockchain technology.",
        "Cybersecurity is important for protecting data.",
        "Samundar is learning about computer vision.",
        "Edge computing brings computation closer to data sources.",
        "Samundar is learning about distributed systems.",
        "The internet of things connects devices worldwide.",
        "Samundar is learning about graph databases.",
        "Samundar enjoys eating chocolate cake.",
        "Samundar is learning about recommendation systems.",
        "Cloud storage solutions include AWS S3 and Google Drive.",
        "Samundar is learning about big O notation.",
        "Mobile app development uses Swift and Kotlin.",
        "Samundar is learning about agile methodologies.",
        "Version control systems include Git and SVN.",
        "Samundar is learning about microservices architecture.",
        "APIs allow different software systems to communicate.",
        "Samundar is learning about encryption algorithms.",
        "Samundar likes eating fresh salad.",
        "Samundar is learning about feature engineering.",
        "Self-driving cars use sensors and AI.",
        "Samundar is learning about transfer learning."
    ]
    for doc in documents:
        vector = get_ollama_embedding(doc, model="mxbai-embed-large")
        vector_db.add_document(doc, vector)

    print("All documents and their vectors have been stored in ChromaDB.")

    # Query section
    question = "what is samundar learning and eating?"
    get_top_n_records(vector_db, question, top_n=10)

if __name__ == "__main__":
    main()