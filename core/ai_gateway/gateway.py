import os

from .providers import qwen


def generate_response(message, context=None, memory=None, instructions=None):
    provider = os.getenv("AI_PROVIDER", "qwen")

    if provider == "qwen":
        return qwen.generate_response(
            message=message,
            context=context,
            memory=memory,
            instructions=instructions,
        )

    raise RuntimeError(f"Unsupported AI provider: {provider}")
