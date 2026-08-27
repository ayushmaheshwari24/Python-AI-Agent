# AI Research Agent

A simple AI research assistant built with Python, LangChain, and Google Gemini.

The agent takes a research query and uses tools like web search and Wikipedia to find relevant information and generate a response.

## Features

- Google Gemini integration
- Web search using DuckDuckGo
- Wikipedia search
- Tool calling with LangChain
- Save research results to a text file

## Tech Stack

- Python
- LangChain
- LangGraph
- Google Gemini
- DuckDuckGo
- Wikipedia
- Pydantic

## Project Structure

```text
Python-AI-Agent/
│
├── main.py
├── tools.py
├── try_gemini.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/ayushmaheshwari24/Python-AI-Agent.git
cd Python-AI-Agent

2. Create & activate virtual environment
python -m venv venv
.\venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Configure API Key
Create a .env file:
GOOGLE_API_KEY=your_gemini_api_key

5. Run
python main.py
