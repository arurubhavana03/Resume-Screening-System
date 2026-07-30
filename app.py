import os
from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

# Configure folder for uploads
UPLOAD_FOLDER = "upload"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure the upload directory exists dynamically
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def extract_text(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text


def calculate_match(resume_text, job_description):
    if not job_description or not resume_text:
        return 0

    resume_words = set(resume_text.lower().split())
    jd_words = set(job_description.lower().split())

    if not jd_words:
        return 0

    matching_words = resume_words.intersection(jd_words)
    score = int((len(matching_words) / len(jd_words)) * 100)
    return min(score * 2, 100)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    # Safely handle missing form inputs
    if "resume" not in request.files:
        return "No file part in the request", 400

    file = request.files["resume"]
    job_description = request.form.get("job_description", "")

    if file.filename == "":
        return "No file selected", 400

    if file:
        # Save file safely to the upload folder
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # Process the resume
        resume_text = extract_text(filepath)
        score = calculate_match(resume_text, job_description)

        # Clean up uploaded file after processing
        if os.path.exists(filepath):
            os.remove(filepath)

        return render_template(
            "result.html", score=score, resume_text=resume_text
        )

    return "An error occurred during file upload", 500


if __name__ == "__main__":
    app.run(debug=True)