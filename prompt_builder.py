def build_prompt(content, question):
  return f"""Answer the question using ONLY the information in the text below.
  Respond in this exact JSON format:
  {{"answer": "your answer here", "found_in_documents": true or false}}

  If the answer is not contained in the text, set found_in_documents to false and answer to "I don't know based on the provided documents."
  
  Text:
  {content}

  Question:
  {question}
  """

