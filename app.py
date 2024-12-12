import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'Apa hewan peliharaan yang anda miliki',
     ['Kucing', 'Anjing', 'Kelinci', 'Ayam'],
     ['Kucing', 'Anjing', 'Kelinci', 'Ayam'])

st.write('Hewan peliharaan yang saya miliki adalah ', options)
