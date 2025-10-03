
def analyze_skill_gap(resume_data, jd_data):
    """
    Compare resume skills with JD skills.
    Both resume_data and jd_data should be dicts with a 'skills' key (list of skills).
    """

    resume_skills = set([skill.lower() for skill in resume_data.get("skills", [])])
    jd_skills = set([skill.lower() for skill in jd_data.get("skills", [])])

    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills - resume_skills
    extra_skills = resume_skills - jd_skills  # skills candidate has but not in JD

    return {
        "resume_skills": list(resume_skills),
        "jd_skills": list(jd_skills),
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "extra_skills": list(extra_skills),
    }
