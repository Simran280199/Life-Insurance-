import streamlit as st
import pandas as pd
import joblib

# load trained model
model = joblib.load("insurance_model.pkl")

st.title("Medical Insurance Cost Prediction")

# user inputs
age = st.slider("Age", 18, 65)
bmi = st.slider("BMI", 15.0, 50.0)
children = st.slider("Number of Children", 0, 5)

sex = st.selectbox("Sex", ["male","female"])
smoker = st.selectbox("Smoker", ["yes","no"])
region = st.selectbox("Region", ["northwest","southeast","southwest","northeast"])

# encoding inputs
sex_male = 1 if sex == "male" else 0
smoker_yes = 1 if smoker == "yes" else 0

region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

input_data = pd.DataFrame([[
    age,
    bmi,
    children,
    sex_male,
    smoker_yes,
    region_northwest,
    region_southeast,
    region_southwest
]], columns=[
    'age','bmi','children','sex_male','smoker_yes',
    'region_northwest','region_southeast','region_southwest'
])

# prediction
if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: ${prediction[0]:.2f}")