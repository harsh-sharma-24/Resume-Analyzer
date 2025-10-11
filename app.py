import os
import tempfile
from flask import Flask, request, render_template
from utils.analyzer import analyze_resume

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        resume = request.files["resume"]
        jd = request.files["jd"]

        tempdir = tempfile.gettempdir()

        resume_path = os.path.join(tempdir, resume.filename)
        jd_path = os.path.join(tempdir, jd.filename)

        resume.save(resume_path)
        jd.save(jd_path)

        result = analyze_resume(resume_path, jd_path)

        try:
            os.remove(resume_path)
            os.remove(jd_path)
        except Exception as e:
            print(f"Cleanup error: {e}")

    return render_template("index.html", result=result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
