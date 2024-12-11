# Install requirement
import streamlit as st
from datetime import time, datetime

# Membuat slider dengan fungsi st.slider
st.header('st.slider')

# Slider satu nilai
# Menampilkan sub header 'Slider satu nilai'
st.subheader('Slider satu nilai')

# Memberi label pertanyaan 'Berapa usiamu saat ini'
# 0 adalah nilai min, 100 adalah nilai max, dan 13 adalah titik awal slider
age = st.slider('Berapa usiamu saat ini?', 0, 100, 13)
st.write("Usia saya", age, 'tahun')

# Slider rentang nilai
# Menampilkan sub header 'Slider rentang nilai'
st.subheader('Slider rentang nilai')

#  50adalah nilai min, 200 adalah nilai max, dan 150-170 adalah titik awal slider
values = st.slider(
     'Berapa rentang tinggi badan anda?',
     50, 200, (150, 170)) 
st.write('Tinggi badan saya adalah', values, 'cm')

# Slider rentang waktu
# Menampilkan sub header 'Slider rentang waktu'
st.subheader('Slider rentang waktu')

# Rentang default waktu adalah 1:00 hingga 5:45
sleeptime = st.slider(
     "Pada pukul berapa anda tidur?",
     value=(time(1, 00), time(5, 45)))
st.write("Saya tidur pada pukul:", sleeptime)

# Slider tanggal dan waktu
# Menampilkan sub header 'Slider rentang tanggal dan waktu'
st.subheader('Slider tanggal dan waktu')

# Default tanggal adalah 1 Januari 2024 dan Default waktu adalah 7:30 
start_time = st.slider(
     "Kapan anda berencana untuk melakukan konsultasi ke klinik Mitra Sehat?",
     value=datetime(2024, 1, 1, 7, 30),
     format="MM/DD/YY - hh:mm")
st.write("Saya akan berkonsultasi pada", start_time)
