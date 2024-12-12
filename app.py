import streamlit as st

st.title('st.form')

# Contoh lengkap menggunakan notasi `with`
st.header('1. Contoh penggunaan notasi `with`')
st.subheader('Pesan Makanan')

with st.form('my_form'):
    st.subheader('**Pesan Makanan Anda**')

    # Input widget
    makanan_val = st.selectbox('Pilih makanan', ['Nasi Goreng', 'Sate', 'Rendang', 'Bakso', 'Gado-Gado'])
    minuman_val = st.selectbox('Pilih minuman', ['Es Teh', 'Es Jeruk', 'Air Putih', 'Kopi', 'Jus Mangga'])
    porsi_val = st.select_slider('Ukuran porsi', ['Kecil', 'Sedang', 'Besar'])
    pedas_val = st.select_slider('Tingkat kepedasan', ['Tidak Pedas', 'Sedikit Pedas', 'Pedas', 'Sangat Pedas'])
    toping_val = st.checkbox('Telur','Sambal','Kerupuk')

    # Setiap form harus memiliki tombol kirim
    submitted = st.form_submit_button('Kirim')

if submitted:
    st.markdown(f'''
        🍽️ Anda telah memesan:
        - Makanan: `{makanan_val}`
        - Minuman: `{minuman_val}`
        - Porsi: `{porsi_val}`
        - Kepedasan: `{pedas_val}`
        - Toping: `{toping_val}`
        ''')
else:
    st.write('☝️ Silakan pilih pesanan Anda!')


# Contoh singkat menggunakan notasi objek
st.header('2. Contoh menggunakan notasi objek')

form = st.form('my_form_2')
selected_val = form.slider('Pilih nilai')
form.form_submit_button('Kirim')

st.write('Nilai yang dipilih: ', selected_val)
