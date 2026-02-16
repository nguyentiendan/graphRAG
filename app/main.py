from fastapi import FastAPI
from app.api import ingest, query
from app.graph.neo4j_client import neo4j_client
from app.core.logging import logger

app = FastAPI(title="Hybrid GraphRAG System")

# Include routers
app.include_router(ingest.router, prefix="/api/v1", tags=["ingestion"])
app.include_router(query.router, prefix="/api/v1", tags=["query"])

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")
    if neo4j_client.verify_connectivity():
        logger.info("Neo4j connectivity verified")
    else:
        logger.warning("Neo4j connectivity failed")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
    neo4j_client.close()

@app.get("/")
async def root():
    return {"message": "GraphRAG System is running"}
