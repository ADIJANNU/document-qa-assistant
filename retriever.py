def find_relevant_document(question, documents):
  question_words = set(question.lower().split())

  best_doc = None
  best_score = 0

  for filename, content in documents.items():
    document_words = set(content.lower().split())
    overlap = question_words & document_words
    score = len(overlap)

    if score > best_score:
      best_score = score
      best_doc = filename
      
  return best_doc