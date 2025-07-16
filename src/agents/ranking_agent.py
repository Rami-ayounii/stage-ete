from src.tools.llm_tool import semantic_rank
from src.config import config

class RankingAgent:
    def __init__(self, use_llm=False):
        self.use_llm = use_llm
        self.llm_api_key = config.get_llm_api_key()

    def rank_resumes(self, parsed_resumes, job_description):
        ranked = []
        for resume in parsed_resumes:
            if self.use_llm:
                score_and_explanation = semantic_rank(str(resume), job_description, self.llm_api_key)
                ranked.append({"resume": resume, "llm_score": score_and_explanation})
            else:
                score = self.calculate_relevance(resume, job_description)
                ranked.append({"resume": resume, "score": score})
        # Sort by score (if using LLM, you may need to extract the score from the LLM output)
        return sorted(ranked, key=lambda x: x.get("score", 0), reverse=True)

    def calculate_relevance(self, resume, job_description):
        # Your existing logic
        resume_skills = set([s.lower() for s in resume.get("skills", [])])
        required_skills = set([s.lower() for s in job_description.get("required_skills", [])])
        if not required_skills:
            return 0
        return int(100 * len(resume_skills & required_skills) / len(required_skills))

    def get_top_n_resumes(self, ranked_resumes, n=5):
        return ranked_resumes[:n]