from utils.resume_parser import parse_resume_pdf
from utils.jd_parser import parse_jd_pdf
from utils.similarity import compute_similarity
from utils.skill_gap import analyze_skill_gap

def main():
    # Take inputs
    resume_path = input(r"Enter path to Resume PDF: ").strip().strip('"')
    jd_path = input(r"Enter path to JD PDF: ").strip().strip('"')

    # Parse resume and JD
    resume_info = parse_resume_pdf(resume_path)
    jd_info = parse_jd_pdf(jd_path)

    # Get full cleaned text
    resume_text = " ".join(
        [str(v) for v in resume_info.values() if v]
    )
    jd_text = " ".join(
        [str(v) for v in jd_info.values() if v]
    )

    # Compute similarity
    score = compute_similarity(resume_text, jd_text)
    min_score = 0.25
    max_score = 0.65
    # Convert to %
    percentage = ((score - min_score) / (max_score - min_score)) * 100

    # Use Min Max Scaler to get the best results  
    print("\n📄 Resume Parsed:", resume_info)
    print("\n📄 JD Parsed:", jd_info)
    print(f"\n Orignal Score : {score}" )
    print(f"\n✅ Resume ↔ JD Match Score: {percentage}%")
# AFTER (Correct)
    skill_gap = analyze_skill_gap(resume_info, jd_info)
    print("\n=== Skill Gap Analysis ===")
    print("Resume Skills:", skill_gap["resume_skills"])
    print("JD Skills:", skill_gap["jd_skills"])
    print("Matched Skills:", skill_gap["matched_skills"])
    print("Missing Skills:", skill_gap["missing_skills"])
    print("Extra Skills (not in JD):", skill_gap["extra_skills"])
if __name__ == "__main__":
    while True:
        main()
