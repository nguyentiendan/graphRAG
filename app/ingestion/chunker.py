from typing import List
from llama_index.core.schema import BaseNode
from llama_index.core.node_parser import SentenceSplitter

def chunk_text(documents: List, chunk_size: int = 512, chunk_overlap: int = 50) -> List[BaseNode]:
    splitter = SentenceSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    nodes = splitter.get_nodes_from_documents(documents)
    return nodes
