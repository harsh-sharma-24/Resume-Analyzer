# utils/jd_parser.py

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
    SKILLS_KEYWORDS = json.load(f)  # Should be a list of strings

# Education keywords (can also be moved to JSON later)
EDUCATION_KEYWORDS = [
    'B.Tech', 'BE', 'M.Tech', 'MBA', 'BSc', 'MSc', 'BCA', 'MCA', 'PhD'
]

def extract_text_from_pdf(pdf_path):
    """
    Extracts and cleans text from a PDF file.
    """
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    # Clean extra spaces and line breaks
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def parse_jd_text(jd_text):
    """
    Parses job description text and returns structured info.
    """
    jd_info = {}

    # Clean text
    jd_text = re.sub(r'\s+', ' ', jd_text).strip()
    jd_info['clean_text'] = jd_text

    # Extract role/title
    role_match = re.search(
        r"(?:looking for|require|hiring|position|role)\s*(?:a|an)?\s*([A-Za-z\s]+)",
        jd_text, re.IGNORECASE
    )
    jd_info['role'] = role_match.group(1).strip() if role_match else None

    # Extract experience
    exp_match = re.search(r"(\d+\+?\s*years?)", jd_text, re.IGNORECASE)
    jd_info['experience'] = exp_match.group(1) if exp_match else None

    # Extract location
    loc_match = re.search(r"Location[:\s]*(.*?)(?:Salary|$)", jd_text, re.IGNORECASE)
    jd_info['location'] = loc_match.group(1).strip() if loc_match else None

    # Extract salary
    salary_match = re.search(r"Salary[:\s]*(.*?)(?:\n|$)", jd_text, re.IGNORECASE)
    jd_info['salary'] = salary_match.group(1).strip() if salary_match else None

    # Extract responsibilities
    resp_match = re.search(
        r"(?:Responsibilities include|You will be responsible for|Tasks include)(.*?)(?:Location|Salary|$)",
        jd_text, re.IGNORECASE
    )
    jd_info['responsibilities'] = resp_match.group(1).strip() if resp_match else None

    # Extract skills from JSON list
    jd_info['skills'] = [skill for skill in SKILLS_KEYWORDS if skill.lower() in jd_text.lower()]

    # Extract education
    jd_info['education'] = [edu for edu in EDUCATION_KEYWORDS if edu.lower() in jd_text.lower()]

    return jd_info

def parse_jd_pdf(pdf_path):
    """
    Parses JD from a PDF file and returns structured info.
    """
    text = extract_text_from_pdf(pdf_path)
    return parse_jd_text(text)