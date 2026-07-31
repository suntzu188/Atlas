import os
import pytest

from core.ai_gateway import generate_response


def test_gateway_provider_selection(monkeypatch):
    monkeypatch.setenv("AI_PROVIDER", "qwen")
    assert os.getenv("AI_PROVIDER") == "qwen"


def test_configuration_missing():
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.delenv("AI_API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        generate_response("teste")
    monkeypatch.undo()
