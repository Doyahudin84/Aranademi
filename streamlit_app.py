import streamlit as st
from streamlit_option_menu import option_menu
import importlib

# Set the page configuration
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# Add custom CSS to load Font Awesome icons
st.markdown("""
    <style>
        /* Load Font Awesome */
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

        /* Hide the Streamlit sidebar */
        .css-1d391kg {
            display: none;
        }

       /* Style for the entire menu container */
        .menu {
            background-color: black !important;  /* Black background for the entire menu */
            padding: 10px 0;  /* Optional: Padding around the menu */
        }

        /* Style for each nav-item (menu item) */
        .nav-item {
            color: #07e3eb !important;  /* Text color for the menu items */
            background-color: transparent !important;  /* Transparent background by default */
            border: none !important;
            font-size: 16px !important;  /* Font size */
        }

        /* Hover effect for nav-item */
        .nav-item:hover {
            background-color: #07e3eb !important;  /* Background color on hover */
            color: white !important;  /* Text color on hover */
        }

        /* Active (selected) nav-item styling */
        .nav-item.active {
            background-color: #07e3eb !important;  /* Active background color */
            color: white !important;  /* Active text color */
        }

        /* Optional: Center the menu items horizontally */
        .menu {
            display: flex;
            justify-content: center;
        }

        /* Optional: Adjust the spacing between nav-items */
        .menu .nav-item {
            margin: 0 10px;  /* Space between menu items */
        }
    </style>
""", unsafe_allow_html=True)

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
    about_us = importlib.import_module("pages.about_us")  # Import about_us.py
    about_us.show_page()  # Call the show_page() function from about_us.py

elif selected == "Matematika":
    matematika = importlib.import_module("pages.matematika")  # Import matematika.py
    matematika.show_page()  # Call the show_page() function from matematika.py

elif selected == "Fisika":
    fisika = importlib.import_module("pages.fisika")  # Import fisika.py
    fisika.show_page()  # Call the show_page() function from fisika.py

elif selected == "Kimia":
    kimia = importlib.import_module("pages.kimia")  # Import kimia.py
    kimia.show_page()  # Call the show_page() function from kimia.py

elif selected == "Biologi":
    biologi = importlib.import_module("pages.biologi")  # Import biologi.py
    biologi.show_page()  # Call the show_page() function from biologi.py

elif selected == "Donasi":
    donasi = importlib.import_module("pages.donasi")  # Import donasi.py
    donasi.show_page()  # Call the show_page() function from donasi.py
