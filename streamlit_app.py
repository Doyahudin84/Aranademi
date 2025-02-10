import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration for mobile-friendly layout
st.set_page_config(layout="centered")
# Create a horizontal sidebar with links to other pages
selected = option_menu(
    menu_title=None,  # required
    options=["Option 1", "Option 2", "Option 3"],  # required
    icons=["house", "gear", "envelope"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal",
)

# Navigation logic
if selected == "Option 1":
    st.write("You selected Option 1")
    # Add code to navigate to Option 1 page
elif selected == "Option 2":
    st.write("You selected Option 2")
    # Add code to navigate to Option 2 page
elif selected == "Option 3":
    st.write("You selected Option 3")
    # Add code to navigate to Option 3 page

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
# Create separate files for each option page
with open("option1.py", "w") as f:
    f.write("""

def app():
    st.title("Option 1 Page")
    st.write("Welcome to Option 1 page!")
""")

with open("option2.py", "w") as f:
    f.write("""

def app():
    st.title("Option 2 Page")
    st.write("Welcome to Option 2 page!")
""")

with open("option3.py", "w") as f:
    f.write("""

def app():
    st.title("Option 3 Page")
    st.write("Welcome to Option 3 page!")
""")
