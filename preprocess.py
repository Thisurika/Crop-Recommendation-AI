# preprocess.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib  # For saving scalers and encoders

# Load dataset
df = pd.read_csv('Crop_recommendation.csv')

# Features and target
X = df.drop('label', axis=1)  # Features: N, P, K, temperature, humidity, ph, rainfall
y = df['label']  # Target: crop name

# Encode labels (crops) to numbers
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split data: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Scale features (important for ML models)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save preprocessed data, scaler, and encoder for later use
joblib.dump(X_train_scaled, 'X_train_scaled.pkl')
joblib.dump(X_test_scaled, 'X_test_scaled.pkl')
joblib.dump(y_train, 'y_train.pkl')
joblib.dump(y_test, 'y_test.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')

print("Preprocessing done! Data split and scaled.")