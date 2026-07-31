from fastapi.testclient import TestClient

from api.main import app
from core.runtime_state import AtlasRuntimeState


client = TestClient(app)


def test_health_endpoint_available():
    response = client.get("/health")
    assert response.status_code == 200
    assert "status" in response.json()


def test_degraded_state_without_credentials():
    state = AtlasRuntimeState.degraded()
    assert state.get_status()["state"] == "idle"
    assert state.get_status()["mode"] == "degraded"


def test_full_state_with_configuration():
    state = AtlasRuntimeState.full()
    assert state.get_status()["state"] == "active"
    assert state.get_status()["mode"] == "full"
