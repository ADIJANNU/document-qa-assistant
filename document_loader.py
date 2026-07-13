import os

def load_documnets(folder):
  documents = {}

  for filename in os.listdir(folder):
    if filename.endswith(".txt"):
      filepath = os.path.join(folder, filename)
      with open(filepath, "r", encoding="utf-8") as f:
        documents[filename] = f.read()
  return documents

docs = load_documnets("documents")
for filename in docs:
  print(filename)


