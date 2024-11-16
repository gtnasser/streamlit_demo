""" TODO: docstring """
import time
import streamlit as st
import auth

st.header('Page2 is available to :red[all logged users]')

def goto_page(pagename, seconds):
    """ TODO: docstring """
    w = st.empty()
    for s in range(seconds,0,-1):
        w.write(f"This page will be redirected in **:red[{s}]** seconds.")
        time.sleep(1)
    st.switch_page(pagename)

# validate session role
if not auth.valid():
    st.error('**Role status**: You are currently not logged.')
    st.image('img/access-0.png')
    goto_page('app.py', 5)

# show page content
st.success(f'**Role status**: You are currently logged as **{auth.get_role()}**.')
st.image('img/access-1.png')
st.write('The content of this page is just visible by logged users.')
