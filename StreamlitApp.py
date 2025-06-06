import streamlit as st
import pickle
import numpy as np

st.title("Car Price Prediction App")

# Load model
with open('car_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Input fields
year = st.number_input("Year of Manufacture", 2000, 2025, step=1)
km_driven = st.number_input("Kilometers Driven", 0, 500000, step=1000)
fuel = st.selectbox("Fuel Type", ['Petrol', 'Diesel'])
trans = st.selectbox("Transmission", ['Manual', 'Automatic'])

fuel_code = 0 if fuel == 'Petrol' else 1
trans_code = 0 if trans == 'Manual' else 1

if st.button("Predict Price"):
    features = np.array([[year, km_driven, fuel_code, trans_code]])
    price = model.predict(features)[0]
    st.success(f"Estimated Car Price: ₹{price:,.0f}")
