class ScenarioDiscoveryAgent:
    def run(self, req_info, llm):
        prompt = f"""
        Using the extracted requirement details:

        {req_info}

        Identify ALL possible scenarios:
        - Positive flows
        - Negative flows
        - Error conditions
        - Boundary cases
        - Edge cases
        - Missing validation areas

        Return as bullet list.
        """
        return llm(prompt)
