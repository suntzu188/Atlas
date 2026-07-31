"""Supabase client factory for Atlas."""

from supabase import Client, create_client

from config.settings import Settings


_client: Client | None = None


def get_supabase_client() -> Client:
    global _client

    if _client:
        return _client

    settings = Settings()
    settings.validate()

    if not settings.supabase_url or not settings.supabase_key:
        raise RuntimeError("Supabase credentials not configured")

    try:
        _client = create_client(settings.supabase_url, settings.supabase_key)
        return _client
    except Exception as error:
        raise RuntimeError(f"Supabase connection failed: {error}")
