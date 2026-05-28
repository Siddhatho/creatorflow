from groq import Groq
from django.conf import settings

class AIService:
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = "llama-3.1-8b-instant"

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"AI Error: {str(e)}"
        
         
    # def __init__(self):
    #     self.api_key = settings.OPENROUTER_API_KEY
    #     self.model = "nvidia/nemotron-3-super-120b-a12b:free"

    # def generate(self, prompt: str) -> str:
    #     try:
    #         response = requests.post(
    #             "https://openrouter.ai/api/v1/chat/completions",
    #             headers={
    #                 "Authorization": f"Bearer {self.api_key}",
    #                 "Content-Type": "application/json"
    #             },
    #             json={
    #                 "model": self.model,
    #                 "messages": [{"role": "user", "content": prompt}]
    #             }
    #         )
    #         data = response.json()
    #         return data['choices'][0]['message']['content']
    #     except Exception as e:
    #         import json
    #         return f"AI Error: {str(e)} | Response: {response.text[:200]}"