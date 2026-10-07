from pathlib import Path
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.schemas.models import (
    TextRequest, QARequest, QuizResponse, LearningPathRequest
)
from app.services.education import (
    answer_question, explain_topic, summarize, create_quiz, learning_path
)

BASE_DIR = Path(__file__).resolve().parent.parent
app = FastAPI(title="EduGenie API", version="1.0.0")

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
async def health():
    return {"status": "ok", "service": "EduGenie"}

@app.post("/qa")
async def qa(payload: QARequest):
    try:
        return {"answer": answer_question(payload.question)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/explain")
async def explain(payload: TextRequest):
    try:
        return {"explanation": explain_topic(payload.text)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/summarize")
async def summarize_text(payload: TextRequest):
    try:
        return {"summary": summarize(payload.text)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/quiz", response_model=QuizResponse)
async def quiz(payload: TextRequest):
    try:
        return create_quiz(payload.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/learn/recommendations")
async def recommendations(payload: LearningPathRequest):
    try:
        return {"learning_path": learning_path(payload.topic, payload.level)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
