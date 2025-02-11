
import streamlit as st
from streamlit_option_menu import option_menu
import importlib

# Mengatur konfigurasi halaman agar selalu berukuran mobile
st.set_page_config(layout="centered")
st.sidebar.empty()

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):  # Menambahkan self di sini
        with st.sidebar:
            app = option_menu(
                menu_title='Aranademi ',
                options=['About Us', 'Biologi', 'Fisika', 'Matematika', 'Kimia', 'Donasi'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        # Dinamis mengimpor dan menjalankan halaman yang dipilih
        if app:
            try:
                # Mengubah nama halaman menjadi format file (misal "Biologi" menjadi "biologi.py")
                page_module = importlib.import_module(f"pages.{app.lower()}")  # Memastikan nama file sesuai
                page_module.app()  # Memanggil fungsi 'app()' di dalam halaman
            except ModuleNotFoundError:
                st.error(f"Halaman {app} tidak ditemukan!")
                

# Menjalankan aplikasi
if __name__ == '__main__':
    app = MultiApp()
    app.run()
