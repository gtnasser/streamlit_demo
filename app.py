import streamlit as st

st.session_state.Appcount = 1 + (st.session_state.get('Appcount') or 0)

st.header('app.py - Main Page')

st.subheader('Page content here')

st.write(':red[session_state]:',st.session_state)
