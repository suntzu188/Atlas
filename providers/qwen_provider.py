"""Qwen provider adapter for Atlas AI Gateway."""

import requests


class QwenProvider:
    def __init__(self, api_key, model, base_url):
        self.api_key = api_key
        self.model = model
        self.base_url = base_url

    def generate(self, message, context=None, memory=None, instructions=None):
        if not self.api_key:
            raise RuntimeError("Qwen API key not configured")

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": instructions or ""},
                {"role": "user", "content": message},
            ],
        }

        response = requests.post(
            self.base_url,
            json=payload,
            headers={"Authorization": f"Bearer {self.api_key}"},
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
