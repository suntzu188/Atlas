"""Memory consolidation and approval preparation."""


class ConsolidationService:
    IMPORTANCE_LEVELS = ["low", "medium", "high", "critical"]

    def evaluate(self, memory):
        return {
            "importance": memory.get("importance", "medium"),
            "requires_approval": memory.get("importance") in ["high", "critical"],
        }

    def classify(self, memory):
        return self.evaluate(memory)

    def prepare_ceo_approval(self, memory):
        result = self.evaluate(memory)
        result["memory"] = memory
        return result
