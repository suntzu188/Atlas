from unittest.mock import Mock, patch

import pytest

from providers.groq_provider import GroqProvider


def test_groq_requires_api_key():
    provider = GroqProvider("", "model", "url")

    with pytest.raises(RuntimeError):
        provider.generate("hello")


def test_groq_http_error():
    provider = GroqProvider("key", "model", "url")

    response = Mock()
    response.raise_for_status.side_effect = RuntimeError("http error")

    with patch("providers.groq_provider.requests.post", return_value=response):
        with pytest.raises(RuntimeError):
            provider.generate("hello")


def test_groq_response():
    provider = GroqProvider("key", "model", "url")

    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = {
        "choices": [
            {"message": {"content": "ok"}}
        ]
    }

    with patch("providers.groq_provider.requests.post", return_value=response):
        assert provider.generate("hello") == "ok"
