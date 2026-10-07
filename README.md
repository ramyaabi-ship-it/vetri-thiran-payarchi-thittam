# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a FastAPI + HTML/CSS/JavaScript educational assistant based on the supplied project documentation. It provides Q&A, topic explanations, summaries, 3-question MCQ quizzes, and personalized learning paths.

## Requirements
- Python 3.10+
- A Gemini API key
- VS Code recommended

## Setup

### Windows
```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

Open `.env` and set `GEMINI_API_KEY`.

### macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set `GEMINI_API_KEY` in `.env`.

## Run
```bash
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000

API documentation is available at:
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Test
```bash
pytest
```

Manual tests:
1. Ask: `What is photosynthesis?`
2. Explain: `Pythagorean theorem`
3. Summarize a paragraph about databases.
4. Generate a quiz from a short passage.
5. Learning path: `SQL`, level `beginner`.

## Project structure
```text
EduGenie/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── schemas/models.py
│   └── services/
│       ├── gemini_service.py
│       └── education.py
├── static/style.css
├── templates/index.html
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Design note
The supplied document names Gemini 1.5 Pro and a local LaMini-Flan-T5 explanation module. This implementation uses the current Google GenAI Python SDK and a configurable Gemini model for all five educational functions, which keeps the application simpler and avoids an unnecessary local model dependency. The model can be changed through `GEMINI_MODEL`.
