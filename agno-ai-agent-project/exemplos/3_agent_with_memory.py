from dotenv import load_dotenv #carrega as variáveis de ambiente

load_dotenv()

from textwrap import dedent #formata o texto

from agno.agent import Agent #agente

from agno.memory.v2.db.sqlite import SqliteMemoryDb #constroi a memória do agente
from agno.memory.v2.memory import Memory #memória do agente

from agno.models.openai import OpenAIChat #modelo de IA

from agno.storage.sqlite import SqliteStorage #banco de dados da sessão


## Banco para armazenar a sessão:
agent_storage = SqliteStorage(table_name="agent_sessions", db_file="data.db") #banco de dados da sessão

## Banco para servir de memória para o agente:
memoria_agente = Memory( #memória do agente
    db=SqliteMemoryDb(
        table_name="agent_memory", #banco de dados da memória
        db_file="agent_memory.db",
    ),
)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"), #modelo de IA
    user_id="Gustavo", ### user ID
    session_id="1", ### sessão ID
    memory=memoria_agente, #memória do agente
    enable_user_memories=True,
    enable_session_summaries=True, #sumário da sessão
    storage=agent_storage, ### banco da sessão
    add_history_to_messages=True, #histórico da sessão
    num_history_responses=3,
    description=dedent("""\
        Você é um assistente de IA útil e amigável com excelente memória. #descrição do agente
        - Lembre-se de detalhes importantes sobre os usuários e referencie-os naturalmente
        - Mantenha um tom caloroso e positivo enquanto é preciso e útil
        - Quando apropriado, refira-se a conversas e memórias anteriores
        - Sempre seja honesto sobre o que você lembra ou não lembra"""), #descrição do agente
)

while True:
    message = input("Entre com a mensagem:") #mensagem do usuário
    if message in ['q']:
        break

    agent.print_response(message=message, stream=True, markdown=True) #resposta do agente   
    print("")
