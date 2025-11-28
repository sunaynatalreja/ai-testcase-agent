class QualityAgent:
    def run(self, draft_cases, llm):
        prompt = f"""
        Improve the following test cases:

        {draft_cases}

        Add:
        - Missing negative cases
        - Edge cases
        - Better validations
        - Security checks
        - Input boundary tests

        Return improved JSON only.
        """
        return llm(prompt)
