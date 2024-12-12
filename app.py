import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Input File CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('Tabel Data')
  st.write(df)
  st.subheader('Hasil Statistika Deskriptif')
  st.write(df.describe())
else:
  st.info('Upload file CSV pada kolom di atas')
