from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import run_agent

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Keep conversation history per demo session (simple, fine for now)
conversation = []

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    conversation.append({"role": "user", "content": req.message})
    reply = run_agent(conversation)
    conversation.append({"role": "assistant", "content": reply})
    return {"reply": reply}