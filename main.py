from fastapi import FastAPI
from app.routes.chatbot import router as chatbot_router

app=FastAPI()
app.include_router(chatbot_router)

@app.get("/")
def home():
    return {"message" : "Welcome to the German Learning AI Chatbot"}