import streamlit as st

st.title('st.session_state')

def meters_to_cm():
    st.session_state.cm = st.session_state.meters * 100

def cm_to_meters():
    st.session_state.meters = st.session_state.cm / 100

st.header('Input')
col1, spacer, col2 = st.columns([2, 1, 2])
with col1:
    meters = st.number_input("Meter:", key="meters", on_change=meters_to_cm)
with col2:
    cm = st.number_input("Sentimeter:", key="cm", on_change=cm_to_meters)

st.header('Output')
st.write("Objek st.session_state:", st.session_state)
