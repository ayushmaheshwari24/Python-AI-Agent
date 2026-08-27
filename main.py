from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from tools import search_tool, wiki_tool, save_tool


# ============================================================
# Load environment variables
# ============================================================

load_dotenv()


# ============================================================
# Gemini LLM
# ============================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)


# ============================================================
# Tools
# ============================================================

tools = [
    search_tool,
    wiki_tool,
    save_tool,
]


# ============================================================
# Create AI Agent
# ============================================================

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are a research assistant.

Your job is to research the user's query and provide an accurate,
clear and well-structured answer.

You have access to the following tools:

1. Search Tool
   - Use it when current or web-based information is required.

2. Wikipedia Tool
   - Use it when general factual information can be obtained
     from Wikipedia.

3. Save Tool
   - Use it when the user asks to save research or information
     into a text file.

Use tools when they are useful.
Do not use tools unnecessarily.

When answering:
- Clearly identify the topic.
- Provide a useful summary.
- Mention the sources used.
- Mention which tools were used.
- Do not expose internal reasoning or tool-calling details.
"""
)


# ============================================================
# Get User Query
# ============================================================

query = input("\nWhat can I help you research? ")


# ============================================================
# Run Agent
# ============================================================

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": query,
            }
        ]
    }
)


# ============================================================
# Get Final Response
# ============================================================

final_message = result["messages"][-1]

content = final_message.content


# ============================================================
# Display Result
# ============================================================

print("\n" + "=" * 60)
print("RESEARCH RESULT")
print("=" * 60)

if isinstance(content, list):

    for item in content:

        if isinstance(item, dict) and item.get("type") == "text":
            print(item["text"])

else:
    print(content)


print("=" * 60)