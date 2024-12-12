import streamlit as st
import pandas as pd
import numpy as np

# Header untuk Line Chart
st.header('Line Chart')

# Data untuk Line Chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

# Menampilkan Line Chart
st.line_chart(chart_data)

# Spacer untuk pemisahan visual
st.write("---")

# Header untuk Bar Chart
st.header('Bar Chart')

# Data untuk Bar Chart
bar_chart_data = pd.DataFrame(
     np.random.randn(10, 3),
     columns=['x', 'y', 'z'])

# Menampilkan Bar Chart
st.bar_chart(bar_chart_data)
