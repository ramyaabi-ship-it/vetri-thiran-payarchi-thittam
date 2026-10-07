from app.services.gemini_service import get_gemini_service

def answer_question(question: str) -> str:
    return get_gemini_service().generate(
        f"""You are EduGenie, a friendly educational assistant.
Answer the student's question accurately and concisely.
Use simple language, short sections, and an example when useful.
If the question is ambiguous, state the assumption you made.
Question: {question}"""
    )

def explain_topic(text: str) -> str:
    return get_gemini_service().generate(
        f"""Explain the following topic to a beginner.
Start with a one-sentence definition, then explain it in simple steps,
and finish with a small real-world example.
Topic: {text}"""
    )

def summarize(text: str) -> str:
    return get_gemini_service().generate(
        f"""Summarize the following educational text for quick revision.
Keep the important facts, definitions, relationships and conclusions.
Use concise bullet points and simple wording.
Text:
{text}"""
    )

def create_quiz(text: str):
    raw = get_gemini_service().generate(
        f"""Create exactly 3 multiple-choice questions from the educational
content below. Each question must have exactly 4 options, exactly one
correct answer, and a short explanation.
Return JSON only in this schema:
{{"questions":[{{"question":"...","options":["...","...","...","..."],
"correct_answer":"...","explanation":"..."}}]}}
Content:
{text}""",
        json_mode=True,
    )
    data = get_gemini_service().clean_json(raw)
    if not isinstance(data, dict) or not isinstance(data.get("questions"), list):
        raise ValueError("Invalid quiz structure returned by Gemini.")
    if len(data["questions"]) != 3:
        raise ValueError("Gemini did not return exactly 3 questions.")
    for q in data["questions"]:
        if len(q.get("options", [])) != 4:
            raise ValueError("Each quiz question must contain 4 options.")
    return data

def learning_path(topic: str, level: str):
    return get_gemini_service().generate(
        f"""Create a structured learning path for: {topic}
Learner level: {level}
Include:
1. Prerequisites
2. Beginner to advanced stages
3. Key concepts at each stage
4. Suggested practice activities
5. Recommended resource types (videos, documentation, books or articles)
6. A realistic weekly progression
Keep it actionable and concise."""
    )
