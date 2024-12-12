import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'Apa hewan peliharaan yang anda miliki?',
     ('Kucing', 'Anjing', 'Kelinci, 'Ayam'))

st.write('Hewan peliharaan yang saya miliki adalah ', option)
