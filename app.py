import os
from flask import Flask,request,render_template
from utils.analyzer import analyze_resume

app = Flask(__name__)

@app.route("/" , methods = ["GET","POST"])
def index():
    result = None
    if request.method == "POST":

        resume = request.files["resume"]
        jd = request.files["jd"]
        result = analyze_resume(resume,jd)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)