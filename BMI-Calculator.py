import streamlit as st

# Title
st.title("BMI Calculator")

# Input fields for weight and height
weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height (m):", min_value=0.0, format="%.2f")

# Calculate BMI
if weight > 0 and height > 0:
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    # Determine BMI category
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")
else:
    st.write("Please enter valid weight and height.")