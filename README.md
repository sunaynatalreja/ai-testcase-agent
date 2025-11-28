# 🧪 AI Test Case Generator 
Automatically generate high-quality **software test cases** from SRS documents using
Google **Gemini 2.5 Flash** + a modular **multi-agent** pipeline.

Supports:
- Requirements understanding
- Scenario discovery
- Structured test case generation
- Quality improvement agent
- Export to **Excel**
- Local CLI runner

---

## 🚀 Features

### ✅ Multi-Agent Architecture
This project uses a chain-of-thought / multi-agent system:
1. **Requirement Understanding Agent** – extracts actors, flows, constraints  
2. **Scenario Discovery Agent** – identifies positive, negative, edge-case scenarios  
3. **Test Case Writer Agent** – generates structured JSON test cases  
4. **Quality Agent** – improves validations, adds missing checks  
5. **Output Composer** – finalizes unified output

### ✅ Input
- PDF SRS documents (multi-page)
- Text requirements

### ✅ Output
- Structured JSON  
- Exported **Excel** file (`.xlsx`)  
- Valid test cases with:  
  - TestCaseID  
  - Description  
  - Preconditions  
  - Steps  
  - ExpectedResult  
  - Priority  

### ✅ API Endpoint
Upload SRS → Download Excel automatically.

### ✅ Local Runner
Run the whole pipeline from your machine without API.

