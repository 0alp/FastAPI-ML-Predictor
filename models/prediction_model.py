from pydantic import BaseModel

class PredictionInput(BaseModel):
    BMI: float
    Glucose: float
    WaistCircumference: float
    WHR: float
    FamilyHistory: int
    HbA1c_Log: float
    BloodPressure_Log: float
    Age_Group_Middle_aged: int
    Age_Group_Old: int

class PredictionOutput(BaseModel):
    category: int  
