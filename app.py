from ats import calculate_ats_score, extract_missing_skills
@app.route("/upload", methods=["POST"])
def upload_file():
    if "resume" not in request.files:
        return "No file part in the request", 400

    file = request.files["resume"]
    job_description = request.form.get("job_description", "")

    if file.filename == "":
        return "No file selected", 400

    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # Process text and calculations
        resume_text = extract_text(filepath)
        score = calculate_ats_score(resume_text, job_description)
        missing_skills = extract_missing_skills(resume_text, job_description)

        # Clean up saved file
        if os.path.exists(filepath):
            os.remove(filepath)

        return render_template(
            "result.html", 
            score=score, 
            resume_text=resume_text, 
            missing_skills=missing_skills
        )

    return "An error occurred during file upload", 500