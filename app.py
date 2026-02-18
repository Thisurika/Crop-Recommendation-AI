import streamlit as st
from predict import recommend_crop_and_price

st.title("Crop Recommendation & Price Forecast AI 🌾")

N = st.number_input("Nitrogen (N)", 0.0, 200.0, 80.0)
P = st.number_input("Phosphorus (P)", 0.0, 200.0, 40.0)
K = st.number_input("Potassium (K)", 0.0, 200.0, 50.0)
temp = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0, 80.0)
ph = st.number_input("Soil pH", 0.0, 14.0, 6.5)
rainfall = st.number_input("Rainfall (mm)", 0.0, 300.0, 200.0)
season = st.selectbox("Season", ['Maha', 'Yala'])
month_start = st.selectbox("Start Month", ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
month_end = st.selectbox("End Month", ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

if st.button("Recommend Crop & Predict Price"):
    crop, price = recommend_crop_and_price(N, P, K, temp, humidity, ph, rainfall, season, month_start, month_end)
    st.success(f"Recommended Crop: **{crop}**")
    st.success(f"Average Predicted Price ({month_start} to {month_end}): **{price:.2f} LKR**")