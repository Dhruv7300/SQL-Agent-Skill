import ast
from langgraph.graph import StateGraph, END
from src.controller.state import SQLFlowState
from src.controller.nodes.schema_search import search_schema
from src.controller.nodes.sql_generator import build_sql_query
from src.controller.nodes.run_query import run_sql_query

# -----------------------------
# 1️⃣ Schema Search (Pinecone)
# -----------------------------
def search_schema_node(state: SQLFlowState) -> SQLFlowState:
    schema_context = search_schema(state["user_query"])

    return {
        **state,
        "retrieved_schema": schema_context
    }


# -----------------------------
# 2️⃣ SQL Generation (LLM)
# -----------------------------
def build_sql_node(state: SQLFlowState) -> SQLFlowState:
    sql_query = build_sql_query(state["retrieved_schema"], state["user_query"])

    return {
        **state,
        "generated_sql": sql_query
    }


# -----------------------------
# 3️⃣ SQL Execution (No Fixing)
# -----------------------------
def execute_sql_node(state: SQLFlowState) -> SQLFlowState:
    result = run_sql_query(state["generated_sql"])
    result = ast.literal_eval(result)  # Convert string representation of list/dict back to actual list/dict

    return {
        **state,
        "result": result,
        "graph": True
    }


# -----------------------------
# LangGraph Flow (Fixed)
# -----------------------------
def build_sql_langgraph():
    graph = StateGraph(SQLFlowState)

    graph.add_node("schema_search", search_schema_node)
    graph.add_node("sql_builder", build_sql_node)
    graph.add_node("sql_executor", execute_sql_node)

    graph.set_entry_point("schema_search")

    graph.add_edge("schema_search", "sql_builder")
    graph.add_edge("sql_builder", "sql_executor")
    graph.add_edge("sql_executor", END)

    return graph.compile()
