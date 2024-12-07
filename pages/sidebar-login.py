""" TODO: docstring """
import streamlit as st
import auth
import sidebar_login

sidebar_login.sidebar_login()

st.subheader('Sidebar Login Simulator')
st.write(f':blue[Auth: valid=:orange[{auth.isvalid_role()}] - role=:orange[\'{auth.get_role()}\'] - user=:orange[{auth.get_user()}]]')
