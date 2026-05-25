import requests
from django.conf import settings

class AIService:
    def __init__(self):
        self.api_key = settings.OPENROUTER_API_KEY
        self.model = "nvidia/nemotron-3-super-120b-a12b:free"

    def generate(self, prompt: str) -> str:
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "messages": [{"role": "user", "content": prompt}]
                }
            )
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"AI Error: {str(e)}"