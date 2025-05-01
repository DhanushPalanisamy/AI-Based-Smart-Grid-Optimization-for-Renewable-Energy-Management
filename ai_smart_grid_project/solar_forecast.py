import joblib
import numpy as np

model = joblib.load("models/solar_model.pkl")

def predict_solar(input_data):
    input_array = np.array(input_data)
    return model.predict(input_array).tolist()