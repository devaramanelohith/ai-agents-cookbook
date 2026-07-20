"""
WHAT: Define tools with @tool and let the LLM decide when to call them.
WHEN: Foundation of agents — the LLM picks a tool + args, YOUR code executes it.
KEY:  The docstring is REQUIRED — it's the tool description the LLM reads.
RUN:  python langchain/03_tool_calling.py
"""

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    # In real life: call a weather API. Here: fake it.
    return f"It is 24°C and cloudy in {city}."


@tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return the sum."""
    return a + b


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm_with_tools = llm.bind_tools([get_weather, add_numbers])

if __name__ == "__main__":
    resp = llm_with_tools.invoke("What's the weather in Bengaluru?")

    # The LLM did NOT run the tool — it just asked for it:
    print(resp.tool_calls)
    # → [{'name': 'get_weather', 'args': {'city': 'Bengaluru'}, 'id': '...'}]

    # We execute it ourselves:
    for call in resp.tool_calls:
        if call["name"] == "get_weather":
            print(get_weather.invoke(call["args"]))
