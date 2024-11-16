import streamlit as st
import auth
import time

st.session_state.page1_counter = 1 + (st.session_state.get('page1_counter') or 0)
st.write(f':blue[Page1 Counter: {st.session_state.page1_counter}]')
st.write(f':green[auth.role: \'{auth.get_role()}\' of {auth.get_roles()}]')

st.header('Page1 is available to :red[everyone]')

# validate session role
if not auth.role_in(auth.get_roles()):
    st.warning('**Role status**: You are currently not logged.')
else:
    st.success(f'**Role status**: You are currently logged as **{auth.get_role()}**.')

# show page content
st.image('img/access-1.png')
st.write('The content of this page is visible by anyone, logged or not')