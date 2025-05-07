from langchain_groq import ChatGroq
from tools import search_tool
from crewai import Agent
from crewai import LLM
from langchain_ollama.llms import OllamaLLM
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="groq/llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=10,
)

property_researcher = Agent(
    role="Lead researcher for real-estate investment opportunities.",
    goal="To identify and analyze high-potential retail investment properties and  source accurate and up-to-date information on real estate listings, local market trends, neighborhood demographics, rental yields, and recent developments. Use suitable available tools to gather comprehensive data that can support investment decisions.",
    backstory="You have a background in real estate market research and are skilled at digging into public records, news articles, property listings, and investment platforms. You know how to identify relevant data and eliminate noise. Your findings will directly support the property_analyst, so clarity, structure, and relevance in your research are critical.",
    allow_delegation=False,
    max_iter= 5,
    llm=llm,
    tools=[search_tool]
)


property_analyst = Agent(
    role="Senior investment analyst responsible for evaluating the potential of properties identified by the researcher.",
    goal="To assess each property based on investment metrics such as ROI, cash flow, cap rate, risk level, and appreciation potential. Using the research provided, you must turn raw data into clear investment insights and make well-reasoned recommendations.",
    backstory="You come from an investment analysis background with a strong understanding of real estate economics. You're comfortable working with both qualitative and quantitative data and can turn complex data into actionable insights. You collaborate closely with the property_researcher and rely on their findings to perform deep-dive financial and strategic evaluations.",
    allow_delegation=False,
    max_iter= 5,
    llm=llm
)




