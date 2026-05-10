from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END
from typing import TypedDict
import os
from dotenv import load_dotenv

from tools import (
    log_interaction_tool,
    edit_interaction_tool,
    get_hcp_profile,
    interaction_summary_tool,
    next_best_action_tool,
)

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="gemma2-9b-it"
)

class AgentState(TypedDict):
    user_input: str
    intent: str
    response: str


# Step 1: detect intent
def detect_intent(state: AgentState):
    text = state["user_input"].lower()

    if "edit" in text:
        state["intent"] = "edit"
    elif "profile" in text:
        state["intent"] = "profile"
    elif "summary" in text:
        state["intent"] = "summary"
    elif "next" in text:
        state["intent"] = "next"
    else:
        state["intent"] = "log"

    return state


# Step 2: tool router
def run_tool(state: AgentState):
    intent = state["intent"]

    if intent == "edit":
        result = edit_interaction_tool(1, "2026-05-20")
    elif intent == "profile":
        result = get_hcp_profile()
    elif intent == "summary":
        result = interaction_summary_tool()
    elif intent == "next":
        result = next_best_action_tool()
    else:
        # ✅ THIS IS THE FIX (LLM NOW USED)
        response = llm.invoke(state["user_input"])
        result = response.content

    state["response"] = result
    return state

# Build graph
graph = StateGraph(AgentState)
graph.add_node("intent_node", detect_intent)
graph.add_node("tool_node", run_tool)

graph.set_entry_point("intent_node")
graph.add_edge("intent_node", "tool_node")
graph.add_edge("tool_node", END)

agent = graph.compile()