
# Guided Practice with CrewAI in Google Colab

This repository contains a guided practice project developed in Google Colab.
All exercises and code examples can be run directly in your browser — no installation required.


# Project Overview

In this practice, we built a small Intelligent Agents project using Python and CrewAI.
The agents collaborate to generate tutorials, beginner guides, and project ideas, which are then exported as markdown files.
Click below to open the interactive notebook:
[![Abrir no Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1BoC0O5syRwGYbvKjwjxNIShE7gTmhHRE?usp=sharing)


```mermaid
---
config:
  layout: dagre
  theme: neo-dark
---
flowchart TD
  subgraph C["🤖 Crew: Python + CrewAI"]
    subgraph Agentes["Agentes"]
      MP["🧑‍🏫 Mentor Python"]
      EC["👨‍💻 Especialista CrewAI"]
      GI["💡 Gerador de Ideias"]
    end
    subgraph Tarefas["Tarefas"]
      T1["📘 Guia Iniciante em Python"]
      T2["🔧 Tutorial de Instalação CrewAI"]
      T3["🤩 Ideias de Projetos com Python e CrewAI no Colab"]      
      subgraph Saídas["Saídas"]
        O1["📄 guia_python.md"]
        O2["📄 tutorial_crewai.md"]
        O3["📄 projetos_colab.md"]
      end
    end
  end
  MP --> T1 --> O1
  EC --> T2 --> O2
  GI --> T3 --> O3

```

