import streamlit as st
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

# Set title for the app
st.title('Dashboard Regresi Linier Berganda')

# Step 1: Upload CSV file
st.header('1. Upload Data CSV')
uploaded_file = st.file_uploader("Pilih file CSV", type="csv")

if uploaded_file is not None:
    # Step 2: Read and display the uploaded CSV
    df = pd.read_csv(uploaded_file)
    st.subheader('Tabel Data')
    st.dataframe(df)

    # Step 3: Check if Y and X variables are available
    if 'Y' in df.columns:
        # Identifikasi variabel Y (target) dan X (predictors)
        X_columns = [col for col in df.columns if col != 'Y']
        X = df[X_columns]
        Y = df['Y']
        
        # Step 4: Add constant to the X variables (for intercept in regression)
        X = sm.add_constant(X)

        # Step 5: Fit the regression model
        model = sm.OLS(Y, X).fit()

        # Step 6: Display regression results
        st.subheader('Hasil Regresi Linier Berganda')
        st.write(model.summary())

        # Step 7: Prediksi dan visualisasi hasil regresi
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
