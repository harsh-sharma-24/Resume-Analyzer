from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(resume_text: str, jd_text: str) -> float:
    """
    Compute cosine similarity between resume and JD text.
    Returns a score between 0 and 1.
    """
    if not resume_text.strip() or not jd_text.strip():
        return 0.0  # handle empty text

    resume_emb = model.encode([resume_text])
    jd_emb = model.encode([jd_text])

    score = cosine_similarity(resume_emb, jd_emb)[0][0]
    return round(float(score), 4)
