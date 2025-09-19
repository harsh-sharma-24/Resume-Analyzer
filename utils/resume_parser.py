# utils/resume_parser.py

import re
import json
import PyPDF2
import spacy
from pathlib import Path

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
SKILLS_JSON = BASE_DIR / "data" / "skills_list.json"

# Load skills from JSON
with open(SKILLS_JSON, "r") as f:
    SKILLS_KEYWORDS = json.load(f)  

EDUCATION_KEYWORDS = [
    'B.Tech', 'BE', 'M.Tech', 'MBA', 'BSc', 'MSc', 'BCA', 'MCA', 'PhD'
]

def extract_text_from_pdf(pdf_path):
    """
    Extract text from PDF and clean it
    """
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    # Clean extra spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def parse_resume_text(resume_text):
    """
    Parse resume text and return structured info
    """
    resume_info = {}

    # Clean text
    resume_text = re.sub(r'\s+', ' ', resume_text).strip()
    resume_info['clean_text'] = resume_text

    # Extract skills
    resume_info['skills'] = [skill for skill in SKILLS_KEYWORDS if skill.lower() in resume_text.lower()]

    # Extract experience (years)
    exp_match = re.search(r"(\d+\+?\s*years?)", resume_text, re.IGNORECASE)
    resume_info['experience'] = exp_match.group(1) if exp_match else None

    # Extract education
    resume_info['education'] = [edu for edu in EDUCATION_KEYWORDS if edu.lower() in resume_text.lower()]

    # Extract current or target role 
    doc = nlp(resume_text)
    roles = []
    for chunk in doc.noun_chunks:
        text_chunk = chunk.text.strip()
        if any(keyword.lower() in text_chunk.lower() for keyword in ['engineer', 'developer', 'scientist', 'analyst', 'manager', 'consultant']):
            roles.append(text_chunk)
    resume_info['role'] = roles[0] if roles else None

    return resume_info

def parse_resume_pdf(pdf_path):
    """
    Parse resume from PDF file
    """
    text = extract_text_from_pdf(pdf_path)
    return parse_resume_text(text)
