import streamlit as st
from pages import home, fisika, kimia, biologi, donasi
print(dir(pages))
# Set page configuration to always be mobile-sized
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
    .nav-img {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        width: 100%; /* Menyesuaikan lebar gambar */
        max-width: 150px; /* Maksimal lebar 150px */
    }
    .nav-img:hover {
        transform: scale(1.1);
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }
    </style>
    """, unsafe_allow_html=True
)

# Menonaktifkan sidebar
st.sidebar.empty()

# Gambar untuk navigasi
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(
        """
        <a href="#Home">
            <img class="nav-img" src="images/home.jpg" alt="Home" width="150">
        </a>
        """, unsafe_allow_html=True)

with col2:
    st.markdown(
        """
        <a href="#Fisika">
            <img class="nav-img" src="fisika.png" alt="Fisika" width="150">
        </a>
        """, unsafe_allow_html=True)

with col3:
    st.markdown(
        """
        <a href="#Kimia">
            <img class="nav-img" src="images/kimia.jpg" alt="Kimia" width="150">
        </a>
        """, unsafe_allow_html=True)

with col4:
    st.markdown(
        """
        <a href="#Biologi">
            <img class="nav-img" src="images/biologi.jpg" alt="Biologi" width="150">
        </a>
        """, unsafe_allow_html=True)

with col5:
    st.markdown(
        """
        <a href="#Donasi">
            <img class="nav-img" src="images/donasi.jpg" alt="Donasi" width="150">
        </a>
        """, unsafe_allow_html=True)

# Default selected page is "Home"
if 'selected' not in locals():
    selected = "Home"

# Logic to handle page content display
if selected == "Home":
    st.title("Selamat datang di Halaman Home")
    st.write("Ini adalah halaman utama dari aplikasi Streamlit.")
    home.doyaapp()  # Panggil fungsi app dari pages/home.py
elif selected == "Fisika":
    st.title("Selamat datang di Halaman Fisika")
    st.write("Ini adalah halaman Fisika dari aplikasi Streamlit.")
    fisika.app()  # Panggil fungsi app dari pages/fisika.py
elif selected == "Kimia":
    st.title("Selamat datang di Halaman Kimia")
    st.write("Ini adalah halaman Kimia dari aplikasi Streamlit.")
    kimia.app()  # Panggil fungsi app dari pages/kimia.py
elif selected == "Biologi":
    st.title("Selamat datang di Halaman Biologi")
    st.write("Ini adalah halaman Biologi dari aplikasi Streamlit.")
    biologi.app()  # Panggil fungsi app dari pages/biologi.py
elif selected == "Donasi":
    st.title("Selamat datang di Halaman Donasi")
    st.write("Ini adalah halaman Donasi dari aplikasi Streamlit.")
    donasi.app()  # Panggil fungsi app dari pages/donasi.py


