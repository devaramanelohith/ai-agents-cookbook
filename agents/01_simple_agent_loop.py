"""
WHAT: A minimal agent loop from scratch — LLM picks tools, we execute, feed results
      back, repeat until it answers. This is what frameworks automate for you.
WHEN: Understand THIS before using prebuilt agents (LangGraph etc.) — then those
      stop feeling like magic.
RUN:  python agents/01_simple_agent_loop.py
"""

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"It is 24°C and cloudy in {city}."


@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


tools = {"get_weather": get_weather, "multiply": multiply}
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools(list(tools.values()))


def run_agent(question: str, max_turns: int = 5) -> str:
    messages = [HumanMessage(content=question)]

    for _ in range(max_turns):
        ai_msg = llm.invoke(messages)
        messages.append(ai_msg)

        if not ai_msg.tool_calls:          # no tool needed → final answer
            return ai_msg.content

        for call in ai_msg.tool_calls:     # execute each requested tool
            result = tools[call["name"]].invoke(call["args"])
            print(f"  [tool] {call['name']}({call['args']}) → {result}")
            messages.append(ToolMessage(content=str(result), tool_call_id=call["id"]))

    return "Max turns reached."


if __name__ == "__main__":
    print(run_agent("What's the weather in Bengaluru, and what is 7 times 12?"))
