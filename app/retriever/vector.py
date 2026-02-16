from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.embeddings.ollama import OllamaEmbedding
from app.core.config import settings

INDEX_DIR = "./data/indexes"

def get_vector_retriever(similarity_top_k: int = 5):
    embed_model = OllamaEmbedding(
        model_name=settings.EMBEDDING_MODEL,
        base_url=settings.OLLAMA_BASE_URL,
    )
    
    storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
    index = load_index_from_storage(storage_context, embed_model=embed_model)
    
    return VectorIndexRetriever(index=index, similarity_top_k=similarity_top_k)

def retrieve_context(query: str, top_k: int = 5):
    try:
        retriever = get_vector_retriever(similarity_top_k=top_k)
        nodes = retriever.retrieve(query)
        return "\n".join([node.get_content() for node in nodes])
    except Exception as e:
        print(f"Vector retrieval failed (index might not exist): {e}")
        return ""
