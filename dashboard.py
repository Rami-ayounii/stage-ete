import streamlit as st
import PyPDF2
from src.agents.hr_input_agent import HrInputAgent
from src.agents.search_agent import SearchAgent
from src.agents.resume_parser_agent import ResumeParserAgent
from src.agents.ranking_agent import RankingAgent
from src.tools.internal_tool import InternalTool

st.title("HR Resume Ranking System")

# Step 1: Upload Job Description
st.header("1. Job Description")
job_title = st.text_input("Job Title", "Software Engineer")
required_skills = st.text_area("Required Skills (comma-separated)", "Python, APIs, SQL")
job_description = {
    "title": job_title,
    "required_skills": [skill.strip() for skill in required_skills.split(",") if skill.strip()]
}

# Step 2: Upload Resumes (PDFs)
st.header("2. Upload Resumes (PDFs)")
uploaded_files = st.file_uploader("Upload multiple PDF resumes", type=["pdf"], accept_multiple_files=True)

resumes = []
for uploaded_file in uploaded_files:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    content = ""
    for page in pdf_reader.pages:
        content += page.extract_text() or ""
    resumes.append({
        "name": f"Candidate {uploaded_file.name}",
        "email": f"{uploaded_file.name.split('.')[0]}@example.com",
        "phone": "N/A",
        "experience": [content],
        "skills": []  # Optionally, extract skills from content
    })

# Step 3: Parse, Rank, and Display Top Candidates
if st.button("Find Best Candidates"):
    hr_input_agent = HrInputAgent()
    for resume in resumes:
        hr_input_agent.collect_resume(resume)
    search_agent = SearchAgent(job_description)
    internal_tool = InternalTool()
    resume_parser_agent = ResumeParserAgent(internal_tool)
    ranking_agent = RankingAgent()

    all_resumes = hr_input_agent.get_submissions()
    filtered_resumes = search_agent.search_resumes(all_resumes)
    parsed_resumes = [resume_parser_agent.analyze_resume(resume) for resume in filtered_resumes]
    ranked_resumes = ranking_agent.rank_resumes(parsed_resumes, job_description)
    top_n = ranking_agent.get_top_n_resumes(ranked_resumes, n=5)

    st.header("Top Candidates")
    for idx, candidate in enumerate(top_n, 1):
        st.subheader(f"Rank #{idx}: {candidate.get('name')}")
        st.write(f"Email: {candidate.get('email')}")
        st.write(f"Skills: {candidate.get('skills')}")
        st.write(f"Experience: {candidate.get('experience')}")
        st.write(f"Match Score: {ranking_agent.calculate_relevance(candidate, job_description)}")
        st.markdown("---")