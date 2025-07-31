from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import pickle
import pandas as pd

# Load your trained model
with open('iris_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

# Define input schema
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(data: IrisInput):
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([{
            "sepal length (cm)": data.sepal_length,
            "sepal width (cm)": data.sepal_width,
            "petal length (cm)": data.petal_length,
            "petal width (cm)": data.petal_width
        }])

        prediction = model.predict(input_df)
        class_names = ['setosa', 'versicolor', 'virginica']
        result = class_names[prediction[0]]
        return JSONResponse(content={"predicted_class": result})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
