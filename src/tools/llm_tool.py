import openai  # or your preferred LLM client

def semantic_rank(resume_text, job_description, api_key):
    openai.api_key = api_key
    prompt = f"""You are an expert HR recruiter. Given the following candidate resume and job description, do the following:
1. Analyze the candidate's fit for the job based on skills, experience, and education.
2. Return a JSON object with:
   - match_score: a number between 0 and 1 representing the overall fit,
   - matched_skills: a list of skills from the resume that match the job requirements,
   - missing_skills: a list of required skills not found in the resume,
   - explanation: a brief explanation of the score and reasoning.
Resume:
{resume_text}

Job Description:
{job_description}
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or your chosen model
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def parse_resume_with_llm(resume_text, api_key):
    openai.api_key = api_key
    prompt = f"""Extract the following fields from this resume: name, email, phone, skills, experience, education.
Resume:
{resume_text}
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']