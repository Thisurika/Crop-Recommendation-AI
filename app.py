# app.py (Flask backend)
from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model, scaler, and encoder
model = joblib.load('crop_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    features = [
        float(request.form['N']),
        float(request.form['P']),
        float(request.form['K']),
        float(request.form['temperature']),
        float(request.form['humidity']),
        float(request.form['ph']),
        float(request.form['rainfall'])
    ]
    
    # Scale and predict
    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled)
    crop = label_encoder.inverse_transform(prediction)[0]
    
    return jsonify({'crop': crop})

if __name__ == '__main__':
    app.run(debug=True)