import json
from pydantic import BaseModel, ValidationError

class DocumentAnswer(BaseModel):
  answer: str
  found_in_documents: bool

def clean_json_response(text):
  text = text.strip()
  if text.startswith("```"):
    text = text.split("```")[1]
    if text.startswith("json"):
      text = text[4:]
  return text.strip()

