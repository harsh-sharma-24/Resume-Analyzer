AI-Powered Resume Analyzer
📝 Overview
This project is a web-based Resume Analyzer that intelligently matches a candidate's resume with a job description (JD). The application accepts both documents in PDF format, performs a detailed analysis, and provides a similarity score to quantify the candidate's suitability for the role.

It leverages Natural Language Processing (NLP) for semantic text comparison and includes a pre-screening eligibility check based on core requirements like experience and education.

✨ Features
📄 PDF Upload: Simple web interface to upload both a resume and a job description PDF.

✅ Eligibility Check: Automatically pre-screens the candidate based on essential criteria like years of experience and required educational qualifications.

🧠 Weighted Similarity Score: Calculates a sophisticated match score by giving different weights to semantic text similarity and a direct comparison of skills.

📊 Skill Gap Analysis (Coming Soon): Provides a detailed breakdown of:

Matched Skills: Skills present in both the resume and the JD.

Missing Skills: Skills required by the JD that are not on the resume.

Extra Skills: Skills the candidate possesses that are not mentioned in the JD.

🌐 Web Interface: Built with Flask and styled with Tailwind CSS for a clean and modern user experience.

🛠️ How It Works
The application follows a simple yet powerful workflow:

File Upload: The user uploads the resume and JD PDFs via the Flask web server.

Parsing: A custom parsing module extracts clean text and structured data (like skills, experience, and education) from both PDFs.

Eligibility Check: The analyzer.py module performs an initial check. If the candidate doesn't meet the minimum requirements, the process stops, and the user is notified.

Similarity Calculation:

Text Similarity: An NLP model (e.g., using spaCy or Sentence Transformers) computes the semantic similarity between the core text of the resume and the JD.

Skill Similarity: The extracted skill lists are directly compared to find overlaps.

A weighted average of these two scores produces the final match percentage.

Display Results: The final score and eligibility status are rendered on the index.html template.

🚀 Setup and Installation
To run this project locally, follow these steps:

1. Clone the repository:

git clone (https://github.com/harsh-sharma-24/Resume-Analyzer)
cd resume-analyzer

2. Create and activate a virtual environment:

python -m venv venv
.\venv\Scripts\activate

3. Install dependencies:
Create a requirements.txt file with the following content:

flask
spacy
pypdf2

Then, install the requirements:

pip install -r requirements.txt

4. Download the spaCy language model:

python -m spacy download en_core_web_sm

5. Run the Flask application:

python app.py

The application will be available at http://127.0.0.1:5000 in your web browser.

Usage
Open your web browser and navigate to http://127.0.0.1:5000.

Click the "Choose File" button to select a resume PDF.

Click the second "Choose File" button to select a job description PDF.

Click the "Analyze Match" button.

The analysis result, including the eligibility status and match score, will be displayed on the page.

📁 Project Structure
resume-analyzer/
│
├── app.py              # Main Flask application file
├── analyzer.py         # Core logic for analysis and scoring
│
├── utils/
│   ├── resume_parser.py  # Function to parse resumes
│   ├── jd_parser.py      # Function to parse job descriptions
│   ├── similarity.py     # Function to compute text similarity
│   └── skill_gap.py      # Function for skill analysis
│
├── templates/
│   └── index.html      # Frontend HTML template
│
├── uploads/            # Temporary storage for uploaded PDFs
│
├── requirements.txt    # Project dependencies
└── README.md           # This file
