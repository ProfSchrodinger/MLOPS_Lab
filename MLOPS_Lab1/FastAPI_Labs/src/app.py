from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from predict import predict_data

app = FastAPI()

# Diabetes dataset has 10 numeric features
class DiabetesData(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float

class DiabetesResponse(BaseModel):
    prediction: float
@app.get("/", status_code=status.HTTP_200_OK)
async def health_ping():
    return {"status": "healthy"}

@app.post("/predict", response_model=DiabetesResponse)
async def predict_diabetes(features: DiabetesData):
    try:
        # Arrange features in the same order as the dataset
        input_data = [[
            features.age,
            features.sex,
            features.bmi,
            features.bp,
            features.s1,
            features.s2,
            features.s3,
            features.s4,
            features.s5,
            features.s6,
        ]]

        prediction = predict_data(input_data)
        return DiabetesResponse(prediction=float(prediction[0]))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
