"""Atlas API chat endpoint."""

from fastapi import FastAPI
from pydantic import BaseModel

from core.orchestrator import AtlasOrchestrator
from memory.service import MemoryService
from gateway.ai_gateway import AIGateway


app = FastAPI(title="Atlas Core", version="0.1.0")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


orchestrator = AtlasOrchestrator(
    memory_service=MemoryService(),
    ai_gateway=AIGateway()
)


@app.get("/")
def health_check():
    return {"status": "Atlas Core online", "version": "0.1.0"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(
        response=orchestrator.process_message(request.message)
    )
