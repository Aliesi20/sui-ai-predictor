from fastapi import FastAPI, Request
import numpy as np

app = FastAPI()

@app.post("/predict")
async def predict(request: Request):
    body = await request.json()
    ohlcv = np.array(body["ohlcv"])
    latest_close = ohlcv[-1][4]
    trend = "long" if ohlcv[-1][4] > ohlcv[-2][4] else "short"
    return {
        "prediction": trend,
        "next_price": latest_close * (1.02 if trend == "long" else 0.98),
        "confidence": 0.76
    }
