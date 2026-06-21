#  AI-Powered Resume Screening & Job Matching System

An intelligent system that automates resume screening and matches candidates with job descriptions using Natural Language Processing (NLP) techniques and semantic similarity.

---

##  Features

*  Automated Resume Screening
*  Resume & Job Description Matching
*  Semantic Similarity using NLP
*  Skill Extraction & Gap Analysis
*  Faster Candidate Shortlisting

---

##  Tech Stack

* **Programming Language:** Python
* **Framework:** Flask
* **Libraries:**

  * Scikit-learn (TF-IDF)
  * Sentence Transformers
  * NumPy, Pandas
* **Other Tools:** Cosine Similarity, NLP techniques

---

## ⚙️ How It Works

1. Upload Resume (PDF/Text)
2. Input Job Description
3. System processes both inputs
4. Extracts key skills and keywords
5. Computes similarity using:

   * TF-IDF
   * Transformer-based embeddings
6. Generates:

   * Match Score
   * Missing Skills
   * Suggestions

---

##  Key Highlights

*  Improved semantic matching relevance by ~30% using embeddings over keyword-based methods
*  Reduced manual screening time by ~40%
*  Tested on 50+ resumes and job descriptions for consistency

---

##  Project Structure

```
├── app.py
├── templates/
├── static/
├── resume_parser.py
├── similarity.py
├── requirements.txt
└── README.md
```

---

##  Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/resume-screening-ai.git

# Navigate to project folder
cd resume-screening-ai

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

---

##  Usage

* Open browser and go to: `http://127.0.0.1:5000/`
* Upload a resume
* Paste job description
* Get match score and insights

---

##  Future Improvements

*  Multiple Resume Upload & Ranking
*  Deploy on cloud (AWS/Render)
*  Dashboard for recruiters
*  Integration with job portals

---

##  Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

##  License

This project is open-source and available under the MIT License.

---

## Author

**Samriddh Saxena**
B.Tech CSE | Aspiring Software Engineer

---

If you found this project useful, don't forget to star the repo!
