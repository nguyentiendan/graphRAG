from fastapi import APIRouter, HTTPException, BackgroundTasks
from app.api.schemas import IngestRequest, IngestResponse
from app.ingestion.pipeline import run_ingestion
from app.core.logging import logger

router = APIRouter()

@router.post("/ingest", response_model=IngestResponse)
async def ingest_documents(request: IngestRequest, background_tasks: BackgroundTasks):
    # Validation
    # if not os.path.exists(request.directory_path):
    #     raise HTTPException(status_code=400, detail="Directory not found")
    
    # Run in background to avoid blocking
    background_tasks.add_task(run_ingestion, request.directory_path)
    
    return IngestResponse(
        message="Ingestion started in background",
        documents_processed=0 # We don't know yet
    )
