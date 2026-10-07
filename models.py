from pydantic import BaseModel, Field
from typing import List

class TextRequest(BaseModel):
    text: str = Field(..., min_length=1)

class QARequest(BaseModel):
    question: str = Field(..., min_length=1)

class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    correct_answer: str
    explanation: str = ""

class QuizResponse(BaseModel):
    questions: List[QuizQuestion]

class LearningPathRequest(BaseModel):
    topic: str = Field(..., min_length=1)
    level: str = "beginner"
