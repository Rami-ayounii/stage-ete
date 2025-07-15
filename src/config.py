import os

class Config:
    def __init__(self):
        self.load_environment_variables()

    def load_environment_variables(self):
        self.api_key = os.getenv("API_KEY", "your_default_api_key")
        self.db_connection_string = os.getenv("DB_CONNECTION_STRING", "your_default_db_connection_string")
        self.email_service_api_key = os.getenv("EMAIL_SERVICE_API_KEY", "your_default_email_service_api_key")
        self.resume_parser_service_url = os.getenv("Resume_Parser", "http://localhost:5000/parse")

    def get_api_key(self):
        return self.api_key

    def get_db_connection_string(self):
        return self.db_connection_string

    def get_email_service_api_key(self):
        return self.email_service_api_key

    def get_resume_parser_service_url(self):
        return self.resume_parser_service_url

config = Config()