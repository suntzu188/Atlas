"""Atlas API chat endpoint."""

from fastapi import FastAPI
from pydantic import BaseModel

from bootstrap import atlas


app = FastAPI(title="Atlas Core", version="0.1.0")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
def health_check():
    return {"status": "Atlas Core online", "version": "0.1.0"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(
        response=atlas.process_message(request.message)
    )
