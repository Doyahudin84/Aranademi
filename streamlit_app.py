import streamlit as st

# Set page configuration to always be mobile-sized
st.set_page_config(layout="centered")

# Create a horizontal sidebar with options
selected = option_menu(
    menu_title=None,  # required
    options=["Home", "Page 1", "Page 2"],  # required
    icons=["house", "file-earmark", "file-earmark"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal",
)

# Navigation logic
if selected == "Home":
    st.title("Welcome to the Home Page")
    st.write("This is the home page of the Streamlit app.")
elif selected == "Page 1":
    st.title("Welcome to Page 1")
    st.write("This is Page 1 of the Streamlit app.")
elif selected == "Page 2":
    st.title("Welcome to Page 2")
    st.write("This is Page 2 of the Streamlit app.")
