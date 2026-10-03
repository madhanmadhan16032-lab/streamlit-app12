import streamlit as st

st.title("My First App")
st.header("this is my  first mobile application")

name = st.text_input("Enter your name")
age = st.number_input("enter your age ")


if st.button("Submit"):
    st.success(f"Hello {name}! your age {age}")
