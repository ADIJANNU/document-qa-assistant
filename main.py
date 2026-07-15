from document_loader import load_documnets
from retriever import find_relevant_document
from prompt_builder import build_prompt
from ai_client import get_ai_response

docs = load_documnets("documents")

question = "How do I add something to the end of a list, and how do I go through each item?"
best_doc = find_relevant_document(question, docs)
print(f"Using document: {best_doc}")

if best_doc is None:
  print(("Sorry, I couldn't find anything relevant in your documents."))
else:
  content = docs[best_doc]
  prompt = build_prompt(content, question)
  answer = get_ai_response(prompt)
  print(answer)