import streamlit as st

def show_page():
    url ='https://saweria.co/AranademiApp'
    st.title("Dukungan Anda")
    st.write("Dukungan anda kami perlukan!")
    st.write("Here we will discuss donasi concepts.")
    st.markdown(f'<a href="{url}" target="_blank" style="background-color: #008CBA; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 4px;">Donate</a>', unsafe_allow_html=True)


