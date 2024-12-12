import streamlit as st

st.header('st.latex')

st.subheader('Teorema Pythagoras')
st.latex(r'c^2 = a^2 + b^2')

st.subheader('Rumus Relativitas Einstein')
st.latex(r'E = mc^2')

st.subheader('Persamaan Maxwell (Divergensi Medan Listrik)')
st.latex(r'\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}')

st.subheader('Persamaan Maxwell (Divergensi Medan Magnet)')
st.latex(r'\nabla \cdot \mathbf{B} = 0')
