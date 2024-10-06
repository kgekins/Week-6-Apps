import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height (m):", min_value=0.0, format="%.2f")

# Calculate BMI
if weight > 0 and height > 0:
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

else:
    st.write("Please enter valid weight and height.")