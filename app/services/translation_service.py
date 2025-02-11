from app.nlp_pipeline.pipeline import translate_to_german

def translate_text(text:str):
    return translate_to_german(text, max_length=100)[0]["translation_text"]