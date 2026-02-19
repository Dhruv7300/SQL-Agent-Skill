from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
LLM_API_KEY = os.getenv("LLM_API_KEY")

llm = ChatOpenAI(
    model="arcee-ai/trinity-large-preview:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=LLM_API_KEY,
    default_headers={
        "HTTP-Referer": "http://localhost",   # optional but recommended
        "X-Title": "Local RAG Script"
    }
)
