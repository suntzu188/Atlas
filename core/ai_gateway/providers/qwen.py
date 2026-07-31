import os
import requests


def generate_response(message, context=None, memory=None, instructions=None):
    api_key = os.getenv("AI_API_KEY")
    base_url = os.getenv("AI_BASE_URL")
    model = os.getenv("AI_MODEL")

    if not api_key:
        raise RuntimeError("AI_API_KEY not configured")

    if not base_url or not model:
        raise RuntimeError("AI provider configuration incomplete")

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": instructions or ""},
            {"role": "user", "content": message}
        ]
    }

    try:
        response = requests.post(
            base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            json=payload,
            timeout=30,
        )
        response.raise_for_status()
    except requests.RequestException as error:
        raise RuntimeError(f"Qwen connection failed: {error}")

    data = response.json()

    if "choices" not in data:
        raise RuntimeError("Invalid AI response")

    return data
