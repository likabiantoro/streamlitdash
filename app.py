import streamlit as st
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

# Judul dashboar
st.title('Dashboard Regresi Linier Berganda')

# Step 1: Upload file CSV
st.header('1. Upload Data CSV')
uploaded_file = st.file_uploader("Pilih file CSV", type="csv")

if uploaded_file is not None:
    # Step 2: Tabel Data
    df = pd.read_csv(uploaded_file)
    st.subheader('Tabel Data')
    st.dataframe(df)

    # Step 3: Cek apakah data Y dan X tersedia
    if 'Y' in df.columns:
        # Identifikasi variabel Y (respon) dan X (prediktor)
        X_columns = [col for col in df.columns if col != 'Y']
        X = df[X_columns]
        Y = df['Y']
        X = sm.add_constant(X)

        # Step 4: Fit model regresi
        model = sm.OLS(Y, X).fit()

        # Step 5: Hasil regresi
        st.subheader('Hasil Regresi Linier Berganda')
        st.write(model.summary())

        # Step 6: Prediksi dan visualisasi hasil regresi
        predictions = model.predict(X)

        st.subheader('Visualisasi Regresi Linier')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.regplot(x=Y, y=predictions, ax=ax, scatter_kws={'s': 10}, line_kws={'color': 'red'})
        ax.set_xlabel('Nilai Aktual Y')
        ax.set_ylabel('Prediksi Y')
        ax.set_title('Prediksi vs Nilai Aktual')
        st.pyplot(fig)

else:
    st.write("Silakan upload file CSV yang berisi data Y dan X1, X2, X3, ...")
