import streamlit as st

# Title and Header
st.title("Basic Streamlit App")
st.header("A Simple Example to Get Started")

# Sidebar Input
st.sidebar.header("User Input")
name = st.sidebar.text_input("Enter your name:", value="Guest")
age = st.sidebar.number_input("Enter your age:", min_value=0, max_value=120, value=25)
favorite_number = st.sidebar.slider("Pick a favorite number:", min_value=1, max_value=100, value=50)

# Main Section
st.subheader("Greetings!")
st.write(f"Hello, **{name}**! 👋")
st.write(f"At age {age}, your favorite number is {favorite_number}. How cool is that?")

# Perform a Simple Calculation
squared = favorite_number ** 2
st.write(f"Did you know? Your favorite number squared is **{squared}**!")

# Footer
st.text("Enjoy exploring Streamlit!")
