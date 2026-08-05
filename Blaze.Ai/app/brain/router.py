from app.brain.providers.ollama import OllamaProvider


class Router:

    def __init__(self):

        self.ollama = OllamaProvider()

    def select(self, prompt: str):

        prompt = prompt.lower()

        # Later we'll route based on task type.
        # For now always use Ollama.

        return self.ollama