from fastapi import APIRouter
from app.services.chatbot_service import process_user_input
from pydantic import BaseModel
router = APIRouter()

class ChatRequest(BaseModel):
    user_input: str

@router.post("/chat/")
def chat(request: ChatRequest):
    response=process_user_input(request.user_input)
    return {"response": response}