import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:3b"

def answer_question(question: str, context_chunks: list) -> str:
    context = "\n\n".join(context_chunks)

    prompt = f"""
Answer the question using ONLY the context below.
If the answer is not in the context, say:
"The document does not contain this information."

Context:
{context}

Question:
{question}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "options": {"temperature": 0.2}
        },
        timeout=120
    )

    response.raise_for_status()
    return response.json()["message"]["content"]
