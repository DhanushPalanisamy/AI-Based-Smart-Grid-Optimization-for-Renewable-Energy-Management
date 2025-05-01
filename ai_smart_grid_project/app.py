from flask import Flask, request, jsonify
from solar_forecast import predict_solar
from load_forecast import predict_load

app = Flask(__name__)

@app.route('/predict/solar', methods=['POST'])
def solar_route():
    input_data = request.get_json()
    result = predict_solar(input_data)
    return jsonify({"solar_prediction": result})

@app.route('/predict/load', methods=['POST'])
def load_route():
    input_data = request.get_json()
    result = predict_load(input_data)
    return jsonify({"load_prediction": result})

if __name__ == '__main__':
    app.run(debug=True)