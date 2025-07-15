class MCPController:
    def __init__(self, hr_input_agent, search_agent, resume_parser_agent, ranking_agent, email_agent):
        self.hr_input_agent = hr_input_agent
        self.search_agent = search_agent
        self.resume_parser_agent = resume_parser_agent
        self.ranking_agent = ranking_agent
        self.email_agent = email_agent

    def run_workflow(self):
        # Step 1: Collect HR input
        resumes = self.hr_input_agent.collect_resumes()

        # Step 2: Search and filter resumes
        filtered_resumes = self.search_agent.filter_resumes(resumes)

        # Step 3: Parse resumes to extract relevant information
        parsed_resumes = self.resume_parser_agent.parse_resumes(filtered_resumes)

        # Step 4: Rank the parsed resumes based on relevance
        ranked_resumes = self.ranking_agent.rank_resumes(parsed_resumes)

        # Step 5: Send results via email
        self.email_agent.send_results(ranked_resumes)