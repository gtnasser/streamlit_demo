# usage: ???
#
# role -> regra atual
# - default = ''
# - deve ser atualizada apos a autenticacao do usuario -> 'auth.set_role("new_role")'
# - pode ser recuperada com 'auth.get_role()'
#
# user -> usuario atual
# - default = ''
# - deve ser atualizado apos a autenticacao do usuario -> 'auth.set_user("new_user")'
# - pode ser recuperado com 'auth.get_user()'
#
# valida se a role atual esta no conjunto -> `auth.role_in([this_set])`
#
"""
TODO: documentar: colocar versao, copy, usage, etc
TODO: krypto, jwt
"""

import uuid
import streamlit as st

# globals
__key = '__auth__'
__uuid4 = str(uuid.uuid4())

print('uuid4: ', __uuid4)

# creates a auth session var
def check_session():
    """ TODO: docstring """
    if __key not in st.session_state:
        st.session_state[__key] = {
            'role': '',
            'user': ''
        }
        print(f'session {__key} not found, recreating var')
check_session()

# set current role
def set_role(curr_role):
    """ TODO: docstring """
    check_session()
    st.session_state[__key]['role'] = curr_role
    #print(f"auth.role -> {st.session_state[__key]['role']}")

# get current role
def get_role():
    """ TODO: docstring """
    check_session()
    return st.session_state[__key]['role']

# set current user
def set_user(curr_user):
    """ TODO: docstring """
    check_session()
    st.session_state[__key]['user'] = curr_user
    #print(f"auth.role -> {st.session_state[__key]['role']}")

# get current user
def get_user():
    """ TODO: docstring """
    check_session()
    return st.session_state[__key]['user']

# check if current role matchs
def role_in(set_of_roles):
    """ TODO: docstring """
    check_session()
    return st.session_state[__key]['role'] in set_of_roles

# check if defined role or user
def valid():
    """ TODO: docstring """
    check_session()
    return bool(get_user() or get_role())

