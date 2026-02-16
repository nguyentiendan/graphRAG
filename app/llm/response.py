from app.llm.ollama import ollama_client
from app.llm.prompts import FINAL_ANSWER_PROMPT

def generate_answer(query: str, context: str) -> str:
    """
    Generate a grounded answer using the provided context and query.
    """
    prompt = FINAL_ANSWER_PROMPT.format(context=context, query=query)
    # response = ollama_client.generate(prompt) # The prompt template already includes instruction, so system prompt might be redundant or we can set a generic one.
    # Let's just use the prompt as is.
    return ollama_client.generate(prompt)
