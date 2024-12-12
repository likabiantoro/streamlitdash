import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set title for the app
st.title('Dashboard Analisis Statistika Deskriptif')

# Step 1: Upload CSV file
st.header('1. Upload Data CSV')
uploaded_file = st.file_uploader("Pilih file CSV", type="csv")

if uploaded_file is not None:
    # Step 2: Read and display the uploaded CSV
    df = pd.read_csv(uploaded_file)
    st.subheader('Tabel Data')
    st.dataframe(df)

    # Step 3: Display descriptive statistics
    st.subheader('Statistik Deskriptif')
    st.write(df.describe())

    # Step 4: Create Boxplot for each numeric column
    st.subheader('Boxplot')
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_columns) > 0:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=df[numeric_columns], ax=ax)
        st.pyplot(fig)
    else:
        st.write("Tidak ada kolom numerik untuk ditampilkan pada boxplot.")

    # Step 5: Create Bar Chart for categorical data (if any)
    st.subheader('Bar Chart')
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    if len(categorical_columns) > 0:
        for column in categorical_columns:
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.countplot(data=df, x=column, ax=ax)
            st.pyplot(fig)
    else:
        st.write("Tidak ada kolom kategorikal untuk ditampilkan pada bar chart.")
else:
    st.write("Silakan upload file CSV untuk analisis.")
