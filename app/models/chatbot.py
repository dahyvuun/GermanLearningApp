from transformers import AutoModelForCausalLM, AutoTokenizer
from app.nlp_pipeline import pipeline

model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

chatbot=pipeline("text-generation", model=model, tokenizer=tokenizer)
