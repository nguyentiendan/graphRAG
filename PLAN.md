# Hybrid GraphRAG System Implementation Plan

## Goal Description
Build a complete, runnable Hybrid GraphRAG system using FastAPI, LlamaIndex, Neo4j, and Ollama. The system will support vector-based retrieval, knowledge graph retrieval, and multi-hop reasoning.

## Proposed Changes
The project will be structured under a graphrag/ directory within the current workspace.

## Directory Structure

graphrag/

app/ (Application logic)
  main.py
  (FastAPI entrypoint)
  api/
  (API endpoints: ingest, query, schemas)
  core/ (Config, logging)
  ingestion/ (Loader, chunker, extractor, pipeline)
  graph/ (Neo4j client, schema, builder, traversal)
  retriever/ (Vector, graph, community, hybrid)
  llm/ (Ollama, prompts, response)
  utils/ (Text, IDs)
data/ (Storage for documents, indexes, summaries)
docker/ (Dockerfiles)
docker-compose.yml

## Core Components

1. FastAPI Application:

  - Expose /ingest and /query endpoints.
  - Use Pydantic models for request/response bodies.

2. Neo4j Graph Database:

  - Store entities and relationships extracted from documents.
  - Support multi-hop traversal queries.
  - Update: Implementing neo4j_client.py using official Neo4j Python driver.

3. LlamaIndex Vector Store:

  - Store vector embeddings for semantic search.
  - Persist indexes locally.

4. Ollama LLM Integration:

  - Local inference for entity extraction and answer generation.
  - Use JSON mode for structured extraction.
  - Update: Implementing prompts.py with specific templates for extraction and synthesis.

5. Ingestion Pipeline:

  - Load -> Chunk -> Extract (LLM) -> Insert to Graph -> Embed -> Link.

6. Retrieval Pipeline:

  - Extract query entities -> Traverse Graph (n-hop) -> Vector Search -> Merge -> Answer.

## Verification Plan

### Automated Tests

  - Verify all services start with docker compose up --build.
  - Verify /ingest accepts documents and populates both Neo4j and vector store.
  - Verify /query returns grounded answers using both graph and vector context.

### Manual Verification

  - Inspect Neo4j browser for correct graph structure.
  - Check vector store persistence.
