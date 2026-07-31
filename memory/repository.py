"""Supabase adapter for Atlas persistent memory."""


class MemoryRepository:
    def __init__(self, client):
        self.client = client

    def insert_memory(self, record):
        result = self.client.table("memories").insert({
            "content": record.get("content"),
            "memory_type": record.get("type", "episodic"),
            "embedding": record.get("embedding"),
            "metadata": {},
        }).execute()
        return result.data[0] if result.data else record

    def search_memory(self, query, limit=5):
        result = self.client.table("memories").select("*").ilike("content", f"%{query}%").limit(limit).execute()
        return result.data or []

    def get_recent_memories(self, limit=5):
        result = self.client.table("memories").select("*").order("created_at", desc=True).limit(limit).execute()
        return result.data or []

    def semantic_search(self, query, limit=5):
        return self.search_memory(query, limit)


def save_conversation(user_id: str, content: str):
    from database.supabase_client import get_supabase_client
    return get_supabase_client().table("conversations").insert({"user_id": user_id, "content": content}).execute()


def get_conversation_history(user_id: str):
    from database.supabase_client import get_supabase_client
    return get_supabase_client().table("conversations").select("*").eq("user_id", user_id).execute()


def save_memory(user_id: str, content: str, memory_type: str = "episodic"):
    from database.supabase_client import get_supabase_client
    return get_supabase_client().table("memories").insert({"user_id": user_id, "content": content, "type": memory_type}).execute()


def get_user_information(user_id: str):
    from database.supabase_client import get_supabase_client
    return get_supabase_client().table("users").select("*").eq("id", user_id).execute()
