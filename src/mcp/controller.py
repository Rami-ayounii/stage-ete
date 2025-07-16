class MCPController:
    def __init__(self, hr_input_agent=None, search_agent=None, resume_parser_agent=None, ranking_agent=None, email_agent=None):
        self.hr_input_agent = hr_input_agent
        self.search_agent = search_agent
        self.resume_parser_agent = resume_parser_agent
        self.ranking_agent = ranking_agent
        self.email_agent = email_agent

    def run_workflow(self, data):
        for step in self.steps:
            data = step(data)
        return data

    def incorporate_feedback(self, feedback):
        # Logic to adjust workflow or data based on feedback
        pass

