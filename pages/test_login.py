""" TODO: docstring """
import streamlit as st
import auth

import login
login.sidebar()

login.sidebar3()

st.subheader('Login Simulator')
st.write(f':orange[Auth valid:{auth.valid()} - role:\'{auth.get_role()}\' - user:\'{auth.get_user()}\']')
