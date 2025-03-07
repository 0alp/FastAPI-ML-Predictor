import joblib
import numpy as np
import os
from models.prediction_model import PredictionInput, PredictionOutput


def load_model():
    model_path = "model/svm_model.pkl"
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model file not found!")
    return joblib.load(model_path)


try:
    model = load_model()
except Exception as e:
    model = None
    print(f"Error loading model: {e}")


def make_prediction(input_data: PredictionInput) -> PredictionOutput:
    if model is None:
        raise Exception("Model could not be loaded!")

    try:
       
        input_features = np.array([[
            input_data.BMI, input_data.Glucose, input_data.WaistCircumference,
            input_data.WHR, input_data.FamilyHistory, input_data.HbA1c_Log,
            input_data.BloodPressure_Log, input_data.Age_Group_Middle_aged, input_data.Age_Group_Old
        ]])

      
        prediction = model.predict(input_features)[0]

        return PredictionOutput(category=int(prediction))

    except Exception as e:
        raise Exception(f"An error occurred during the estimate: {str(e)}")
