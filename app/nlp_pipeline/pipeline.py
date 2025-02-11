from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer, AutoModelForCausalLM
from langdetect import detect

# 모델 설정
grammar_model_name = "t5-small"
grammar_tokenizer = AutoTokenizer.from_pretrained(grammar_model_name)
grammar_corrector = pipeline("text2text-generation", model=grammar_model_name, tokenizer=grammar_tokenizer)

trans_model_name = "Helsinki-NLP/opus-mt-en-de"
trans_tokenizer = AutoTokenizer.from_pretrained(trans_model_name)
trans_model = AutoModelForSeq2SeqLM.from_pretrained(trans_model_name)
translator = pipeline("translation_en_to_de", model=trans_model, tokenizer=trans_tokenizer)

chat_model_name = "distilgpt2"
chat_tokenizer = AutoTokenizer.from_pretrained(chat_model_name)
chat_model = AutoModelForCausalLM.from_pretrained(chat_model_name)
chatbot = pipeline("text-generation", model=chat_model, tokenizer=chat_tokenizer)

# 언어 감지 및 변환 처리
def process_text(text: str):
    """
    입력된 문장이 영어인지 독일어인지 감지하고:
    - 영어이면 독일어로 번역
    - 독일어이면 문법 교정
    """
    detected_lang = detect(text)

    if detected_lang == "en":
        corrected_text = grammar_corrector(f"Grammar Correction: {text}", max_length=100)[0]["generated_text"]
        translated_text = translator(corrected_text, max_length=100)[0]["translation_text"]
        return translated_text
    elif detected_lang == "de":
        return grammar_corrector(f"Grammar Correction: {text}", max_length=100)[0]["generated_text"]
    else:
        return "지원되지 않는 언어입니다. 영어 또는 독일어를 입력하세요."
