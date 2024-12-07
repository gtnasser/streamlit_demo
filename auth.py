# usage: ???
#
# prove um mecanismo simples de verificacao da autenticacao do usuario no app
# utiliza variaveis de sessao, portanto volateis, e devem ser utilizadas em conjunto
# com um provedor de acesso a uma base de usuarios
#
# trata dois niveis de informacao, role e usuario
#
# role == regra atual
# armazena o nivel de acesso ou a regra a ser utilizada para validar a autenticacao
#
# - default = None
# - deve ser atualizada apos a autenticacao do usuario, com a role do usuario, ex: 'auth.set_role("authenticated_role")'
# - deve ser recuperada toda vez que for necessario valida-la, ex: 'current_role = auth.get_role()'
# - pode ser verificada se foi definida com 'exists_current_role = auth.isvalid_role()'
# - para validar se a role atual esta no conjunto a ser validado, use `auth.role_in([isvalid_role_set])`
#
# user == usuario atual
#
# de conteudo livre, armazena as informacoes do usuario a serem utilizadas no projeto
# - default = None
# - deve ser atualizado apos a autenticacao do usuario -> 'auth.set_user(new_user_info)'
# - deve ser recuperado com 'auth.get_user()'
# - pode ser verificada se foi definico com 'auth.isvalid_user()'
#
"""
TODO: documentar: colocar versao, copy, usage, etc
TODO: krypto, jwt
"""

import uuid
import streamlit as st

# globals
__uuid4 = str(uuid.uuid4())
__key = '__auth__' + __uuid4

print('uuid4: ', __uuid4)

# creates a auth session var
def check_session():
    """ TODO: docstring """
    if __key not in st.session_state:
        st.session_state[__key] = {
            'role': None,
            'user': None
        }
        print(f'session {__key} not found, recreating var')

# executo quando este singleton for carregado pela primeira vez.
# quando houver a execucao em uma nova sessao, as variaveis de
# sessao aida nao terao sido criadas, por isso chamo a execucao
# desta rotina em todas as rotinas deste modulo, para que sejam
# inicializadas.

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

# check if is there a role defined
def isvalid_role():
    """ TODO: docstring """
    check_session()
    return bool(get_role())

# check if is there a user defined
def isvalid_user():
    """ TODO: docstring """
    check_session()
    return bool(get_user())
