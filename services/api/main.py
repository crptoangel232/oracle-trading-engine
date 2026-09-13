from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from enum import Enum
app=FastAPI(title="Oracle Trading Engine API",version="0.1.0")
class Mode(str,Enum): paper="paper"; signal="signal"; live="live"
class Risk(BaseModel): risk_per_trade:float=Field(1,ge=.1,le=5); daily_loss_limit:float=Field(3,ge=.5,le=10); max_positions:int=Field(5,ge=1,le=20)
class Decision(BaseModel): symbol:str; action:str; confidence:float; stop_loss:float|None=None; take_profit:float|None=None
@app.get("/health")
def health(): return {"status":"ok","engine":"oracle","mode":"paper"}
@app.post("/v1/analyse")
def analyse(symbol:str): return {"symbol":symbol,"action":"WAIT","confidence":0,"reason":"Market data adapter not connected; no order is authorised."}
@app.post("/v1/risk/check")
def risk_check(risk:Risk,decision:Decision): return {"approved":False,"reason":"Execution bridge is disabled in scaffold mode","risk":risk.model_dump()}
@app.post("/v1/engine/{mode}")
def engine(mode:Mode):
    if mode is Mode.live: raise HTTPException(403,"Live execution is disabled until a broker connection, risk profile and explicit live-mode approval are configured.")
    return {"mode":mode.value,"running":True}