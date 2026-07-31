"""Atlas API chat endpoint."""

from fastapi import FastAPI
from pydantic import BaseModel

from bootstrap import atlas, runtime


app = FastAPI(title="Atlas Core", version="0.1.0")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
def root():
    return runtime.get_status()


@app.get("/health")
def health():
    return runtime.get_status()


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(
        response=atlas.process_message(request.message)
    )
