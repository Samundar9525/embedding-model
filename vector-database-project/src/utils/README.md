# Vector Database Project

This project demonstrates how to generate embeddings for text documents using Ollama, store them in a ChromaDB vector database, and perform similarity search queries.

## Prerequisites

- **Python 3.8+**
- **Ollama** running locally (for embedding generation)
- **ChromaDB** Python package

## Installation

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd vector-database-project
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Start Ollama locally:**
   - Download and install Ollama from [https://ollama.com/](https://ollama.com/)
   - Start the Ollama server:
     ```sh
     ollama serve
     ```
   - Make sure the embedding model (e.g., `mxbai-embed-large` or `nomic-embed-text`) is available in Ollama.

## Running the Application

1. **Navigate to the source directory:**
   ```sh
   cd src
   ```

2. **Run the main script:**
   ```sh
   python main.py
   ```

3. **What happens:**
   - The script generates embeddings for a set of example documents.
   - Stores them in a persistent ChromaDB database.
   - Performs a similarity search based on a sample query.

## Project Structure

```
src/
  main.py
  database/
    vector_db.py
  utils/
    embeddings.py
requirements.txt
README.md
```

## Configuration

- You can change the embedding model in `main.py` and `embeddings.py` by modifying the `model` parameter.
- The ChromaDB persistent directory can be changed in `vector_db.py`.

---

## requirements.txt

````plaintext
chromadb
requests