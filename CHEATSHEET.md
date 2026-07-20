# CHEATSHEET — the lines I look up most

## Pydantic

```python
from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    name: str
    age: int = Field(gt=0, description="Age in years")
    email: str | None = None

    @field_validator("name")
    @classmethod
    def name_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("name cannot be empty")
        return v

u = User(name="Lohith", age=28)
u.model_dump()          # → dict
u.model_dump_json()     # → JSON string
User.model_validate({"name": "A", "age": 1})   # dict → model
User.model_validate_json('{"name":"A","age":1}')
```

## LangChain — model + prompt + chain (LCEL)

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}"),
])

chain = prompt | llm | StrOutputParser()
chain.invoke({"question": "What is RAG?"})
```

## LangChain — structured output (LLM → Pydantic)

```python
structured_llm = llm.with_structured_output(User)   # User = Pydantic model
result = structured_llm.invoke("Extract: Lohith is 28")   # → User instance
```

## LangChain — tool calling

```python
from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""     # docstring = tool description (required!)
    return f"Sunny in {city}"

llm_with_tools = llm.bind_tools([get_weather])
resp = llm_with_tools.invoke("Weather in Bengaluru?")
resp.tool_calls    # → [{"name": "get_weather", "args": {"city": "Bengaluru"}, ...}]
```

## Messages

```python
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage
```

## Env vars

```python
from dotenv import load_dotenv
load_dotenv()   # reads .env into os.environ
```
