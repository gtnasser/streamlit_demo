import streamlit as st

st.session_state.Appcount = 1 + (st.session_state.get('Appcount') or 0)

st.header('Demo Streamlit App')

#st.write(':red[session_state]:',st.session_state)

st.markdown('''
This is my project powered by [Streamlit :streamlit:](https://streamlit.io/).

The main goal is FUN, despite the learning of Streamlit Framework.

Full repo project in my [Github](https://github.com/gtnasser/streamlit_demo.git)


### Features

* multipage

''')