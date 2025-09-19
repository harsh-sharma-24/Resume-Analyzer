from utils.resume_parser import parse_resume_pdf
from utils.jd_parser import parse_jd_pdf
from utils.similarity import compute_similarity
from utils.skill_gap import analyze_skill_gap

def analyze_resume(resume_path,jd_path):
    resume = parse_resume_pdf(resume_path)
    jd = parse_jd_pdf(jd_path)
    eligible = True
    resume_exp = resume.get('experience')
    jd_exp = jd.get('experience')

    if isinstance(resume_exp, (int, float)) and isinstance(jd_exp, (int, float)):
        if resume_exp < jd_exp:
            eligible = False

    if(resume.get('education') and jd.get('education')):
        if not any(degree in resume['education'] for degree in jd['education']):
            eligible = False
    similarity = 0
    skills = {}

    if eligible and resume.get("clean_text") and jd.get("clean_text") :
        text_analysis = compute_similarity(resume['clean_text'], jd['clean_text'])
        skill_analysis = compute_similarity(" ".join(resume['skills']), " ".join(jd['skills']))
        similarity = (text_analysis*0.6) + (skill_analysis*0.4)
        print(similarity)
        skills = analyze_skill_gap(resume,jd)
        min_score = 0.25
        max_score = 0.60
        # Convert to %
        similarity = ((similarity - min_score) / (max_score - min_score))
        if(similarity > 1):
            similarity = 1
    print(f"eligible {eligible}")
    print(f"similarity_score: {round(similarity * 100, 2) if eligible else 0}")
    print(f"skills : {skills if eligible else {}}")
    return {
    "eligible": eligible,
    "similarity_score": round(similarity * 100, 2) if eligible else 0,
    "skills" : skills if eligible else {}
    }

