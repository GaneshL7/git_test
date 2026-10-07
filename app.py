import streamlit as st

st.title("Addition Program")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

if st.button("division"):
    result = num1 / num2
    st.success(f"Division = {result}")
