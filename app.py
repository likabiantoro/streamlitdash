import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

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

    # Cek jika ada nilai yang hilang dan mengisi dengan nilai rata-rata untuk kolom numerik
    if df.isnull().sum().any():
        st.warning("Terdapat nilai yang hilang dalam data.")
        
        # Isi nilai yang hilang untuk kolom numerik dengan rata-rata
        for column in df.select_dtypes(include=['float64', 'int64']).columns:
            df[column] = df[column].fillna(df[column].mean())
        
        # Isi nilai yang hilang untuk kolom non-numerik dengan mode
        for column in df.select_dtypes(include=['object']).columns:
            df[column] = df[column].fillna(df[column].mode()[0])

    # Step 4: Pastikan kolom target ada, misalnya 'Species' adalah kolom target
    target_column = 'Species'  # Sesuaikan dengan nama kolom target yang benar
    if target_column not in df.columns:
        st.error(f"Kolom target '{target_column}' tidak ditemukan dalam data.")
    else:
        # Step 5: Encode target kolom jika diperlukan (misalnya 'Species' adalah string)
        if df[target_column].dtype == 'object':  # Asumsi target kolom bernama 'Species'
            le = LabelEncoder()
            df[target_column] = le.fit_transform(df[target_column])

        # Step 6: Pisahkan data menjadi fitur (X) dan target (y)
        X = df.drop(columns=[target_column])  # Fitur (X)
        y = df[target_column]  # Target (y)

        # Step 7: Pisahkan data menjadi data pelatihan dan pengujian
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Step 8: Inisialisasi dan latih model Decision Tree
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)

        # Step 9: Prediksi dan evaluasi model
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # Step 10: Tampilkan hasil evaluasi
        st.subheader(f'Hasil Evaluasi Model')
        st.write(f'Akurasi model: {accuracy:.2f}')
        
        # Step 11: Visualisasi pohon keputusan (optional)
        from sklearn.tree import plot_tree
        import matplotlib.pyplot as plt

        st.subheader('Visualisasi Pohon Keputusan')
        fig, ax = plt.subplots(figsize=(10, 8))
        plot_tree(model, filled=True, feature_names=X.columns, class_names=le.classes_, ax=ax)
        st.pyplot(fig)

else:
    st.write("Silakan upload file CSV yang berisi data dengan kolom target seperti 'Species'.")
