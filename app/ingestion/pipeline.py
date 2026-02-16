import os
from typing import List
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core.schema import TextNode
from llama_index.embeddings.ollama import OllamaEmbedding

from app.core.config import settings
from app.core.logging import logger
from app.ingestion.loader import load_documents
from app.ingestion.chunker import chunk_text
from app.ingestion.entity_extractor import extract_entities_relations
from app.graph.builder import graph_builder

# Initialize embedding model
embed_model = OllamaEmbedding(
    model_name=settings.EMBEDDING_MODEL,
    base_url=settings.OLLAMA_BASE_URL,
)

INDEX_DIR = "./data/indexes"

def run_ingestion(directory_path: str):
    logger.info(f"Starting ingestion from {directory_path}")
    
    # 1. Load Documents
    documents = load_documents(directory_path)
    logger.info(f"Loaded {len(documents)} documents")

    # 2. Chunk Text
    nodes = chunk_text(documents)
    logger.info(f"Created {len(nodes)} chunks")

    # 3. Process Chunks (Extract & Graph Insert)
    annotated_nodes = []
    
    for node in nodes:
        text = node.get_content()
        triples = extract_entities_relations(text)
        
        extracted_entities = list(set([t['subject'] for t in triples] + [t['object'] for t in triples]))
        
        # Insert into Graph
        graph_builder.insert_triples(triples)
        graph_builder.link_chunk_to_entities(node.node_id, extracted_entities)
        
        # Add metadata to node for vector store
        node.metadata["entities"] = extracted_entities
        annotated_nodes.append(node)

    # 4. Create/Update Vector Index
    logger.info("Building vector index...")
    if not os.path.exists(INDEX_DIR):
        os.makedirs(INDEX_DIR)
        index = VectorStoreIndex(annotated_nodes, embed_model=embed_model)
        index.storage_context.persist(persist_dir=INDEX_DIR)
    else:
        storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
        index = load_index_from_storage(storage_context, embed_model=embed_model)
        index.insert_nodes(annotated_nodes)
        index.storage_context.persist(persist_dir=INDEX_DIR)

    logger.info("Ingestion complete.")
