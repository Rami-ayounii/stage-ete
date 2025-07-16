import streamlit as st
from src.agents.hr_input_agent import HrInputAgent
from src.agents.search_agent import SearchAgent
from src.agents.resume_parser_agent import ResumeParserAgent
from src.agents.ranking_agent import RankingAgent
from src.agents.email_agent import EmailAgent
from src.mcp.controller import MCPController
from src.tools.internal_tool import InternalTool
from src.config import config  # Assuming you have config.py with SMTP info

def main():
    hr_input_agent = HrInputAgent()
    job_description = {
        "title": "Software Engineer",
        "required_skills": ["Python", "APIs", "SQL"]
    }
    search_agent = SearchAgent(job_description)
    internal_tool = InternalTool()
    resume_parser_agent = ResumeParserAgent(internal_tool)
    ranking_agent = RankingAgent()

    # Get SMTP config from your config module or environment variables
    smtp_server = config.get_smtp_server()
    smtp_port = config.get_smtp_port()
    smtp_username = config.get_smtp_username()
    smtp_password = config.get_smtp_password()

    email_agent = EmailAgent(smtp_server, smtp_port, smtp_username, smtp_password)

    mcp_controller = MCPController(
        hr_input_agent=hr_input_agent,
        search_agent=search_agent,
        resume_parser_agent=resume_parser_agent,
        ranking_agent=ranking_agent,
        email_agent=email_agent
    )

if __name__ == "__main__":
    main()