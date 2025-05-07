# 🏠 Real-Estate-Investment-AI-Assistant

An AI-powered assistant for researching and analyzing real estate investment opportunities using multi-agent collaboration, Groq LLMs, and real-time web search tools. Built with LangChain, CrewAI, Groq and Streamlit.

## 🔍 What It Does

This AI assistant helps users explore and evaluate retail real estate investments in any city. It performs two key tasks through separate agents:

1. **Property Research Agent** – Gathers real-time property listings, neighborhood insights, market trends, and rental yields using search tools.
2. **Investment Analyst Agent** – Evaluates the properties based on ROI, cap rate, cash flow, and risk to generate actionable recommendations.

---

## 🧠 Powered By

- **CrewAI** - For multi-agentic orchestration.
- **Groq LLM (LLaMA 3)** – High-speed, cost-effective LLMs for reasoning and analysis.
- **LangChain** – Language model tooling and task chaining.
- **Serper.dev API** – Google Search API for real-time data gathering.
- **Streamlit** – Interactive and minimal front-end.

---

## 🚀 How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/Real-Estate-Investment-AI-Assistant.git
cd Real-Estate-Investment-AI-Assistant
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add Environment Variables

Create a `.env` file in the root directory:

```bash
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

### 4. Run the App
```bash
streamlit run app.py
```

---

## 📄 Example Output

Each report includes:

- 📌 Property listings with key details  
- 🏘️ Neighborhood & demographic insights  
- 📊 Local market trends  
- 💰 Rental yields or appreciation metrics  
- 📈 ROI, Cap Rate, Risk Level analysis  
- ✅ Buy/Hold/Skip recommendation  

---

## 📦 Project Structure

```
├── agents.py          # Defines property researcher and analyst agents
├── tasks.py           # Research and analysis task logic
├── tools.py           # Web search tools (Serper)
├── app.py             # Streamlit front-end
├── .env               # API keys (not committed)
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## 🧩 Future Enhancements

- Upload CSV property data for personalized analysis  
- Visualizations (ROI trends, maps, etc.)  
- Multi-city or bulk analysis mode  
- Authentication for saved report history  

---

## ⭐ Show Your Support

If you found this project useful:
- ⭐ Star this repo  
- 🛠️ Use it in your own AI portfolio  
- 📣 Share feedback and improvements via issues or pull requests  
