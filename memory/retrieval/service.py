"""Semantic retrieval layer prepared for Supabase similarity search."""


class RetrievalService:
    def __init__(self, storage=None):
        self.storage = storage

    def search(self, query, limit=5):
        if self.storage and hasattr(self.storage, "semantic_search"):
            return self.storage.semantic_search(query, limit)
        return []

    def rank(self, memories):
        return sorted(
            memories,
            key=lambda item: item.get("similarity", 0),
            reverse=True,
        )
