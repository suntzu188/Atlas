"""Atlas Core orchestration pipeline."""


class AtlasOrchestrator:
    def __init__(self, memory_service=None, ai_gateway=None):
        self.memory = memory_service
        self.ai_gateway = ai_gateway

    def process_message(self, message):
        context = ""
        memories = []

        try:
            if self.memory:
                memories = self.memory.retrieve_memories(message)
                context = self.memory.prepare_context(message)

            if not self.ai_gateway:
                raise RuntimeError("AI Gateway unavailable")

            response = self.ai_gateway.generate_response(
                message=message,
                context=context,
                memory=memories,
                instructions="Você é o Atlas, um sistema cognitivo assistente."
            )

            if self.memory:
                self.memory.save_memory(
                    f"Usuário: {message}\nAtlas: {response}",
                    memory_type="episodic"
                )

            return response

        except Exception as error:
            return f"Atlas temporariamente indisponível: {error}"
