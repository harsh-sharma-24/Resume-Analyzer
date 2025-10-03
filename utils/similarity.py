from sklearn.metrics.pairwise import cosine_similarity
import os
from openai import OpenAI
import numpy as np
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

model = OpenAI(
    base_url = endpoint,
    api_key = api_key,
)


def compute_similarity(resume_text: str, jd_text: str) -> float:
    """
    Compute cosine similarity between resume and JD text.
    Returns a score between 0 and 1.
    """
    if not resume_text.strip() or not jd_text.strip():
        return 0.0
    
    resume_emb = model.embeddings.create(
        input = resume_text,
        model = deployment_name
    )
        
    jd_emb = model.embeddings.create(
        input = jd_text,
        model = deployment_name
    )
    resume_emb = np.array(resume_emb.data[0].embedding, dtype="float32").reshape(1, -1)
    jd_emb = np.array(jd_emb.data[0].embedding, dtype="float32").reshape(1, -1)
    score = cosine_similarity(resume_emb, jd_emb)[0][0]
    return round(float(score), 4)


if __name__ == "__main__":
    resume_text = input("Enter resume text: ")
    jd_text = input("Enter job description: ")
    similarity = compute_similarity(resume_text, jd_text)
    print(f"Similarity: {similarity:.4f}")  

