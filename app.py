import streamlit as st

st.title('Tema Aplikasi Streamlit')

st.write('Berikut isi dari file `.streamlit/config.toml`:')

st.code("""
[theme]
primaryColor="#00008B"
backgroundColor="#00008B"
secondaryBackgroundColor="#2F4F4F"
textColor="#FFFF00"
font="sans serif"
""")

number = st.sidebar.slider('Pilih angka:', 0, 10, 5)
st.write('Angka yang dipilih adalah:', number)
