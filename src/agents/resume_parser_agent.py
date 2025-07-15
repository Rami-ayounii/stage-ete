class ResumeParserAgent:
    def __init__(self, internal_tool):
        self.internal_tool = internal_tool

    def parse_resume(self, resume):
        parsed_data = self.internal_tool.parse(resume)
        return parsed_data

    def extract_relevant_info(self, parsed_data):
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