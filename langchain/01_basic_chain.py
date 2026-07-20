"""
WHAT: The core LangChain pattern — prompt | llm | parser (LCEL pipe syntax).
WHEN: The starting point of almost everything in LangChain.
RUN:  python langchain/01_basic_chain.py   (needs OPENAI_API_KEY in .env)
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a concise assistant. Answer in 2 sentences max."),
    ("human", "{question}"),
])

# LCEL: pipe components together. Output of one = input of next.
chain = prompt | llm | StrOutputParser()

if __name__ == "__main__":
    answer = chain.invoke({"question": "What is an AI agent?"})
    print(answer)

    # Streaming variant — same chain, different call
    for chunk in chain.stream({"question": "Explain RAG briefly."}):
        print(chunk, end="", flush=True)
    print()
