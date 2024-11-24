""" TODO: docstring """
import streamlit as st

# count this page execution, creating session counter var at fist execution
st.session_state.app_counter = 1 if 'app_counter' not in st.session_state else st.session_state.app_counter + 1

st.write(f':blue[Main Page Counter: {st.session_state.app_counter}]')

st.header('Demo Streamlit App')

st.markdown('''
This is my Sample App powered by [Streamlit :streamlit:](https://streamlit.io/).

The main goal is FUN, despite the learning of Streamlit Framework.

Full repo project in my [Github](https://github.com/gtnasser/streamlit_demo.git)
''')

st.write("")

st.markdown('''
### Features

:heavy_check_mark: multipage

:white_large_square: user role session :ballot_box_with_check:

''')



