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

    # Cek jika ada nilai yang hilang dan mengisi dengan nilai rata-rata
    if df.isnull().sum().any():
        st.warning("Terdapat nilai yang hilang dalam data. Nilai yang hilang akan diisi dengan rata-rata.")
        df = df.fillna(df.mean())

    # Step 4: Encode target kolom jika diperlukan (misalnya 'Species' adalah string)
    if df['Species'].dtype == 'object':  # Asumsi target kolom bernama 'Species'
        le = LabelEncoder()
        df['Species'] = le.fit_transform(df['Species'])
    
    # Step 5: Pisahkan data menjadi fitur (X) dan target (y)
    X = df.drop(columns=['Species'])  # Fitur (X)
    y = df['Species']  # Target (y)

    # Step 6: Pisahkan data menjadi data pelatihan dan pengujian
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 7: Inisialisasi dan latih model Decision Tree
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Step 8: Prediksi dan evaluasi model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Step 9: Tampilkan hasil evaluasi
    st.subheader(f'Hasil Evaluasi Model')
    st.write(f'Akurasi model: {accuracy:.2f}')
    
    # Step 10: Visualisasi pohon keputusan (optional)
    from sklearn.tree import plot_tree
    import matplotlib.pyplot as plt

    st.subheader('Visualisasi Pohon Keputusan')
    fig, ax = plt.subplots(figsize=(10, 8))
    plot_tree(model, filled=True, feature_names=X.columns, class_names=le.classes_, ax=ax)
    st.pyplot(fig)

else:
    st.write("Silakan upload file CSV yang berisi data dengan kolom 'Species' sebagai target.")
