from typing import List, Dict

ENTITY_RELATION_EXTRACTION_PROMPT = """
You are an information extraction system.

Given the following text, extract structured knowledge in the form of
(subject, relation, object) triples.

Rules:
- Subjects and objects must be concrete entities.
- Use concise relation names (e.g., DEPENDS_ON, USES, PART_OF).
- Do not hallucinate facts.
- If no relation exists, return an empty list.

Text:
{text}

Return JSON only in the following format:

{{
  "triples": [
    {{
      "subject": "string",
      "relation": "string",
      "object": "string"
    }}
  ]
}}
"""

QUERY_ENTITY_EXTRACTION_PROMPT = """
Extract all relevant entities from the following user query.

Rules:
- Return only entities explicitly or implicitly mentioned.
- Do not include explanations.

Query:
{query}

Return JSON only:

{{
  "entities": ["entity1", "entity2"]
}}
"""

COMMUNITY_SUMMARY_PROMPT = """
You are summarizing a knowledge graph subgraph.

Given the following entities and relationships, produce a concise
high-level summary explaining what this subgraph represents.

Rules:
- Focus on system-level meaning.
- Avoid listing raw relationships.
- Keep the summary under 150 words.

Graph Data:
{graph_context}

Return plain text only.
"""

FINAL_ANSWER_PROMPT = """
You are a question-answering assistant.

Use ONLY the provided context to answer the question.
If the answer cannot be determined, say so explicitly.

Context:
{context}

Question:
{query}

Answer:
"""
