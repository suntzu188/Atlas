"""Atlas runtime composition root."""

from config.settings import Settings
from database.supabase_client import get_supabase_client
from gateway.ai_gateway import AIGateway
from core.orchestrator import AtlasOrchestrator
from core.runtime_state import AtlasRuntimeState
from memory.service import MemoryService
from providers.qwen_provider import QwenProvider
from providers.groq_provider import GroqProvider


class AtlasRuntime:
    def __init__(self):
        self.state = AtlasRuntimeState.degraded()
        self.atlas = self._initialize()

    def _initialize(self):
        try:
            settings = Settings()
            settings.validate()

            supabase = get_supabase_client()
            memory = MemoryService(storage=supabase)

            if settings.ai_provider == "groq":
                provider = GroqProvider(
                    api_key=settings.ai_api_key,
                    model=settings.ai_model,
                    base_url=settings.ai_base_url,
                )
            else:
                provider = QwenProvider(
                    api_key=settings.ai_api_key,
                    model=settings.ai_model,
                    base_url=settings.ai_base_url,
                )

            gateway = AIGateway(provider=provider)
            self.state = AtlasRuntimeState.full()

            return AtlasOrchestrator(
                memory_service=memory,
                ai_gateway=gateway,
            )
        except Exception:
            self.state = AtlasRuntimeState.degraded()
            return AtlasOrchestrator()

    def get_status(self):
        return self.state.get_status()


runtime = AtlasRuntime()
atlas = runtime.atlas
