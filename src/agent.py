# from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

from src.llm_provider import llm

# Create the agent
memory = MemorySaver()
model = llm
# search = TavilySearchResults(max_results=2)
tools = [
    # search
]
agent_executor = create_react_agent(model, tools, checkpointer=memory)


# def run_agent(user_input: str, thread_id: str):
#     config = {"configurable": {"thread_id": thread_id}}
#
#     for step in agent_executor.stream(
#             {"messages": [HumanMessage(content=user_input)]},
#             config,
#             stream_mode="values",
#     ):
#         step["messages"][-1].pretty_print()

def run_agent(user_input: str, thread_id: str) -> str:
    config = {"configurable": {"thread_id": thread_id}}
    response = ""

    for step in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]},
            config,
            stream_mode="values",
    ):
        message = step["messages"][-1]
        response = message.content  # collect the last message content

    return response
