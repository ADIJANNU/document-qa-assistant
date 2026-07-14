from document_loader import load_documnets
from retriever import find_relevant_document

docs = load_documnets("documents")
result = find_relevant_document("What is python", docs)
print(result)
