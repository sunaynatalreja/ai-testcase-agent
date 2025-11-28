from agents.requirement_agent import RequirementUnderstandingAgent
from agents.scenario_agent import ScenarioDiscoveryAgent
from agents.testcase_agent import TestCaseWriterAgent
from agents.quality_agent import QualityAgent
from llm.gemini_llm import llm_call
import json
import re

class TestCaseAgentOrchestrator:

    def generate(self, requirement_text):
        req_agent = RequirementUnderstandingAgent()
        scenario_agent = ScenarioDiscoveryAgent()
        testcase_agent = TestCaseWriterAgent()
        quality_agent = QualityAgent()

        req_info = req_agent.run(requirement_text, llm_call)
        scenarios = scenario_agent.run(req_info, llm_call)
        draft = testcase_agent.run(scenarios, llm_call)
        refined = quality_agent.run(draft, llm_call)
        refined = refined.strip()

        # Remove ```json ... ```
        refined = re.sub(r"```json", "", refined)
        refined = re.sub(r"```", "", refined)

        # Remove ``` blocks with or without language
        refined = re.sub(r"```[\s\S]*?```", "", refined)

        # Remove any accidental backticks
        refined = refined.replace("`", "").strip()
        # Ensure JSON validity
        try:
            tc_json = json.loads(refined)
        except:
            raise Exception("LLM did not return valid JSON test cases")

        return tc_json
