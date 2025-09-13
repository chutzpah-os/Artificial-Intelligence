

# AI Applications with Autonomous Agents

This project was developed to teach basic concepts related to building agents using Large Language Models (LLMs).

The focus is on developing a Python-based assistant capable of answering questions about movies, stored as a Knowledge Graph in [neo4j](https://neo4j.com).



## How to Use This Project

### I already have a GitHub account
- **I want to build upon this project**: In this case, fork this repository. This way, you can extend it in your own GitHub, adding your own code — which I highly recommend.
- **I just want to follow this project**: If you only want to keep track of its progress, click on **Watch** to be notified of updates.
- If you find this project useful, consider giving it a **star** ⭐!

### I don’t have a GitHub account
First, I recommend creating a GitHub account and following one of the options above. If you prefer not to create an account, you can:

- **If you have Git installed on your machine**:  
  Clone this repository with:

```bash
  git clone https://github.com/chutzpah-os/artificial-intelligence/ReAct-Agent-with-langchain
````

Then, edit the code in your favorite IDE.

* **If you don’t have Git installed**:
  Download the project by clicking the green **Code** button and then selecting **Download ZIP**.

---

## Environment Setup

### OpenAI

We will use OpenAI’s language and embedding models.
You need to create an OpenAI account and generate an API Key.

### Docker

Docker and docker-compose are required to run the assistant.

### Python – Virtual Environment

We’ll use **Anaconda** to manage Python virtual environments. Installation instructions can be found [here](https://docs.anaconda.com/free/anaconda/install/).

Once Anaconda is installed, create a virtual environment:

```bash
conda create -n llm-agent python=3.9
```

Activate the new environment:

```bash
conda activate llm-agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Database

To start the Neo4j service, run:

```bash
docker-compose up -d
```

Then, ingest the movie catalog. In the `notebooks` folder, you’ll find a Jupyter Notebook for this purpose: `ingest_data.ipynb`.

---

## Solution Overview

The core of the conversational bot is a **ReAct Agent**, designed to extract information from a Knowledge Graph in Neo4j.
Specifically, the bot consists of an **agent** and a set of **tools**. During an interaction:

1. The agent decides what action to take, which may include using a tool.
2. If a tool is invoked, the results are returned to the agent.
3. If no tool is needed, the interaction ends with a direct response to the user.

---

## ReAct Agent Implementation

The ReAct agent was implemented using **LangChain (v0.2)** and **LangGraph**.
It operates as a **state graph** composed of three main components:

* **State**: A data structure that stores the agent’s current status.
* **Nodes**: Python functions encoding the agent’s logic. They take the current state as input, perform an action, and return an updated state.
* **Edges**: Python functions that determine the next node based on the current state.

The **main node (agent)** runs a language model (**Azure GPT-4o, version 2024-05-13**) to decide whether it needs to fetch new data from the database or can provide an appropriate response directly.
Execution ends when there are no further actions to take.

---

## Why LangChain?

LangChain is an open-source framework for building applications with LLMs.
These models, pre-trained on large volumes of data, can answer questions or generate images from text.

LangChain provides tools to improve customization and accuracy, allowing developers to:

* Create new prompts or refine existing ones.
* Allow models to access fresh data without retraining.


---

## Note

I learned and developed this project during a class at **DIO**.

---

## Contact

If you need help or want to connect, feel free to reach out:

📎 [LinkedIn](https://www.linkedin.com/haniel-rolemberg)


