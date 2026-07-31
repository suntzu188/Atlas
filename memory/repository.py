from database.supabase_client import get_supabase_client


def save_conversation(user_id: str, content: str):
    client = get_supabase_client()
    return client.table("conversations").insert({
        "user_id": user_id,
        "content": content
    }).execute()


def get_conversation_history(user_id: str):
    client = get_supabase_client()
    return client.table("conversations").select("*").eq("user_id", user_id).execute()


def save_memory(user_id: str, content: str, memory_type: str = "episodic"):
    client = get_supabase_client()
    return client.table("memories").insert({
        "user_id": user_id,
        "content": content,
        "type": memory_type
    }).execute()


def get_user_information(user_id: str):
    client = get_supabase_client()
    return client.table("users").select("*").eq("id", user_id).execute()
