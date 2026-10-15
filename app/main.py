from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict():
    return {
        "vessel_count": 1,
        "detections": [
            {
                "class": "ship",
                "confidence": 0.85,
                "box": [100, 150, 300, 350]
            }
        ]
    }