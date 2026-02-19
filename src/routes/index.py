from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.middleware.run_graph import run_sql_pipeline

app = FastAPI(title="SQL Agent API")

class SQLAgentRequest(BaseModel):
    user_query: str

@app.post("/sql-agent")
async def get_sql_agent(payload: SQLAgentRequest):
    """
    Get SQL agent response for a given user query
    """
    try:
        result = run_sql_pipeline(payload.user_query)
        return JSONResponse(content=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to execute SQL pipeline")