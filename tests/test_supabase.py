import os
import pytest

from database.supabase_client import get_supabase_client


@pytest.mark.skipif(
    not os.getenv("SUPABASE_URL") or not os.getenv("SUPABASE_KEY"),
    reason="Supabase environment variables not configured"
)
def test_supabase_connection():
    client = get_supabase_client()
    assert client is not None


@pytest.mark.skipif(
    not os.getenv("SUPABASE_URL") or not os.getenv("SUPABASE_KEY"),
    reason="Supabase environment variables not configured"
)
def test_supabase_read():
    client = get_supabase_client()
    response = client.table("users").select("*").limit(1).execute()
    assert response is not None
