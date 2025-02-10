import streamlit as st

# Set page configuration for mobile-friendly layout
st.set_page_config(layout="centered")

# Create a horizontal sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is a horizontal sidebar.")

# Main page content
st.title("Main Page")
st.write("Welcome to the main page!")

# Add some widgets to the sidebar
option = st.sidebar.selectbox(
    'Select an option:',
    ['Option 1', 'Option 2', 'Option 3']
)

st.sidebar.write('You selected:', option)
