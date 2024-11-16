import auth
import streamlit as st

st.subheader('Login Simulator')
st.write(f':green[auth.role: \'{auth.get_role()}\' of {auth.get_roles()}]')

# seleciona role

filter = st.container()
content = st.container()

sel_roles = ['none'] + auth.get_roles()
sel_pos = next( (i for i, role in enumerate(sel_roles) if role == auth.get_role()), None)

def clear_msg():
    content.write(' ')

def set_role(role):
    auth.set_role(role)
    content.write(f'Current role changed to **{auth.get_role()}**')

with filter:
    col1, col2 = st.columns([11,2])
    with col1:
        option = st.selectbox("Select new role", index=sel_pos, options=sel_roles, on_change=clear_msg)
    with col2:
        st.html('<div style="height:12px"></div>')
        st.button('SET', type="primary", disabled=(len(sel_roles)==0), on_click=set_role, args=[option])





