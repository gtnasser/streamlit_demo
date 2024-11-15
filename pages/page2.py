import streamlit as st

st.session_state.Page2count = 1 + (st.session_state.get('Page2count') or 0)

st.header('Page 2')

st.subheader('Page content here')

st.write(':red[session_state]:',st.session_state)
