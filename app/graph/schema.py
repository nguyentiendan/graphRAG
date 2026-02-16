# While Neo4j is schema-less, defining common labels and relationship types helps consistency.

class NodeLabels:
    ENTITY = "Entity"
    DOCUMENT = "Document"
    CHUNK = "Chunk"

class RelationshipTypes:
    # Genetic relations
    RELATED_TO = "RELATED_TO"
    
    # Document hierarchy
    HAS_CHUNK = "HAS_CHUNK"
    MENTIONS = "MENTIONS"
