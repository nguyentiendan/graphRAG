# Hybrid GraphRAG System

This project implements a Hybrid GraphRAG system using FastAPI, Neo4j, LlamaIndex, and Ollama.

## Features
- **Hybrid Retrieval**: Combines vector similarity search (LlamaIndex) with graph traversal (Neo4j).
- **Multi-hop Reasoning**: Uses Neo4j to traverse relationships between entities.
- **Local Inference**: Uses Ollama for LLM tasks (Entity Extraction, Answer Generation).
- **Ingestion Pipeline**: Automated loading, chunking, extraction, and indexing.

## Prerequisites
- Docker & Docker Compose
- `uv` (for local development, optional)

## getting Started

1. **Build and Start Services**
   ```bash
   docker compose up --build
   ```

2. **Pull Ollama Models**
   Once the services are running, you need to pull the models in the Ollama container.
   ```bash
   docker exec -it graphrag-ollama-1 ollama pull llama3
   docker exec -it graphrag-ollama-1 ollama pull nomic-embed-text
   ```

3. **Ingest Documents**
   Place your documents in the `data/documents` folder (mapped volume).
   Then trigger ingestion:
   ```bash
   curl -X POST "http://localhost:8000/api/v1/ingest" \
        -H "Content-Type: application/json" \
        -d '{"directory_path": "/app/data/documents"}'
   ```

4. **Query the System**
   ```bash
   curl -X POST "http://localhost:8000/api/v1/query" \
        -H "Content-Type: application/json" \
        -d '{"query": "What are the dependencies of the system?", "mode": "hybrid"}'
   ```

## API Documentation
The API documentation is available at `http://localhost:8000/docs`.

## Configuration
Environment variables can be set in `docker-compose.yml` or a `.env` file.
- `NEO4J_URI`: Neo4j Bolt URI
- `NEO4J_USER`: Neo4j User
- `NEO4J_PASSWORD`: Neo4j Password
- `OLLAMA_BASE_URL`: Ollama API URL
