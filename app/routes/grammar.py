from fastapi import APIRouter
from app.services.grammar_service import handle_text_processing
from pydantic import BaseModel

router = APIRouter()

class TextRequest(BaseModel):
    text:str


@router.post("/process/")

def process_input_text(request: TextRequest):
    result = handle_text_processing(request.text)
    return result