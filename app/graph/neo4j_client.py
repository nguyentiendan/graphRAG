from neo4j import GraphDatabase
from app.core.config import settings
from app.core.logging import logger

class Neo4jClient:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            settings.NEO4J_URI,
            auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
        )
    
    def close(self):
        self.driver.close()
    
    def query(self, query: str, parameters: dict = None):
        if parameters is None:
            parameters = {}
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record.data() for record in result]

    def verify_connectivity(self):
        try:
            self.driver.verify_connectivity()
            logger.info("Connected to Neo4j")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Neo4j: {e}")
            return False

# Global client instance
neo4j_client = Neo4jClient()
