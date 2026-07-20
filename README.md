# AI Agents Cookbook 🧑‍🍳

My personal, runnable reference for AI agent patterns — LangChain, Pydantic, and agent architectures.

**Why this repo exists:** I don't memorize syntax. I keep every pattern I learn here as a small,
runnable file, so I can find it in 10 seconds with search instead of re-watching class recordings.

## How I use it

- One pattern per file, numbered in learning order (`01_`, `02_`, ...)
- Every file has a docstring: *what it shows* and *when to use it*
- `CHEATSHEET.md` holds the 20 lines I look up most often
- Search everything: `Ctrl+Shift+F` in VS Code, or GitHub search

## Structure

```
langchain/   → chains, prompts, structured output, tool calling
pydantic/    → models, validation, serialization
agents/      → agent loops, tools, memory
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # then add your API keys
```

## Run any example

```bash
python langchain/01_basic_chain.py
```

## Rules I follow

1. If I learned it in class, it gets a file here **the same day**
2. Rebuild from memory first, peek only when stuck
3. Pin versions — LangChain's API changes fast; pinned code keeps working
