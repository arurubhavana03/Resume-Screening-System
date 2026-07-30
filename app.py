import os
from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

UPLOAD_FOLDER = "upload"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "resume" not in request.files:
        return "No file part", 400
    
    file = request.files["resume"]
    if file.filename == "":
        return "No selected file", 400

    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)
        
        # Extract text from uploaded PDF
        extracted_text = extract_text(filepath)
        
        # Pass extracted text or results to template
        return render_template("result.html", text=extracted_text)

if __name__ == "__main__":
    app.run(debug=True)