"""Initial Atlas cognitive cycle tests."""

from unittest.mock import Mock


def test_atlas_orchestrator_cycle():
    from core.orchestrator import AtlasOrchestrator

    memory = Mock()
    memory.retrieve_memories.return_value = []
    memory.prepare_context.return_value = ""

    gateway = Mock()
    gateway.generate_response.return_value = "Atlas response"

    atlas = AtlasOrchestrator(memory_service=memory, ai_gateway=gateway)

    result = atlas.process_message("hello")

    assert result == "Atlas response"
    memory.save_memory.assert_called_once()


def test_provider_failure_is_handled():
    from core.orchestrator import AtlasOrchestrator

    gateway = Mock()
    gateway.generate_response.side_effect = RuntimeError("provider error")

    atlas = AtlasOrchestrator(ai_gateway=gateway)

    result = atlas.process_message("hello")

    assert "indisponível" in result
