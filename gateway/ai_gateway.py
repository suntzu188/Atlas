"""Atlas AI Gateway abstraction."""

import os


class AIGateway:
    def __init__(self, provider=None):
        self.provider = provider

    def generate_response(self, message, context=None, memory=None, instructions=None):
        if not self.provider:
            raise RuntimeError("AI provider not configured")

        return self.provider.generate(
            message=message,
            context=context or "",
            memory=memory or [],
            instructions=instructions or ""
        )
