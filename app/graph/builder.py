from typing import List, Dict
from app.graph.neo4j_client import neo4j_client
from app.graph.schema import NodeLabels, RelationshipTypes
from app.core.logging import logger

class GraphBuilder:
    def __init__(self, client=neo4j_client):
        self.client = client

    def insert_triples(self, triples: List[Dict[str, str]]):
        if not triples:
            return

        query = f"""
        UNWIND $triples AS triple
        MERGE (s:{NodeLabels.ENTITY} {{name: triple.subject}})
        MERGE (o:{NodeLabels.ENTITY} {{name: triple.object}})
        WITH s, o, triple
        CALL apoc.create.relationship(s, triple.relation, {{}}, o) YIELD rel
        RETURN count(rel)
        """
        try:
            self.client.query(query, {"triples": triples})
        except Exception as e:
            logger.error(f"Failed to insert triples: {e}")

    def link_chunk_to_entities(self, chunk_id: str, entities: List[str]):
        if not entities:
            return

        query = f"""
        MATCH (c:{NodeLabels.CHUNK} {{id: $chunk_id}})
        UNWIND $entities AS entity_name
        MERGE (e:{NodeLabels.ENTITY} {{name: entity_name}})
        MERGE (c)-[:{RelationshipTypes.MENTIONS}]->(e)
        """
        # Note: We assume Chunk node is created separately or we create it here.
        # Let's ensure Chunk node exists.
        
        create_chunk_query = f"""
        MERGE (c:{NodeLabels.CHUNK} {{id: $chunk_id}})
        """
        try:
            self.client.query(create_chunk_query, {"chunk_id": chunk_id})
            self.client.query(query, {"chunk_id": chunk_id, "entities": entities})
        except Exception as e:
            logger.error(f"Failed to link chunk to entities: {e}")

graph_builder = GraphBuilder()
