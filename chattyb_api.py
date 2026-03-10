from fastapi import FastAPI
from pydantic import BaseModel
from chattyb1000 import ChattyB1000

engine = ChattyB1000()

app = FastAPI(
    title="ChattyB1000 Tone Engine API",
    description="API that transforms neutral text into ChattyB1000 style.",
    version="1.0.0"
)

class ChattyBRequest(BaseModel):
    user_text: str
    draft_reply: str

@app.post("/chattyb/respond")
def chattyb_respond(req: ChattyBRequest):
    transformed = engine.respond(req.user_text, req.draft_reply)
    return {"chattyb_reply": transformed}
