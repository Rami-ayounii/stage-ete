def parse_resume(resume_text):
    # Function to parse the resume text and extract relevant information
    parsed_data = {
        "name": extract_name(resume_text),
        "email": extract_email(resume_text),
        "phone": extract_phone(resume_text),
        "skills": extract_skills(resume_text),
        "experience": extract_experience(resume_text),
        "education": extract_education(resume_text),
    }
    return parsed_data

def extract_name(resume_text):
    # Logic to extract name from the resume text
    pass

def extract_email(resume_text):
    # Logic to extract email from the resume text
    pass

def extract_phone(resume_text):
    # Logic to extract phone number from the resume text
    pass

def extract_skills(resume_text):
    # Logic to extract skills from the resume text
    pass

def extract_experience(resume_text):
    # Logic to extract work experience from the resume text
    pass

def extract_education(resume_text):
    # Logic to extract education details from the resume text
    pass

def analyze_resume(parsed_resume, job_description):
    # Function to analyze the parsed resume against the job description
    analysis_results = {
        "match_percentage": calculate_match_percentage(parsed_resume, job_description),
        "matched_skills": find_matched_skills(parsed_resume, job_description),
        "unmatched_skills": find_unmatched_skills(parsed_resume, job_description),
    }
    return analysis_results

def calculate_match_percentage(parsed_resume, job_description):
    # Logic to calculate match percentage
    pass

def find_matched_skills(parsed_resume, job_description):
    # Logic to find matched skills
    pass

def find_unmatched_skills(parsed_resume, job_description):
    # Logic to find unmatched skills
    pass