from src.controller.sql_agent.workflow import build_sql_langgraph

def run_sql_pipeline(user_query: str):
    graph = build_sql_langgraph()

    final_state = graph.invoke({
        "user_query": user_query
    })
    if 'Error' in final_state["result"]:
        return {
        "status": "An error occurred while executing the SQL query. Please try again."
        }
    return {
        "result": final_state["result"],
        "executed_query": final_state["generated_sql"],
        "graph": final_state["graph"],
        "status": "SQL query executed successfully."
    }