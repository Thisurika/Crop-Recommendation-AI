# test.py
import joblib
from sklearn.metrics import accuracy_score, classification_report

# Load preprocessed test data and model
X_test_scaled = joblib.load('X_test_scaled.pkl')
y_test = joblib.load('y_test.pkl')
model = joblib.load('crop_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Predict on test set
y_pred = model.predict(X_test_scaled)

# Decode predictions back to crop names
y_test_decoded = label_encoder.inverse_transform(y_test)
y_pred_decoded = label_encoder.inverse_transform(y_pred)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print(classification_report(y_test_decoded, y_pred_decoded))