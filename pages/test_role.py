""" TODO: docstring """
import streamlit as st
import auth

st.subheader('Login Simulator')
st.write(f':orange[Auth valid:{auth.valid()} - role:\'{auth.get_role()}\' - user:\'{auth.get_user()}\']')

# seleciona role

filter_area = st.container()
content_area = st.container()

sel_roles = ['user', 'admin', 'demo', 'logout']
sel_pos = next((i for i, role in enumerate(sel_roles)
               if role == auth.get_role()), None)


def clear_msg():
    """clear content area"""
    content_area.write(' ')


def set_role(role):
    """update session data"""
    if role == 'logout':
        auth.set_user('')
        auth.set_role('')
    else:
        auth.set_role(role)
    content_area.write(f'Current role changed to **\'{auth.get_role()}\'**')


with filter_area:
    col1, col2 = st.columns([11, 2])
    with col1:
        option = st.selectbox("Select new role", index=sel_pos,
                              options=sel_roles, on_change=clear_msg)
    with col2:
        st.html('<div style="height:12px"></div>')
        st.button('SET', type="primary",
                  disabled=(len(sel_roles) == 0),
                  on_click=set_role, args=[option])

