from fastapi import APIRouter
from app.services.translation_service import translate_text


router=APIRouter()


@router.post("/translate/")

async def translate(input_text: str):
    translated_text=translate_text(input_text)
    return {"translated_text": translated_text}