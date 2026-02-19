from typing import TypedDict

class SQLFlowState(TypedDict):
    user_query: str
    retrieved_schema: str
    generated_sql: str
    result: list[dict]
    graph: bool