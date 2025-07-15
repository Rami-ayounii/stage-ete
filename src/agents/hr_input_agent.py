class HrInputAgent:
    def __init__(self):
        self.submissions = []

    def collect_resume(self, resume_data):
        self.validate_resume(resume_data)
        self.submissions.append(resume_data)
        return "Resume submitted successfully."

    def validate_resume(self, resume_data):
        if not isinstance(resume_data, dict):
            raise ValueError("Resume data must be a dictionary.")
        required_fields = ["name", "email", "phone", "experience", "skills"]
        for field in required_fields:
            if field not in resume_data:
                raise ValueError(f"Missing required field: {field}")

    def get_submissions(self):
        return self.submissions