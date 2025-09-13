import os

from langchain.chains import GraphCypherQAChain
from langchain_core.tools import tool
from langchain_community.graphs import Neo4jGraph
from langchain_community.vectorstores import Neo4jVector

from langchain_openai import OpenAIEmbeddings, ChatOpenAI

print(os.getenv("NEO4J_URL"))

neo4j_vector_store = Neo4jVector.from_existing_graph(
    embedding=OpenAIEmbeddings(model="text-embedding-3-large"),
    url=os.getenv("NEO4J_URL"),
    username=os.getenv("NEO4J_USER"),
    password=os.getenv("NEO4J_PASSWORD"),
    index_name="movie_index",
    node_label="Movie",
    text_node_properties=["title", "description", "location"],
    embedding_node_property="movie_embedding",
)

neo4j_graph = Neo4jGraph(
    url=os.getenv("NEO4J_URL"),
    username=os.getenv("NEO4J_USER"),
    password=os.getenv("NEO4J_PASSWORD"),
)


@tool
def get_movies_by_description(description: str):
    """
    Function to search for a movie through a description (synopsis).
    The input is necessarily a descriptive text, never a movie name.
    The return is a list of movies that most resemble the provided description.
    """
    return neo4j_vector_store.similarity_search(description, top_n=10)


@tool
def get_info_about_movies(query: str):
    """
    Function that returns information about movies.
    The input can be either a question about an actor or about a movie.
    For example: which movies did actor X participate in? or which actors starred in movie X?
    """

    chain = GraphCypherQAChain.from_llm(
        ChatOpenAI(temperature=0, model="gpt-4o"),
        graph=neo4j_graph,
        verbose=False,
        return_direct=True,
        top_k=10,
    )
    return chain.invoke({"query": query})
