import streamlit as st
import auth
import time

st.session_state.page2_counter = 1 + (st.session_state.get('page2_counter') or 0)
st.write(f':blue[Page2 Counter: {st.session_state.page2_counter}]')
st.write(f':green[auth.role: \'{auth.get_role()}\' of {auth.get_roles()}]')

st.header('Page2 is available to :red[all logged users]')

def goto_page(pagename, seconds):
    w = st.empty()
    for s in range(seconds,0,-1):
        w.write(f"This page will be redirected in **:red[{s}]** seconds.")
        time.sleep(1)
    st.switch_page('app.py')

# validate session role
if not auth.role_in(auth.get_roles()):
    st.error('**Role status**: You are currently not logged.')
    st.image('img/access-0.png')
    goto_page('app.py', 5)

# show page content
st.success(f'**Role status**: You are currently logged as **{auth.get_role()}**.')
st.image('img/access-1.png')
st.write('The content of this page is just visible by logged users.')
