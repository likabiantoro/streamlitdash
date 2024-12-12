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
    if cm.shape == (2, 2):  # Jika klasifikasi biner
        tn, fp, fn, tp = cm.ravel()  # tn: True Negative, fp: False Positive, fn: False Negative, tp: True Positive

        # Menghitung sensitivitas (recall) dan spesifisitas
        sensitivity = tp / (tp + fn)
        specificity = tn / (tn + fp)
    else:
        # Jika lebih dari dua kelas, sensitifitas dan spesifisitas per kelas
        sensitivity = {}
        specificity = {}
        for i in range(cm.shape[0]):
            tp = cm[i, i]  # True Positive per kelas
            fn = cm[i, :].sum() - tp  # False Negative per kelas
            fp = cm[:, i].sum() - tp  # False Positive per kelas
            tn = cm.sum() - (tp + fp + fn)  # True Negative per kelas

            sensitivity[i] = tp / (tp + fn) if (tp + fn) != 0 else 0
            specificity[i] = tn / (tn + fp) if (tn + fp) != 0 else 0

    # Step 9: Tampilkan hasil evaluasi
    st.subheader(f'Hasil Evaluasi Model')
    st.write(f'Akurasi model: {accuracy:.2f}')
    
    if cm.shape == (2, 2):  # Jika klasifikasi biner
        st.write(f'Sensitivitas (Recall): {sensitivity:.2f}')
        st.write(f'Spesifisitas: {specificity:.2f}')
    else:  # Jika lebih dari dua kelas
        st.write(f'Sensitivitas per kelas: {sensitivity}')
        st.write(f'Spesifisitas per kelas: {specificity}')
    
    # Step 10: Visualisasi pohon keputusan (optional)
    from sklearn.tree import plot_tree
    import matplotlib.pyplot as plt

    st.subheader('Visualisasi Pohon Keputusan')
    fig, ax = plt.subplots(figsize=(10, 8))
    plot_tree(model, filled=True, feature_names=X.columns, class_names=le.classes_, ax=ax)
    st.pyplot(fig)

else:
    st.write("Silakan upload file CSV yang berisi data dengan kolom 'Species' sebagai target.")
