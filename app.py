
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    amt = request.json['amount']
    result = model.predict([[amt]])
    return jsonify({"fraud": bool(result[0])})

app.run(host='0.0.0.0', port=5000)
