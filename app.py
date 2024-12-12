import streamlit as st

st.header('st.checkbox')

st.write('Apa aktivitas yang Anda sukai?')

membaca = st.checkbox('Membaca')
bepergian = st.checkbox('Bepergian')
bersepeda = st.checkbox('Bersepeda')

if membaca:
    st.write("Luar biasa! Membaca memperluas wawasan Anda 📚")

if bepergian:
    st.write("Hebat! Bepergian memperluas cakrawala Anda ✈️")

if bersepeda:
    st.write("Pilihan yang bagus! Bersepeda membuat Anda tetap sehat dan bugar 🚴")
