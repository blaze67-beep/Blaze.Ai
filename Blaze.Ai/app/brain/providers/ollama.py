import requests

from app.brain.providers.base import AIProvider
from app.brain.personality import SYSTEM_PROMPT


class OllamaProvider(AIProvider):

    def __init__(self):

        self.url = "http://127.0.0.1:11434/api/generate"
        self.model = "qwen2.5:3b"

    def chat(self, prompt: str) -> str:

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "system": SYSTEM_PROMPT,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data["response"].strip()