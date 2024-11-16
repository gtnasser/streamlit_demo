import auth
import streamlit as st
import pandas as pd

st.subheader('auth.py lib Auto test')

def line_print(p1, p2, p3, p4):
    col1, col2, col3, col4 = st.columns([1,1,3,1])
    with col1:
        st.markdown(p1)
    with col2:
        st.markdown(p2)
    with col3:
        st.markdown(p3)
    with col4:
        st.markdown(p4)

def teste(id, role, roles):
    auth.set_role(role)
    line_print(id,
           f"'{auth.get_role()}'",
           roles,
           auth.role_in(roles)
           )

line_print('**Test ID**', '**role**', '**roles**', '**role_in()**')
teste('#1', 'none',  ['user','admin'])
teste('#2', 'supe',  ['user','admin','super'])
teste('#3', 'supe',  [])
teste('#4', '',      [''])
teste('#5', '',      [])
