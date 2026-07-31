"""Atlas runtime composition root."""

from config.settings import Settings
from database.supabase_client import get_supabase_client
from gateway.ai_gateway import AIGateway
from core.orchestrator import AtlasOrchestrator
from memory.service import MemoryService
from providers.qwen_provider import QwenProvider


def create_atlas():
    settings = Settings()
    settings.validate()

    supabase = get_supabase_client()
    memory = MemoryService(storage=supabase)

    provider = QwenProvider(
        api_key=settings.ai_api_key,
        model=settings.ai_model,
        base_url=settings.ai_base_url,
    )

    gateway = AIGateway(provider=provider)

    return AtlasOrchestrator(
        memory_service=memory,
        ai_gateway=gateway,
    )


atlas = create_atlas()
