import os
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise Exception("Please set GEMINI_API_KEY environment variable")

genai.configure(api_key=GEMINI_API_KEY)
