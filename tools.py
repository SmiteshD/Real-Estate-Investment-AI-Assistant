from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

load_dotenv()
serper_api_key=os.getenv("SERPER_API_KEY")

search_tool = SerperDevTool(api_key=serper_api_key)