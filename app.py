import streamlit as st
import auth

st.session_state.app_counter = 1 + (st.session_state.get('app_counter') or 0)
st.write(f':blue[Main Page Counter: {st.session_state.app_counter}]')

st.header('Demo Streamlit App')

st.markdown('''
This is my project powered by [Streamlit :streamlit:](https://streamlit.io/).

The main goal is FUN, despite the learning of Streamlit Framework.

Full repo project in my [Github](https://github.com/gtnasser/streamlit_demo.git)
''')

st.write("")

st.markdown('''
### Features

* multipage
* user role session

''')
