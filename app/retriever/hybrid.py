from app.retriever.vector import retrieve_context as retrieve_vector_context
from app.retriever.graph import retrieve_graph_context

def retrieve_hybrid_context(query: str) -> str:
    # 1. Vector Retrieval
    vector_context = retrieve_vector_context(query)
    
    # 2. Graph Retrieval
    graph_context = retrieve_graph_context(query)
    
    # 3. Merge
    combined_context = f"""
    Vector Context:
    {vector_context}
    
    Graph Context:
    {graph_context}
    """
    return combined_context
