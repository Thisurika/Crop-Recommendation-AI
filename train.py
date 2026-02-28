# train.py
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load preprocessed data
X_train_scaled = joblib.load('X_train_scaled.pkl')
y_train = joblib.load('y_train.pkl')

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Save the trained model
joblib.dump(model, 'crop_model.pkl')

print("Model trained and saved!")