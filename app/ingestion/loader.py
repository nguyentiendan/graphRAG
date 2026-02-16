from typing import List
from llama_index.core import Document, SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter

def load_documents(directory_path: str) -> List[Document]:
    reader = SimpleDirectoryReader(directory_path, recursive=True)
    return reader.load_data()

def chunk_documents(documents: List[Document], chunk_size: int = 1024, chunk_overlap: int = 20) -> List[Document]:
    splitter = SentenceSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    nodes = splitter.get_nodes_from_documents(documents)
    # Convert nodes back to documents-like objects or keep as nodes. 
    # For extraction, we need text.
    return nodes
