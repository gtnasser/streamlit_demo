import streamlit as st

st.session_state.Page1count = 1 + (st.session_state.get('Page1count') or 0)

st.header('Page 1')

st.subheader('Page content here')

st.write(':red[session_state]:',st.session_state)
