import streamlit as st
from streamlit_option_menu import option_menu
import importlib

# Set the page configuration
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# Hide the sidebar using custom CSS
st.markdown("""
    <style>
        /* Hide the Streamlit sidebar */
        .css-1d391kg {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Use option_menu for navigation
selected = option_menu(
    "Main Menu",
    ["About Us", "Matematika", "Fisika", "Kimia", "Biologi", "Donasi"],
    icons=["info-circle", "calculator", "atom", "flask", "leaf", "donate"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",  # Set to horizontal
)

# Dynamically load and display the content of the selected page
if selected == "About Us":
    about_us = importlib.import_module("about_us")  # Import about_us.py
    about_us.show_page()  # Call the show_page() function from about_us.py

elif selected == "Matematika":
    matematika = importlib.import_module("matematika")  # Import matematika.py
    matematika.show_page()  # Call the show_page() function from matematika.py

elif selected == "Fisika":
    fisika = importlib.import_module("fisika")  # Import fisika.py
    fisika.show_page()  # Call the show_page() function from fisika.py

elif selected == "Kimia":
    kimia = importlib.import_module("kimia")  # Import kimia.py
    kimia.show_page()  # Call the show_page() function from kimia.py

elif selected == "Biologi":
    biologi = importlib.import_module("biologi")  # Import biologi.py
    biologi.show_page()  # Call the show_page() function from biologi.py

elif selected == "Donasi":
    donasi = importlib.import_module("donasi")  # Import donasi.py
    donasi.show_page()  # Call the show_page() function from donasi.py
