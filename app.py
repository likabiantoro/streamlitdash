import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Set title for the app
st.title('Dashboard Klasifikasi dengan Decision Tree')

# Step 1: Upload CSV file
st.header('1. Upload Data CSV')
uploaded_file = st.file_uploader("Pilih file CSV", type="csv")

if uploaded_file is not None:
    # Step 2: Read the CSV and display it
    df = pd.read_csv(uploaded_file)

    # Step 3: Display the first few rows and column names
    st.subheader('Tabel Data')
    st.dataframe(df.head())

    # Step 4: Menampilkan informasi tentang data
    st.subheader('Informasi Data')
    st.write(df.info())

    # Step 5: Menampilkan statistik deskriptif data
    st.subheader('Statistik Deskriptif')
    st.write(df.describe())

    # Step 6: Memilih fitur dan target untuk klasifikasi
    st.header('2. Pilih Fitur dan Target')
    target_column = st.selectbox('Pilih kolom target', df.columns)
    feature_columns = st.multiselect('Pilih kolom fitur', df.columns, default=df.columns.tolist()[:-1])

    if target_column and feature_columns:
        # Step 7: Memisahkan data menjadi fitur dan target
        X = df[feature_columns]
        y = df[target_column]

        # Step 8: Membagi data menjadi data pelatihan dan data pengujian
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Step 9: Membuat model Decision Tree
        model = DecisionTreeClassifier(random_state=42)
        model.fit(X_train, y_train)

        # Step 10: Prediksi dan evaluasi
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # Step 11: Menampilkan hasil evaluasi
        st.subheader('Hasil Evaluasi Model')
        st.write(f'Akurasi Model: {accuracy * 100:.2f}%')

        # Menampilkan classification report
        st.subheader('Classification Report')
        st.text(classification_report(y_test, y_pred))

        # Menampilkan confusion matrix
        st.subheader('Confusion Matrix')
        cm = confusion_matrix(y_test, y_pred)
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=model.classes_, yticklabels=model.classes_)
        ax.set_xlabel('Prediksi')
        ax.set_ylabel('Aktual')
        ax.set_title('Confusion Matrix')
        st.pyplot(fig)

else:
    st.write("Silakan upload file CSV yang berisi data untuk klasifikasi.")
