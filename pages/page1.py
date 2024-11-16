""" TODO: docstring """
import streamlit as st
import auth

st.header('Page1 is available to :red[everyone]')

# validate session role
if not auth.valid():
    st.warning('**Role status**: You are currently not logged.')
else:
    st.success(f'**Role status**: You are currently logged as **{auth.get_role()}**.')

# show page content
st.image('img/access-1.png')
st.write('The content of this page is visible by anyone, logged or not')