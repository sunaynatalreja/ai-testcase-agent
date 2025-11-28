class TestCaseWriterAgent:
    def run(self, scenarios, llm):
        prompt = f"""
        Convert the scenarios below into a MAXIMUM of 25 test cases.

        SCENARIOS:
        {scenarios}

        Return ONLY valid JSON array, no explanation.
        Format each test case as:

        {{
            "TestCaseID": "",
            "Description": "",
            "Preconditions": "",
            "Steps": "",
            "ExpectedResult": "",
            "Priority": "High/Medium/Low"
        }}

        Ensure JSON is valid.
        """
        return llm(prompt)
