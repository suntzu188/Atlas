"""Atlas runtime state model."""


class AtlasRuntimeState:
    def __init__(self, mode="degraded", state="idle", reason=None):
        self.mode = mode
        self.state = state
        self.reason = reason

    def get_status(self):
        response = {
            "status": "online",
            "state": self.state,
            "mode": self.mode,
            "version": "0.1.0",
        }
        if self.reason:
            response["reason"] = self.reason
        return response

    @classmethod
    def degraded(cls, reason="serviço indisponível ou aguardando configuração"):
        return cls(mode="degraded", state="idle", reason=reason)

    @classmethod
    def full(cls):
        return cls(mode="full", state="active")
