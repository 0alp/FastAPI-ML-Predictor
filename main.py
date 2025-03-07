from fastapi import FastAPI, HTTPException
from models.prediction_model import PredictionInput, PredictionOutput
from services.predict import make_prediction


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Support Vector is working!"}

@app.get("/ping")
def ping():
    return {"ping": "pong!"}

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    try:
        result = make_prediction(input_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred during the estimate: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7584)
