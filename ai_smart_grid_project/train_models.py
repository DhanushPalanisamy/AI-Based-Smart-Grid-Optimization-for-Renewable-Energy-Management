import pandas as pd
import numpy as np
import joblib
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import os

# Generate synthetic dataset
X = np.random.rand(100, 3)  # Features: [temperature, humidity, wind_speed]
y_solar = X[:, 0] * 100
y_load = X[:, 0] * 50 + X[:, 1] * 20

X_train, X_test, y_train_solar, _ = train_test_split(X, y_solar, test_size=0.2)
_, _, y_train_load, _ = train_test_split(X, y_load, test_size=0.2)

# Train models
solar_model = XGBRegressor()
load_model = RandomForestRegressor()

solar_model.fit(X_train, y_train_solar)
load_model.fit(X_train, y_train_load)

# Save models
os.makedirs("models", exist_ok=True)
joblib.dump(solar_model, "models/solar_model.pkl")
joblib.dump(load_model, "models/load_model.pkl")

print("✅ Models trained and saved in 'models/' folder.")