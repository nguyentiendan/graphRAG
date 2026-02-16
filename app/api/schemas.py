from typing import List, Optional
from pydantic import BaseModel

class IngestRequest(BaseModel):
    # Depending on how we ingest, maybe a path or raw text.
    # Requirement says "d) Ingestion Pipeline ... Load documents".
    # Let's support a local directory path for simplicity as per requirements, or maybe file upload.
    # Given "Load documents" typically implies from a source, let's allow specifying a directory path on the server 
    # (mapped via volume) or just a trigger.
    # For a robust API, file upload is better, but "Load documents" from folder structure implies we might just trigger it.
    # Let's support a directory path that exists in the container (e.g., /app/data/documents).
    directory_path: str = "/app/data/documents"

class IngestResponse(BaseModel):
    message: str
    documents_processed: int

class QueryRequest(BaseModel):
    query: str
    mode: str = "hybrid" # hybrid, vector, graph

class QueryResponse(BaseModel):
    answer: str
    context: Optional[str] = None
