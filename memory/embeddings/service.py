"""Embedding layer prepared for Supabase pgvector integration."""


class EmbeddingService:
    def __init__(self, storage=None, provider=None):
        self.storage = storage
        self.provider = provider

    def generate(self, memory):
        content = memory.get("content", "")
        vector = None
        if self.provider:
            vector = self.provider.create_embedding(content)
        memory["embedding"] = vector
        if self.storage:
            self.storage.update_embedding(memory)
        return memory

    def update(self, memory):
        return self.generate(memory)

    def remove(self, memory_id):
        if self.storage:
            return self.storage.remove_embedding(memory_id)
        return True
