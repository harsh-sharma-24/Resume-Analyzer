import os
from flask import Flask,request,render_template
from services.analyzer import analyze_resume

app = Flask(__name__)
upload_folder = "uploads"
os.makedirs(upload_folder,exist_ok=True)

@app.route("/" , methods = ["GET","POST"])
def index():
    result = None

    if request.method == "POST":
        resume = request.files["resume"]
        jd = request.files["jd"]
        resume_path = os.path.join(upload_folder,resume.filename)
        jd_path = os.path.join(upload_folder,jd.filename)
        resume.save(resume_path)
        jd.save(jd_path)
        result = analyze_resume(resume_path,jd_path)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)