"""
WHAT: Force the LLM to return a validated Pydantic object instead of free text.
WHEN: Extraction, classification, or any time downstream code needs reliable fields.
      This is where LangChain and Pydantic meet — the most useful pattern in the course.
RUN:  python langchain/02_structured_output_pydantic.py
"""

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

load_dotenv()


class PersonInfo(BaseModel):
    """Information extracted about a person."""   # docstring helps the LLM
    name: str = Field(description="Full name of the person")
    age: int | None = Field(default=None, description="Age if mentioned")
    profession: str | None = Field(default=None, description="Job or role if mentioned")


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# One line: wrap the llm so it MUST return a PersonInfo
structured_llm = llm.with_structured_output(PersonInfo)

if __name__ == "__main__":
    text = "Lohith is a 28-year-old telecom engineer from Bengaluru learning AI agents."
    result = structured_llm.invoke(f"Extract person info from: {text}")

    print(type(result))          # <class '__main__.PersonInfo'> — a real Pydantic object
    print(result.name, "|", result.age, "|", result.profession)
    print(result.model_dump())   # normal Pydantic methods work
