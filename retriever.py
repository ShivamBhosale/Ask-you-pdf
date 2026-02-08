from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_retriever(chunks: list):
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(chunks)
    return vectorizer, matrix

def retrieve_chunks(question: str, chunks: list, vectorizer, matrix, top_k=3):
    query_vec = vectorizer.transform([question])
    scores = cosine_similarity(query_vec, matrix)[0]

    top_indices = scores.argsort()[-top_k:][::-1]
    return [chunks[i] for i in top_indices]
