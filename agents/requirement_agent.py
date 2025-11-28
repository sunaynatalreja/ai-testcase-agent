class RequirementUnderstandingAgent:
    def run(self, requirement_text, llm):
        prompt = f"""
        Extract the following from the SRS section:

        - Actors
        - Preconditions
        - Main flow steps
        - Alternate flows
        - Business rules
        - Constraints

        Return everything in clean text.

        SRS Content:
        {requirement_text}
        """
        return llm(prompt)
