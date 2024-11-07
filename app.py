import streamlit as st

# Add a header and text
st.header('Getting Started with Streamlit')
st.write("This app will help you explore basic Streamlit components.")

# Add a slider
age = st.slider('Select your age:', 0, 100, 25)
st.write(f"Your selected age is: {age}")

# Add a text input
name = st.text_input('Enter your name:')
if name:
    st.write(f"Hello, {name}!")
