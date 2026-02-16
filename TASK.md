# Task: Build Hybrid GraphRAG System

## Scaffolding & Configuration

- Create project directory structure graphrag/
- Create pyproject.toml and lock file
- Create docker/Dockerfile.api and docker/Dockerfile.ollama
- Create docker-compose.yml
- Implement app/core/config.py and app/core/logging.py

## Core Graph & LLM Components

- Implement app/graph/neo4j_client.py
- Implement app/llm/prompts.py (Integrate provided templates)
- Implement app/llm/ollama.py
- Implement app/llm/response.py

## Ingestion Pipeline

- Implement app/graph/schema.py (Node & relationship definitions)
- Implement app/ingestion/loader.py & chunker.py
- Implement app/ingestion/entity_extractor.py
- Implement app/graph/builder.py (Graph insertion)
- Implement app/ingestion/pipeline.py (Orchestrator)

## Retrieval & Query Pipeline

- Implement app/graph/traversal.py (Cypher queries)
- Implement app/retriever/vector.py (LlamaIndex)
- Implement app/retriever/graph.py (Neo4j)
- Implement app/retriever/hybrid.py (Merge logic)
- Implement app/api/query.py, app/api/ingest.py, app/api/schemas.py
- Implement app/main.py (FastAPI entrypoint)

## Verification

- Verify file structure
- Create README.md with run instructions