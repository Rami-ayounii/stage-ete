from src.tools.llm_tool import parse_resume_with_llm
from src.config import config

class ResumeParserAgent:
    def __init__(self, internal_tool, use_llm=False):
        self.internal_tool = internal_tool
        self.use_llm = use_llm
        self.llm_api_key = config.get_llm_api_key()  # Add this method to your config

    def parse_resume(self, resume):
        if self.use_llm:
            # Use LLM for parsing
            llm_result = parse_resume_with_llm(resume, self.llm_api_key)
            # Optionally, parse the LLM's JSON/text output into a dict here
            # For now, just return the raw LLM output
            return llm_result
        else:
            # Use internal tool
            return self.internal_tool.parse(resume)

    def extract_relevant_info(self, parsed_data):
        # If LLM returns a string, parse it to dict (implement as needed)
        if isinstance(parsed_data, str):
            # Try to parse as dict if possible (e.g., using json.loads)
            import json
            try:
                return json.loads(parsed_data)
            except Exception:
                return {"llm_raw": parsed_data}
        # Otherwise, assume dict
        relevant_info = {
            "name": parsed_data.get("name"),
            "email": parsed_data.get("email"),
            "skills": parsed_data.get("skills"),
            "experience": parsed_data.get("experience"),
            "education": parsed_data.get("education"),
        }
        return relevant_info

    def analyze_resume(self, resume):
        parsed_data = self.parse_resume(resume)
        return self.extract_relevant_info(parsed_data)