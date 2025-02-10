import streamlit as st
import page1
import page2

# Set page configuration to always be mobile-sized
st.set_page_config(layout="centered")

# Create buttons for navigation
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Home"):
        selected = "Home"
with col2:
    if st.button("Page 1"):
        selected = "Page 1"
with col3:
    if st.button("Page 2"):
        selected = "Page 2"

# Default selected page is "Home"
if 'selected' not in locals():
    selected = "Home"

# Navigation logic
if selected == "Home":
    st.title("Welcome to the Home Page")
    st.write("This is the home page of the Streamlit app.")
    home.app()  # Call the home app function
elif selected == "Page 1":
    st.title("Welcome to Page 1")
    st.write("This is Page 1 of the Streamlit app.")
    page1.app()  # Call the page1 app function
elif selected == "Page 2":
    st.title("Welcome to Page 2")
    st.write("This is Page 2 of the Streamlit app.")
    page2.app()  # Call the page2 app function
