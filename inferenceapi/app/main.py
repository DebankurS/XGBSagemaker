from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from pydantic import BaseModel
from xgboost import XGBRanker
import numpy as np
from fastapi.responses import JSONResponse


model = XGBRanker()

@asynccontextmanager
async def lifespan(app:FastAPI):
    model.load_model("/modeldir/xgbmodelfile.json")

    yield

app = FastAPI(lifespan=lifespan)

class PredictionRequest(BaseModel):
    features: list[list[float]] | list[float]

@app.post("/invocations")
def predict(inputdata: PredictionRequest):

    data = np.array(inputdata.features)
    if len(data.shape)==1:
        data = data.reshape(1,-1)
    
        prediction = model.predict(data)
        return {"predictions": prediction.tolist()}
    else:
        prediction = model.predict(data)

        return {"predictions": prediction.tolist()}

@app.get("/ping")
def health_check():
    return {"Health":"OK"}