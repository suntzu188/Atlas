from supabase import create_client, Client
from config.settings import SUPABASE_URL, SUPABASE_KEY


_client: Client | None = None


def get_supabase_client() -> Client:
    global _client

    if _client:
        return _client

    if not SUPABASE_URL or not SUPABASE_KEY:
        raise RuntimeError("Supabase credentials not configured")

    try:
        _client = create_client(SUPABASE_URL, SUPABASE_KEY)
        return _client
    except Exception as error:
        raise RuntimeError(f"Supabase connection failed: {error}")
