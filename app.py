from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, render_template, request
from pdfminer.high_level import extract_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

model = SentenceTransformer('all-MiniLM-L6-v2')
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

SKILLS_DB = [
    "python", "java", "c++", "machine learning", "deep learning",
    "django", "flask", "react", "node.js", "sql", "mongodb",
    "html", "css", "javascript", "aws", "docker", "kubernetes"
]

def extract_skills(text):
    text = text.lower()
    found = []
    for skill in SKILLS_DB:
        if skill in text:
            found.append(skill)
    return list(set(found))

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        files = request.files.getlist("resume")
        job_desc = request.form["job_desc"]

        results = []

        for file in files:
            if file.filename == "":
                continue

            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            resume_text = extract_text(filepath)

            resume_skills = extract_skills(resume_text)
            jd_skills = extract_skills(job_desc)
            missing_skills = list(set(jd_skills) - set(resume_skills))

            emb1 = model.encode(resume_text)
            emb2 = model.encode(job_desc)

            similarity = cosine_similarity([emb1], [emb2])[0][0]

            score = round(similarity * 100, 2)

            suggestions = generate_suggestions(missing_skills)

            results.append({
                "filename": file.filename,
                "score": score,
                "resume_skills": resume_skills,
                "missing_skills": missing_skills,
                "suggestions": suggestions
            })

            results = sorted(results, key=lambda x: x["score"], reverse=True)

    return render_template("index.html", results=results)

def generate_suggestions(missing_skills):
    suggestions = []

    for skill in missing_skills:
        suggestions.append(f"Consider adding or improving your {skill} skills")

    if not missing_skills:
        suggestions.append("Your resume is well aligned with the job description")

    return suggestions

if __name__ == "__main__":
    app.run(debug=True)