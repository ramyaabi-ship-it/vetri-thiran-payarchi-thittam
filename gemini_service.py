from functools import lru_cache
import json
import re
from google import genai
from google.genai import types
from app.config import settings

class GeminiService:
    def __init__(self):
        if not settings.gemini_api_key:
            raise RuntimeError("GEMINI_API_KEY is not configured.")
        self.client = genai.Client(api_key=settings.gemini_api_key)
        self.model = settings.gemini_model

    def generate(self, prompt: str, json_mode: bool = False) -> str:
        config = None
        if json_mode:
            config = types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.3,
            )
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=config,
        )
        text = getattr(response, "text", None)
        if not text:
            raise RuntimeError("Gemini returned an empty response.")
        return text.strip()

    @staticmethod
    def clean_json(text: str):
        text = re.sub(r"^```(?:json)?\s*", "", text.strip(), flags=re.I)
        text = re.sub(r"\s*```$", "", text.strip())
        return json.loads(text)

@lru_cache
def get_gemini_service():
    return GeminiService()
