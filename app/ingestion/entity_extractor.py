import json
from typing import List, Dict, Any
from app.llm.ollama import ollama_client
from app.llm.prompts import ENTITY_RELATION_EXTRACTION_PROMPT
from app.core.logging import logger

def extract_entities_relations(text: str) -> List[Dict[str, str]]:
    prompt = ENTITY_RELATION_EXTRACTION_PROMPT.format(text=text)
    try:
        response_json = ollama_client.extract_json(prompt)
        triples = response_json.get("triples", [])
        return triples
    except Exception as e:
        logger.error(f"Error extracting entities: {e}")
        return []
