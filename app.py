import streamlit as st

st.header('st.multiselect')
# opsi yang dapat dipilih
options = st.multiselect(
     'Apa hewan peliharaan yang anda miliki',
     ['Kucing', 'Anjing', 'Kelinci', 'Ayam'],
     ['Kucing', 'Anjing']) # tampilan default

st.write('Hewan peliharaan yang saya miliki adalah ', options)
