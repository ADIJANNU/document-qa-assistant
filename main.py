from document_loader import load_documnets
from retriever import find_relevant_document
from prompt_builder import build_prompt
from ai_client import get_ai_response
from structured_output import clean_json_response, DocumentAnswer
import json
from pydantic import ValidationError

RED, GREEN, YELLOW, BLUE, CYAN, MAGENTA, WHITE, RESET = '\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[96m', '\033[95m', '\033[97m', '\033[0m' 

docs = load_documnets("documents")

question = "How do I add something to the end of a list?"
best_doc = find_relevant_document(question, docs)
print(f"Using document: {YELLOW}{best_doc}{RESET}")

if best_doc is None:
  print(("Sorry, I couldn't find anything relevant in your documents."))
else:
  content = docs[best_doc]
  prompt = build_prompt(content, question)
  print(f"{MAGENTA}Thinking... {RESET}")
  raw_answer = get_ai_response(prompt)
  cleaned = clean_json_response(raw_answer)

  try:
    data = json.loads(cleaned)
    structured_answer = DocumentAnswer(**data)
    print(structured_answer)
  except (json.JSONDecodeError, ValidationError) as e:
    print(f"Failed to parse AI response: {e}")
