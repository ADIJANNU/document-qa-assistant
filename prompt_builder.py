def build_prompt(content, question):
  return f"""Answer the question using ONLY the information in the text below.
  If the answer is not contained in the text, respond exactly with: "I don't know based on the provided documents."

  Text:
  {content}

  Question:
  {question}
  """
# prompt = build_prompt("Erling  Haaland is a Norwegian professional footballer who plays as a striker for Premier League club Manchester City and the Norway national team.", "Who is Erling Haaland")

# print(prompt)
