import re

def extract_missing_skills(resume_text, job_description):
    """
    Finds keywords present in the job description that are missing from the resume.
    """
    if not resume_text or not job_description:
        return []

    # Clean and extract individual words (alphanumeric only, lowercase)
    jd_words = set(re.findall(r'\b[a-zA-Z]{3,}\b', job_description.lower()))
    resume_words = set(re.findall(r'\b[a-zA-Z]{3,}\b', resume_text.lower()))

    # Ignore common non-technical stopwords
    common_stopwords = {
        'and', 'the', 'for', 'with', 'you', 'this', 'that', 'from', 'have', 'are', 
        'will', 'our', 'team', 'work', 'ability', 'experience', 'knowledge', 'must'
    }

    # Filter out stopwords from job description words
    important_jd_words = jd_words - common_stopwords

    # Find missing words
    missing_words = important_jd_words - resume_words

    # Return top 10 missing words sorted
    return sorted(list(missing_words))[:10]