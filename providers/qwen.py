"""Qwen API provider adapter."""

import requests


class QwenProvider:
    def __init__(self, api_key, model, base_url):
        self.api_key = api_key
        self.model = model
        self.base_url = base_url

    def generate(self, message, context="", memory=None, instructions=""):
        if not self.api_key:
            raise RuntimeError("Qwen API key not configured")

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": instructions},
                {"role": "user", "content": message},
            ],
        }

        try:
            response = requests.post(
                self.base_url,
                headers={"Authorization": f"Bearer {self.api_key}"},
                json=payload,
                timeout=30,
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except Exception as error:
            raise RuntimeError(f"Qwen provider error: {error}")
