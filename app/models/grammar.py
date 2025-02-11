from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "t5-small"
tokenizer=AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

grammar_corrector=pipeline("text2text-generation", model=model_name)