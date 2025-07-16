import re

class InternalTool:
    def parse(self, resume_text):
        if isinstance(resume_text, dict):
            return resume_text  # Already parsed, just return
        if not isinstance(resume_text, str):
            raise TypeError("Expected resume_text to be a string, got {}".format(type(resume_text)))
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
    # Simple heuristic: first line or line with capitalized words
    lines = resume_text.split('\n')
    for line in lines:
        if line.strip() and line.strip()[0].isupper() and len(line.split()) <= 4:
            return line.strip()
    return "Unknown"

def extract_email(resume_text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', resume_text)
    return match.group(0) if match else "Unknown"

def extract_phone(resume_text):
    match = re.search(r'(\+?\d{1,3}[\s-]?)?(\(?\d{2,4}\)?[\s-]?)?\d{3,4}[\s-]?\d{4}', resume_text)
    return match.group(0) if match else "Unknown"

def extract_skills(resume_text):
    # Example: look for a "Skills" section
    skills = []
    skills_section = re.search(r'Skills\s*[:\-]?\s*(.*)', resume_text, re.IGNORECASE)
    if skills_section:
        skills = [skill.strip() for skill in re.split(r',|;', skills_section.group(1))]
    return skills

def extract_experience(resume_text):
    # Example: look for lines containing 'Experience' or job titles
    experience = []
    for line in resume_text.split('\n'):
        if 'experience' in line.lower() or 'engineer' in line.lower() or 'developer' in line.lower():
            experience.append(line.strip())
    return experience

def extract_education(resume_text):
    # Example: look for lines containing 'University', 'Bachelor', 'Master', etc.
    education = []
    for line in resume_text.split('\n'):
        if any(keyword in line.lower() for keyword in ['university', 'bachelor', 'master', 'phd', 'degree']):
            education.append(line.strip())
    return education

def analyze_resume(parsed_resume, job_description):
    analysis_results = {
        "match_percentage": calculate_match_percentage(parsed_resume, job_description),
        "matched_skills": find_matched_skills(parsed_resume, job_description),
        "unmatched_skills": find_unmatched_skills(parsed_resume, job_description),
    }
    return analysis_results

def calculate_match_percentage(parsed_resume, job_description):
    matched = find_matched_skills(parsed_resume, job_description)
    required = job_description.get("required_skills", [])
    if not required:
        return 0
    return int(100 * len(matched) / len(required))

def find_matched_skills(parsed_resume, job_description):
    resume_skills = set([s.lower() for s in parsed_resume.get("skills", [])])
    required_skills = set([s.lower() for s in job_description.get("required_skills", [])])
    return list(resume_skills & required_skills)

def find_unmatched_skills(parsed_resume, job_description):
    resume_skills = set([s.lower() for s in parsed_resume.get("skills", [])])
    required_skills = set([s.lower() for s in job_description.get("required_skills", [])])
    return list(required_skills - resume_skills)

# Example usage:
internal_tool = InternalTool()
resume_text = """
John Doe
john.doe@example.com
(123) 456-7890
Skills: Python, Java, C++
Experience: Software Engineer at XYZ Corp
Education: Bachelor of Science in Computer Science
"""
job_description = {
    "required_skills": ["python", "java", "communication"],
}

parsed_resume = internal_tool.parse(resume_text)
analysis = analyze_resume(parsed_resume, job_description)

print("Parsed Resume:", parsed_resume)
print("Analysis:", analysis)

# Loop through multiple resumes
resumes = [resume_text, resume_text]  # Example: list of resume texts
for resume in resumes:
    # If resume is a string (raw text), this is correct:
    parsed = internal_tool.parse(resume)
    # If resume is already a dict, do NOT parse again!