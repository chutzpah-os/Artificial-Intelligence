
# About the Project

This project showcases a **financial analysis team** powered by AI agents, each with a specialized role:

- **Financial Researcher**: Gathers the latest financial market information using DuckDuckGo.  
- **Financial Analyst**: Processes and interprets financial data with Yahoo Finance tools (`yfinance`).  

Working collaboratively, these agents generate comprehensive and well-structured financial reports.

## Prerequisites

- Python **3.13+**  
- [**UV (Astral)**](https://docs.astral.sh/uv/) — package and environment manager  

## Description

The project demonstrates the **Agno framework**, highlighting how to design a team of **collaborative AI agents** for financial analysis.

## Tech Stack

- **UV** → Dependency and package management  
- **LLM** → OpenAI (ChatGPT) for natural language processing  

## How to Run

1. Install dependencies:  
   ```bash
   uv sync
````

2. Run the system by specifying the file path:

   ```bash
   uv run <path_to_file>
   ```

   Example:

   ```bash
   uv run examples/1_basic_agent.py
   ```
