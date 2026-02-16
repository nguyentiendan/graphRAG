from typing import List
from app.llm.ollama import ollama_client
from app.llm.prompts import QUERY_ENTITY_EXTRACTION_PROMPT
from app.graph.traversal import graph_traversal
from app.core.logging import logger

def extract_query_entities(query: str) -> List[str]:
    prompt = QUERY_ENTITY_EXTRACTION_PROMPT.format(query=query)
    try:
        response = ollama_client.extract_json(prompt)
        return response.get("entities", [])
    except Exception as e:
        logger.error(f"Failed to extract entities from query: {e}")
        return []

def retrieve_graph_context(query: str, depth: int = 2) -> str:
    entities = extract_query_entities(query)
    if not entities:
        return ""
    
    context_parts = []
    for entity in entities:
        # 1-hop
        # context_parts.append(graph_traversal.one_hop_traversal(entity))
        # Multi-hop
        paths = graph_traversal.multi_hop_traversal(entity, depth=depth)
        
        for p in paths:
            # Format: Subject RELATION Object
            context_parts.append(f"{p['source']} {p['relation']} {p['target']}")
            
    return "\n".join(list(set(context_parts)))
