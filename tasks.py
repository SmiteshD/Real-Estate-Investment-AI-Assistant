from crewai import Task
from agents import property_researcher, property_analyst

def research_task(city):
    return Task(
    description=f"Identify and compile relevant real-estate investment opportunities in the city of {city}. Use available tools to search the web for current listings, neighborhood data, rental yields, local development news, and market trends. The output should be structured, relevant, and rich with actionable insights that the analyst can evaluate further.",
    expected_output="""A structured summary (e.g., in table format) containing:
                    Property details (location, type, price, size, etc.)
                    Neighborhood insights (safety, schools, amenities, etc.)
                    Local market trends (price movement, demand/supply)
                    Rental yield or price appreciation data (if available)
                    Relevant links to original sources or listings""",
    agent=property_researcher,
    output_file="research_task_output_internet.md"
)

def analysis_task():
    return Task(
    description="Evaluate the investment potential of the properties researched. Assess financial metrics like ROI, cap rate, cash flow potential, and risk factors. Incorporate neighborhood trends, market conditions, and property-specific data to generate a clear investment recommendation.",
    expected_output="""An investment analysis report including:
                    Property-by-property assessment with financial metrics
                    Strengths and weaknesses of each opportunity
                    Risk analysis (e.g., market volatility, legal issues, etc.)
                    Investment recommendation (buy/hold/skip)""",
    agent=property_analyst,
    output_file="task2_output.md",
)