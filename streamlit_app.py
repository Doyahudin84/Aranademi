
import streamlit as st

# Set page configuration to always be mobile-sized
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# Tambahkan CSS untuk efek hover dan gambar responsif
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
            <img class="nav-img" src="images/fisika.jpg" alt="Fisika" width="150">
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

# Simulasi halaman berdasarkan URL hash
page = st.experimental_get_query_params().get("page", ["Home"])[0]

# Tampilkan konten halaman sesuai dengan pemilihan
if page == "Home":
    st.title("Selamat datang di Halaman Home")
    st.write("Ini adalah halaman utama dari aplikasi Streamlit.")
elif page == "Fisika":
    st.title("Selamat datang di Halaman Fisika")
    st.write("Ini adalah halaman Fisika dari aplikasi Streamlit.")
elif page == "Kimia":
    st.title("Selamat datang di Halaman Kimia")
    st.write("Ini adalah halaman Kimia dari aplikasi Streamlit.")
elif page == "Biologi":
    st.title("Selamat datang di Halaman Biologi")
    st.write("Ini adalah halaman Biologi dari aplikasi Streamlit.")
elif page == "Donasi":
    st.title("Selamat datang di Halaman Donasi")
    st.write("Ini adalah halaman Donasi dari aplikasi Streamlit.")
