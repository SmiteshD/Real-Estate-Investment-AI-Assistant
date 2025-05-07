from agents import property_researcher, property_analyst
from tasks import research_task, analysis_task
from crewai import Crew, Process
import streamlit as st


st.title("🌍 AI-Assisted Property Research")

st.markdown("""
💡 **Boost your Real Estate research with AI!**  
Enter the city of your choice below, and the AI-powered research assistant will create a personalized report including:
 Best Property listings 🗳️ 
 Neighborhood insights 🏢 
 Local market trends 🏗️  
 Rental yield or price 💴 
 Valuable financial metrics(ROI, cap rate etc) 💹
""")


city = st.text_input("Enter the name of the city in which you want to search properties")

if st.button("🚀 Generate Report"):
    if not city:
        st.error("⚠️ Please enter the city name before generating your property report.")
    else:
        st.write("⏳ AI is preparing your report... Please wait.")

        property_research = research_task(city) #initialize task functions
        property_analysis = analysis_task()

        crew = Crew(
            agents=[property_researcher, property_analyst],
            tasks=[property_research, property_analysis],
            process=Process.sequential,
            full_output=True,
            verbose=True,
        )

        result = crew.kickoff()

        st.subheader("✅ Your AI-Powered Property Report")
        st.markdown(result)


        property_report_text = str(result)  #Convert CrewOutput to string

        st.download_button(
            label="📥 Download Report",
            data=property_report_text, 
            file_name=f"Property_report_{city}.txt",
            mime="text/plain"
        )