from providers.qwen import QwenProvider


def test_provider_without_key():
    provider = QwenProvider(None, "model", "url")
    try:
        provider.generate("hello")
        assert False
    except RuntimeError:
        assert True


def test_provider_error_handling():
    provider = QwenProvider("key", "model", "invalid")
    try:
        provider.generate("hello")
        assert False
    except RuntimeError:
        assert True
