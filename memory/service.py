"""Central memory service for Atlas Advanced Memory System."""

from datetime import datetime

from memory.embeddings.service import EmbeddingService
from memory.retrieval.service import RetrievalService
from memory.consolidation.service import ConsolidationService


class MemoryService:
    """Coordinates memory storage, retrieval and context preparation."""

    def __init__(self, storage=None):
        self.storage = storage
        self.embeddings = EmbeddingService(storage)
        self.retrieval = RetrievalService(storage)
        self.consolidation = ConsolidationService()

    def save_memory(self, content, memory_type="episodic", importance="medium"):
        record = {
            "content": content,
            "type": memory_type,
            "importance": importance,
            "created_at": datetime.utcnow().isoformat(),
        }
        if self.storage:
            record = self.storage.insert_memory(record)
        self.embeddings.generate(record)
        return record

    def retrieve_memories(self, query, limit=5):
        return self.retrieval.search(query, limit)

    def prepare_context(self, query, limit=5):
        memories = self.retrieve_memories(query, limit)
        return "\n".join(item.get("content", "") for item in memories)
