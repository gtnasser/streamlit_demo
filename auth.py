# usage: ???
#
# role -> regra atual
# - default = 'none'
# - deve ser atualiza apos a autenticacao do usuario -> 'auth.set_role("new_role")'
# - pode ser recuperada com 'auth.get_role()'
#
# roles -> conjunto de regras
# - default = ['user','admin']
# - pode ser customizado com um novo conjunto -> `auth.set_roles([new_set])`
# - pode ser recuperada com 'auth.get_roles()'
#
# valida se a role atual esta no conjunto -> `auth.role_in([this_set])`
#

# TODO: documentar: colocar versao, copy, usage, etc
# TODO: krypto, jwt


import streamlit as st
import uuid

# globals
__key = '__auth__'
__uuid4 = str(uuid.uuid4())

print('uuid4: ', __uuid4)

# creates a auth session var
def check_session():
    if __key not in st.session_state:
        st.session_state[__key] = {
            'role': '',
            'roles': ['user','admin']
        }
        print(f'session {__key} not found, recreating var')
check_session()

# set current role
def set_role(curr_role):
    check_session()
    st.session_state[__key]['role'] = curr_role
    #print(f"auth.role -> {st.session_state[__key]['role']}")

# set current role
def get_role():
    check_session()
    return st.session_state[__key]['role']

# set custom roles
def set_roles(new_set):
    check_session()
    st.session_state[__key]['role'] = new_set
    #print(f"auth.roles -> {st.session_state[__key]['roles']}")

# get current roles
def get_roles():
    check_session()
    return st.session_state[__key]['roles']

# check if current role matchs
def role_in(set_of_roles):
    check_session()
    return st.session_state[__key]['role'] in set_of_roles
