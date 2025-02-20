import streamlit as st
from streamlit_option_menu import option_menu
import importlib

# Set the page configuration
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

#
st.markdown(
    """
    <style>
    .st-emotion-cache-79elbk {
        display: none;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Create empty space for centering the logo
st.empty()

# Display the logo centered
st.image("aranademi.png", width=200, use_container_width='auto')



# Use option_menu for navigation
#with st.sidebar:
selected = option_menu(
        "",
        ["About Us",  "App STEM","Donasi"],
        icons=["caret-right-fill", "caret-right-fill", "cash-coin"],
        menu_icon="cast",
        default_index=0, orientation="horizontal",
        styles={
                "container": {"padding": "5!important", "background-color": "#d7f1fc"},
                "icon": {"color": "orange", "font-size": "20px"}, 
                "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#13AFF0"},
                "nav-link-selected": {"background-color": "#13AFF0"},
                }
    )


# Dynamically load and display the content of the selected page
if selected == "About Us":
    about_us = importlib.import_module("pages.about_us")  # Import about_us.py
    about_us.show_page()  # Call the show_page() function from about_us.py

elif selected == "App STEM":
        submenu = option_menu(
            "", 
            ["Matematika", "Fisika", "Kimia", "Biologi"], 
            menu_icon="file-earmark-text", 
            default_index=0, 
            orientation="horizontal"
        )
        if submenu ==  "Matematika":
            matematika = importlib.import_module("pages.matematika")  # Import matematika.py
            matematika.show_page()  # Call the show_page() function from matematika.py
        
        elif submenu == "Fisika":
            fisika = importlib.import_module("pages.fisika")  # Import fisika.py
            fisika.show_page()  # Call the show_page() function from fisika.py
        
        elif submenu == "Kimia":
            kimia = importlib.import_module("pages.kimia")  # Import kimia.py
            kimia.show_page()  # Call the show_page() function from kimia.py
        
        elif submenu == "Biologi":
            biologi = importlib.import_module("pages.biologi")  # Import biologi.py
            biologi.show_page()  # Call the show_page() function from biologi.py

elif selected == "Donasi":
    donasi = importlib.import_module("pages.donasi")  # Import donasi.py
    donasi.show_page()  # Call the show_page() function from donasi.py
