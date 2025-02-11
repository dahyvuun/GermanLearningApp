from fastapi import FastAPI
from app.routes import chatbot, translation, grammar

app = FastAPI()


app.include_router(chatbot.router, prefix = "/api")
app.include_router(translation.router, prefix = "/api")
app.include_router(grammar.router, prefix="/api")


@app.get("/")
def home():
    return {"message": "Welcome to the German Learning AI Chatbot"}


app.include_router(grammar.router)