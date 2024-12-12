import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
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

    # Menghilangkan warning dan langsung mengisi nilai yang kosong dengan rata-rata
    # Isi nilai yang hilang untuk kolom numerik dengan rata-rata
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        df[column] = df[column].fillna(df[column].mean())
    
    # Isi nilai yang hilang untuk kolom non-numerik dengan mode (opsional)
    for column in df.select_dtypes(include=['object']).columns:
        df[column] = df[column].fillna(df[column].mode()[0])

    # Pastikan kolom 'Species' adalah string atau kategori
    df['Species'] = df['Species'].astype(str).str.strip()  # Menghapus spasi pada string

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

    # Confusion matrix untuk menghitung sensitivitas dan spesifisitas
    cm = confusion_matrix(y_test, y_pred)

    # Menangani kasus dengan lebih dari dua kelas
    tp = cm.diagonal().sum()  # Total True Positive (untuk semua kelas)
    fn = cm.sum(axis=1) - cm.diagonal()  # Total False Negative
    fp = cm.sum(axis=0) - cm.diagonal()  # Total False Positive
    tn = cm.sum() - (tp + fn.sum() + fp.sum())  # Total True Negative

    # Menghitung sensitivitas dan spesifisitas keseluruhan
    sensitivity = (tp / (tp + fn.sum())) * 100 if (tp + fn.sum()) > 0 else 0  # Sensitivitas total dalam persen
    specificity = (tn / (tn + fp.sum())) * 100 if (tn + fp.sum()) > 0 else 0  # Spesifisitas total dalam persen

    # Step 9: Tampilkan hasil evaluasi
    st.subheader(f'Hasil Evaluasi Model')
    st.write(f'Akurasi model: {accuracy:.2f}%')
    st.write(f'Sensitivitas keseluruhan: {sensitivity:.2f}%')
    st.write(f'Spesifisitas keseluruhan: {specificity:.2f}%')
    
    # Step 10: Visualisasi pohon keputusan (optional)
    from sklearn.tree import plot_tree
    import matplotlib.pyplot as plt

    st.subheader('Visualisasi Pohon Keputusan')
    fig, ax = plt.subplots(figsize=(10, 8))
    plot_tree(model, filled=True, feature_names=X.columns, class_names=le.classes_, ax=ax)
    st.pyplot(fig)

else:
    st.write("Silakan upload file CSV yang berisi data dengan kolom 'Species' sebagai target.")
