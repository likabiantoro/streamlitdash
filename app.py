import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# Set title for the app
st.title('Dashboard Analisis Time Series dengan ARIMA')

# Step 1: Upload CSV file
st.header('1. Upload Data CSV')
uploaded_file = st.file_uploader("Pilih file CSV", type="csv")

if uploaded_file is not None:
    # Step 2: Read the CSV and display it
    df = pd.read_csv(uploaded_file)

    # Step 3: Display the first few rows and column names
    st.subheader('Tabel Data')
    st.dataframe(df.head())

    # Step 4: Kolom waktu harus diubah menjadi datetime
    # Pastikan file CSV memiliki kolom dengan format waktu
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])

        # Pilih kolom waktu dan nilai (misal: kolom 'Date' dan 'Value')
        st.subheader('Visualisasi Data Time Series')
        st.line_chart(df.set_index('Date')['Value'])

        # Step 5: Pilih parameter ARIMA (p, d, q)
        st.header('2. Pilih Parameter ARIMA (p, d, q)')
        p = st.slider("Pilih p (AR order)", 0, 5, 1)
        d = st.slider("Pilih d (differencing order)", 0, 2, 1)
        q = st.slider("Pilih q (MA order)", 0, 5, 1)

        # Step 6: Memisahkan data menjadi data pelatihan dan data pengujian
        train_size = int(len(df) * 0.8)
        train, test = df['Value'][:train_size], df['Value'][train_size:]

        # Step 7: Membuat model ARIMA dan melakukan prediksi
        model = ARIMA(train, order=(p, d, q))
        model_fit = model.fit()

        # Prediksi pada data pengujian
        predictions = model_fit.forecast(steps=len(test))

        # Step 8: Visualisasi hasil prediksi dan data aktual
        st.subheader('Hasil Prediksi ARIMA')
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df['Date'][:train_size], train, label='Data Pelatihan')
        ax.plot(df['Date'][train_size:], test, label='Data Pengujian', color='orange')
        ax.plot(df['Date'][train_size:], predictions, label='Prediksi ARIMA', color='red')
        ax.set_xlabel('Waktu')
        ax.set_ylabel('Nilai')
        ax.set_title(f'Prediksi ARIMA (p={p}, d={d}, q={q})')
        ax.legend()
        st.pyplot(fig)

        # Step 9: Menampilkan metrik evaluasi
        mse = mean_squared_error(test, predictions)
        st.subheader('Metrik Evaluasi')
        st.write(f'Mean Squared Error (MSE): {mse}')

else:
    st.write("Silakan upload file CSV yang berisi data time series dengan kolom 'Date' dan 'Value'.")
