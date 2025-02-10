import streamlit as st

# Set page configuration to always be mobile-sized
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# Add CSS for hover effect and responsive images
st.markdown(
    """
    <style>
    .nav-img {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        width: 100%; /* Adjust image width */
        max-width: 150px; /* Max width of 150px */
    }
    .nav-img:hover {
        transform: scale(1.1);
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }
    </style>
    """, unsafe_allow_html=True
)

# Disable sidebar
st.sidebar.empty()

# Images for navigation
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(
        """
        <a href="?page=Home">
            <img class="nav-img" src="images/home.jpg" alt="Home" width="150">
        </a>
        """, unsafe_allow_html=True)

with col2:
    st.markdown(
        """
        <a href="?page=Fisika">
            <img class="nav-img" src="fisika.png" alt="Fisika" width="150">
        </a>
        """, unsafe_allow_html=True)

with col3:
    st.markdown(
        """
        <a href="?page=Kimia">
            <img class="nav-img" src="images/kimia.jpg" alt="Kimia" width="150">
        </a>
        """, unsafe_allow_html=True)

with col4:
    st.markdown(
        """
        <a href="?page=Biologi">
            <img class="nav-img" src="images/biologi.jpg" alt="Biologi" width="150">
        </a>
        """, unsafe_allow_html=True)

with col5:
    st.markdown(
        """
        <a href="?page=Donasi">
            <img class="nav-img" src="images/donasi.jpg" alt="Donasi" width="150">
        </a>
        """, unsafe_allow_html=True)

# Get query parameters using st.query_params (recommended for future compatibility)
page = st.query_params.get("page", ["Home"])[0]

# Display content based on the selected page
if page == "Home":
    st.title("Welcome to the Home Page")
    st.write("This is the main page of the Streamlit app.")
elif page == "Fisika":
    st.title("Welcome to the Fisika Page")
    st.write("This is the Fisika page of the Streamlit app.")
elif page == "Kimia":
    st.title("Welcome to the Kimia Page")
    st.write("This is the Kimia page of the Streamlit app.")
elif page == "Biologi":
    st.title("Welcome to the Biologi Page")
    st.write("This is the Biologi page of the Streamlit app.")
elif page == "Donasi":
    st.title("Welcome to the Donasi Page")
    st.write("This is the Donasi page of the Streamlit app.")
