from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.services.deepseek import chat_with_deepseek

router = APIRouter()

@router.post("/chat")
async def chat(chat_request: ChatRequest):
    response = await chat_with_deepseek(chat_request.messages)
    return response
