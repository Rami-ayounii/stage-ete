from agents.hr_input_agent import HrInputAgent
from agents.search_agent import SearchAgent
from agents.resume_parser_agent import ResumeParserAgent
from agents.ranking_agent import RankingAgent
from agents.email_agent import EmailAgent
from mcp.controller import MCPController

def main():
    hr_input_agent = HrInputAgent()
    search_agent = SearchAgent()
    resume_parser_agent = ResumeParserAgent()
    ranking_agent = RankingAgent()
    email_agent = EmailAgent()

    mcp_controller = MCPController(
        hr_input_agent=hr_input_agent,
        search_agent=search_agent,
        resume_parser_agent=resume_parser_agent,
        ranking_agent=ranking_agent,
        email_agent=email_agent
    )

    mcp_controller.start_workflow()

if __name__ == "__main__":
    main()