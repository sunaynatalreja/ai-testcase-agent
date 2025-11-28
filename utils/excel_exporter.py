from openpyxl import Workbook

def export_excel(testcases, filename="generated_testcases.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Cases"

    headers = ["TestCaseID", "Description", "Preconditions", "Steps", "ExpectedResult", "Priority"]
    ws.append(headers)

    for tc in testcases:
        ws.append([
            tc.get("TestCaseID",""),
            tc.get("Description",""),
            tc.get("Preconditions",""),
            tc.get("Steps",""),
            tc.get("ExpectedResult",""),
            tc.get("Priority","")
        ])

    wb.save(filename)
    return filename
