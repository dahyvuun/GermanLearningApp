from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "Helsinki-NLP/opus-mt-en-de"
tokenizer=AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

translator = pipeline("translation_en_to_de", model=model_name, tokenizer = tokenizer)
