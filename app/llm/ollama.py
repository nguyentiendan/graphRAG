import json
from ollama import Client
from app.core.config import settings
from app.core.logging import logger

class OllamaClient:
    def __init__(self):
        self.client = Client(host=settings.OLLAMA_BASE_URL)
        self.model = settings.OLLAMA_MODEL

    def generate(self, prompt: str, system: str = None, json_mode: bool = False):
        try:
            options = {}
            format = None
            if json_mode:
                format = "json"
            
            response = self.client.generate(
                model=self.model,
                prompt=prompt,
                system=system,
                format=format,
                stream=False
            )
            return response['response']
        except Exception as e:
            logger.error(f"Ollama generation failed: {e}")
            raise e

    def extract_json(self, prompt: str, system: str = None):
        response_text = self.generate(prompt, system, json_mode=True)
        try:
            return json.loads(response_text)
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON from Ollama response: {response_text}")
            return {}

ollama_client = OllamaClient()
