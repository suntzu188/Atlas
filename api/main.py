"""Atlas API chat endpoint."""

from fastapi import FastAPI
from pydantic import BaseModel

from core.orchestrator import AtlasOrchestrator


app = FastAPI(title="Atlas Core", version="0.1.0")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


orchestrator = AtlasOrchestrator()


@app.get("/")
def health_check():
    return {"status": "Atlas Core online", "version": "0.1.0"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = orchestrator.process_message(request.message)
    return ChatResponse(response=response)
