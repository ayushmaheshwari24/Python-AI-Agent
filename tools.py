from datetime import datetime

import requests
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun


# --------------------------------------------------
# Save Tool
# --------------------------------------------------

@tool
def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """Save research data to a text file."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_text = (
        f"--- Research Output ---\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
    )

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


# --------------------------------------------------
# Web Search Tool
# --------------------------------------------------

search = DuckDuckGoSearchRun()


@tool
def search_tool(query: str) -> str:
    """Search the web for current information."""

    return search.run(query)


# --------------------------------------------------
# Wikipedia Tool
# --------------------------------------------------

@tool
def wiki_tool(query: str) -> str:
    """Search Wikipedia and return a short summary."""

    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query,
        "srlimit": 1,
    }

    response = requests.get(
        url,
        params=params,
        headers={
            "User-Agent": "ResearchAgent/1.0"
        },
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

    results = data.get("query", {}).get("search", [])

    if not results:
        return f"No Wikipedia results found for: {query}"

    result = results[0]

    return (
        f"Title: {result['title']}\n"
        f"Snippet: {result['snippet']}"
    )


# --------------------------------------------------
# Tool list
# --------------------------------------------------

save_tool = save_to_txt