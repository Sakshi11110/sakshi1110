from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()

class Message(BaseModel):
    question: str

# Mount the 'static' folder for HTML
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

def chatbot_reply(message: str) -> str:
    msg = message.lower()
    if "hello" in msg or "hi" in msg:
        return "Hey there! 👋 How can I help you today?"
    elif "name" in msg:
        return "I'm MiniBot 🤖, your little chatbot!"
    elif "python" in msg:
        return "Python is a powerful programming language. 🐍"
    elif "bye" in msg:
        return "Goodbye! See you again soon! 👋"
    else:
        return "Hmm... I'm still learning. Can you ask something else?"

@app.get("/", response_class=HTMLResponse)
async def serve_chat_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(data: Message):
    reply = chatbot_reply(data.question)
    return JSONResponse(content={
        "you_said": data.question,
        "chatbot_says": reply
    })
