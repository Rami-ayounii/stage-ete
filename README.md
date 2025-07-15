# HR Automation App

## Overview
The HR Automation App is designed to streamline the recruitment process by automating the analysis and ranking of resumes based on job descriptions. The application consists of multiple agents that work together to collect, parse, analyze, and communicate results regarding resume submissions.

## Architecture
The project is structured around several key components:

- **HR Input Agent**: Handles input from HR, including collecting and validating resume submissions.
- **Search Agent**: Responsible for searching and filtering resumes based on job descriptions and requirements.
- **Resume Parser Agent**: Utilizes an internal tool to parse resumes and extract relevant information.
- **Ranking Agent**: Ranks the parsed resumes based on their relevance to the job description.
- **Email Agent**: Manages sending emails to candidates or HR with the results of the resume analysis.

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
│   │   └── external_api.py
│   ├── mcp
│   │   └── controller.py
│   ├── main.py
│   └── config.py
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd hr-automation-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the application by editing the `src/config.py` file to include necessary API keys and settings.

4. Run the application:
   ```
   python src/main.py
   ```

## Usage Guidelines
- Ensure that all resumes are submitted in a supported format.
- The application will automatically parse and analyze the resumes against the provided job descriptions.
- Results will be communicated via email to the designated recipients.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.