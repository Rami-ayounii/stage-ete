# HR Automation App

## Overview
The HR Automation App streamlines recruitment by automating resume parsing, semantic ranking, and candidate communication. It leverages LLMs for advanced analysis, supports dynamic workflows with feedback, and provides a simple dashboard UI for HR teams.

## Features
- **Semantic Resume Parsing & Ranking:** Uses LLMs for extracting and matching candidate data to job descriptions.
- **Dynamic MCP Workflow:** Modular, feedback-driven process orchestration.
- **Persistent Storage:** Stores resumes, jobs, results, and feedback.
- **Dashboard UI:** Simple web interface for HR to manage jobs, candidates, and results.
- **Robust Error Handling & Security:** Input validation, logging, and secure config.
- **Automated Testing:** Pytest-based test suite.
- **Comprehensive Documentation:** User, developer, and API guides.

## Architecture
- **Agents:**  
  - HR Input Agent  
  - Search Agent  
  - Resume Parser Agent (LLM & internal tool)  
  - Ranking Agent (LLM)  
  - Email Agent  
- **Tools:**  
  - Internal and external API integrations  
- **MCP Controller:**  
  - Orchestrates dynamic workflows and feedback  
- **Storage:**  
  - Persistent database (e.g., SQLite)  
- **Dashboard:**  
  - Streamlit-based UI

## Project Structure
```
hr-automation-app
├── src
│   ├── agents
│   │   ├── hr_input_agent.py
│   │   ├── search_agent.py
│   │   ├── resume_parser_agent.py
│   │   ├── ranking_agent.py
│   │   └── email_agent.py
│   ├── tools
│   │   ├── internal_tool.py
│   │   ├── external_api.py
│   │   └── llm_tool.py
│   ├── mcp
│   │   └── controller.py
│   ├── storage.py
│   ├── main.py
│   └── config.py
├── dashboard.py
├── requirements.txt
├── tests/
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd hr-automation-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   - Create a `.env` file or edit `src/config.py` to include API keys, database URLs, and LLM credentials.

4. **Initialize the database (if needed):**
   ```bash
   python src/storage.py
   ```

5. **Run the main application:**
   ```bash
   python src/main.py
   ```

6. **Launch the dashboard UI:**
   ```bash
   streamlit run dashboard.py
   ```

7. **Run automated tests:**
   ```bash
   pytest
   ```

## Usage Guidelines
- Upload resumes and job descriptions via the dashboard or API.
- The system parses, ranks, and stores results automatically.
- HR can review results, provide feedback, and trigger re-ranking.
- All actions and errors are logged for traceability.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Documentation
- **User Guide:** See `docs/user_guide.md`
- **Developer Guide:** See `docs/developer_guide.md`
- **API Guide:** See `docs/api_guide.md`