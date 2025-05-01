# ⚡ AI-Based Smart Grid Optimization for Renewable Energy Management

This project uses AI to forecast solar power generation and electricity load, enabling smart grid optimization using machine learning models.

## 🚀 Features

- 🔋 Predict **solar energy output** from environmental data
- ⚡ Forecast **electricity load demand**
- 🧠 Uses **XGBoost** and **Random Forest** models
- 🌐 Provides a **Flask API** for integration
- ✅ Easy to set up, train, and deploy

## 🧱 Project Structure

```
ai_smart_grid_project/
├── app.py
├── train_models.py
├── solar_forecast.py
├── load_forecast.py
├── sample_input.json
├── requirements.txt
└── models/
```

## 🛠️ Setup Instructions

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Train the models:

```
python train_models.py
```

3. Start the Flask server:

```
python app.py
```

4. Use Postman or curl to POST to:

- `/predict/solar`
- `/predict/load`

## 📦 Sample Input

```json
[[0.9, 0.3, 0.2], [0.5, 0.6, 0.4]]
```

## 📌 Future Enhancements

- Real-time IoT data integration
- Web dashboard for live analytics
- Storage & battery control integration