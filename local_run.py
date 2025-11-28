from orchestrator.agent_orchestrator import TestCaseAgentOrchestrator
from utils.srs_loader import load_srs
from utils.excel_exporter import export_excel

def run_local(srs_path):
    print("[1] Loading SRS:", srs_path)
    text = load_srs(srs_path)

    print("[2] Running AI Agents...")
    orchestrator = TestCaseAgentOrchestrator()
    testcases = orchestrator.generate(text)

    print("[3] Exporting to Excel...")
    excel_file = export_excel(testcases, "local_testcases.xlsx")

    print("\n🎉 DONE!")
    print("Generated Excel:", excel_file)
    print("Total Test Cases:", len(testcases))

    print("\n--- SAMPLE OUTPUT ---")
    for i, tc in enumerate(testcases[:3]):
        print(f"\nTest Case #{i+1}:")
        print("ID:", tc["TestCaseID"])
        print("Desc:", tc["Description"])
        print("Steps:", tc["Steps"])
        print("Expected:", tc["ExpectedResult"])

if __name__ == "__main__":
    # UPDATE THIS WITH YOUR SRS FILE PATH
    run_local("data/sample_srs.pdf")
