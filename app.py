import streamlit as st

st.set_page_config(layout="wide")

st.title('Cara Menata Aplikasi Streamlit Anda')

with st.expander('Tentang aplikasi ini'):
  st.write('Aplikasi ini menunjukkan berbagai cara untuk menata aplikasi Streamlit Anda.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('Siapa nama Anda?')
user_emoji = st.sidebar.selectbox('Bagaimana perasaan anda saat ini?', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('Apa makanan favorit Anda?', ['', 'Nasi Goreng', 'Sate', 'Rendang', 'Bakso', 'Gado-Gado', 'Nasi Uduk'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Halo {user_name}!')
  else:
    st.write('👈  Silakan masukkan **nama** anda!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} Perasaan anda hari ini adalah **emoji**')
  else:
    st.write('👈 Silakan pilih **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** adalah makanan **favorit** anda !')
  else:
    st.write('👈 Silakan pilih makanan **favorit** Anda!')
