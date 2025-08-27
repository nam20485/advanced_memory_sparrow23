from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    method: str = "global"

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/query")
async def query_graph(request: QueryRequest):
    # Placeholder that echoes the request; wire to GraphRAG later
    return {"method": request.method, "query": request.query, "result": "placeholder"}
