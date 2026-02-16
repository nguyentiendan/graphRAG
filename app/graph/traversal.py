from typing import List, Dict, Any
from app.graph.neo4j_client import neo4j_client

class GraphTraversal:
    def __init__(self, client=neo4j_client):
        self.client = client

    def one_hop_traversal(self, entity_name: str) -> List[Dict]:
        query = """
        MATCH (e:Entity {name: $entity})-[r]->(n:Entity)
        RETURN e.name AS source, type(r) AS relation, n.name AS target
        """
        return self.client.query(query, {"entity": entity_name})

    def multi_hop_traversal(self, entity_name: str, depth: int = 2) -> List[Dict]:
        query = f"""
        MATCH p=(e:Entity {{name: $entity}})-[*1..{depth}]-(n:Entity)
        RETURN p
        LIMIT 50
        """
        # Note: returning paths directly might be complex to parse. 
        # Simpler approach: return relationships.
        # But user requirement says "RETURN p". Neo4j driver returns Path objects.
        # We need to serialize them.
        
        # Let's construct a cleaner return for consumption
        query = f"""
        MATCH (e:Entity {{name: $entity}})-[r*1..{depth}]-(n:Entity)
        UNWIND r AS rel
        RETURN startNode(rel).name AS source, type(rel) AS relation, endNode(rel).name AS target
        LIMIT 100
        """
        return self.client.query(query, {"entity": entity_name})

graph_traversal = GraphTraversal()
