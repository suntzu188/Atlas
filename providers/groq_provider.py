"""Groq provider adapter for Atlas AI Gateway."""

import requests


class GroqProvider:
    def __init__(self, api_key, model, base_url):
        self.api_key = api_key
        self.model = model
        self.base_url = base_url

    def generate(self, message, context=None, memory=None, instructions=None):
        if not self.api_key:
            raise RuntimeError("Groq API key not configured")

        messages = [
            {"role": "system", "content": instructions or ""},
        ]

        if context:
            messages.append({"role": "assistant", "content": f"Contexto de memória relevante:\n{context}"})

        messages.append({"role": "user", "content": message})

        response = requests.post(
            self.base_url,
            json={"model": self.model, "messages": messages},
            headers={"Authorization": f"Bearer {self.api_key}"},
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
