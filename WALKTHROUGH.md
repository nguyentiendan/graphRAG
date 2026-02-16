# Hybrid GraphRAG System Walkthrough
I have built a complete Hybrid GraphRAG system that combines vector retrieval with knowledge graph capabilities.

## System Components
### 1. Core Infrastructure
- Neo4j: Graph database for storing entities and relationships.
- LlamaIndex: Vector store for semantic search.
- Ollama: Local LLM for extraction and generation.
- FastAPI: REST API for ingestion and querying.
### 2. Ingestion Pipeline (app/ingestion)
Loader: Loads documents from a directory.
Chunker: Splits text into chunks.
Extractor: Uses LLM to extract (Subject, Relation, Object) triples.
Graph Builder: Inserts triples into Neo4j and links chunks to entities.
Vector Indexer: Embeds chunks and stores them in a local vector index.
### 3. Retrieval Pipeline (app/retriever)
- Graph Traversal: Performs multi-hop traversal (default depth=2) starting from entities found in the query.
- Vector Retrieval: Finds semantically similar text chunks.
- Hybrid Merger: Combines context from both sources.
### 4. API Endpoints (app/api)
- POST /api/v1/ingest: Triggers the ingestion process.
- POST /api/v1/query: Answers questions using Hybrid, Vector, or Graph modes.

## How to Run
### Start Services:

```bash
cd graphrag
docker compose up --build
```

### Pull Models (in a separate terminal):

```bash
docker exec -it graphrag-ollama-1 ollama pull llama3
docker exec -it graphrag-ollama-1 ollama pull nomic-embed-text
```

### Use the API:
- Docs available at http://localhost:8000/docs.
- Ingest documents by placing them in graphrag/data/documents