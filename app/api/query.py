from fastapi import APIRouter, HTTPException
from app.api.schemas import QueryRequest, QueryResponse
from app.retriever.hybrid import retrieve_hybrid_context
from app.retriever.vector import retrieve_context as retrieve_vector_context
from app.retriever.graph import retrieve_graph_context
from app.llm.response import generate_answer

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def query_system(request: QueryRequest):
    if request.mode == "hybrid":
        context = retrieve_hybrid_context(request.query)
    elif request.mode == "vector":
        context = retrieve_vector_context(request.query)
    elif request.mode == "graph":
        context = retrieve_graph_context(request.query)
    else:
        raise HTTPException(status_code=400, detail="Invalid mode")
    
    answer = generate_answer(request.query, context)
    
    return QueryResponse(
        answer=answer,
        context=context
    )
