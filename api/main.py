
from fastapi import FastAPI
from decision.policy import decide

app = FastAPI()

@app.post("/decide")
def decide_route(p90_eta: float, sla: float):
    return {"decision": decide(p90_eta, sla)}
