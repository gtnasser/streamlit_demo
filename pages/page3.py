import streamlit as st

st.session_state.Page3count = 1 + (st.session_state.get('Page3count') or 0)

st.header('Page 3')

st.subheader('Page content here')

st.write(':red[session_state]:',st.session_state)
