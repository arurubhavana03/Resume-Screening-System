# AI Resume Screening & ATS System

An intelligent web application that evaluates candidate resumes against job descriptions using Natural Language Processing (NLP) to compute match percentages and highlight missing skills.

---

## Features
- **PDF Text Extraction:** Parses text from uploaded resume files.
- **NLP Scoring Engine:** Uses TF-IDF Vectorization and Cosine Similarity (`scikit-learn`) to calculate semantic match scores.
- **Skill Gap Analysis:** Extracts crucial missing keywords from the job description to help candidates optimize their resumes.
- **Modern Responsive UI:** Built with Flask and Bootstrap 5.

---

## Tech Stack
- **Backend:** Python, Flask, PyPDF2
- **Machine Learning / NLP:** scikit-learn (TF-IDF, Cosine Similarity)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Deployment:** Render

---

## Team Contributions
- **Bhavana (Team Lead):** Core Flask Architecture, PyPDF2 Integration, Render Deployment
- **drakshayani 1:** NLP & Cosine Similarity Scoring Module (`ats.py`)
- **salama banu 2:** Frontend & UI/UX Design (`index.html`, `result.html`)
- **gadhipakula reshmaa3:** Keyword & Missing Skill Analytics Module (`extract_missing_skills`)