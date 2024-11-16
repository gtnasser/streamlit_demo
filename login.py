import streamlit as st
import time
import auth

import users_controller as userctl


def do_login(username, password):
    user = userctl.validate(username, password)
    if user:
        auth.set_role(user['role'])
        auth.set_user(user['userid'])
        return userctl.get_data(username)


def do_logout():
    auth.set_role('')
    auth.set_user('')
    return None


def sidebar():
    """ cria tela de login no sidebar """
    # TODO: passar como parametros as acoes pos-login e pos-logout
    login_area = st.sidebar.container(border=False)
    with login_area:

        if auth.valid():
            user = userctl.get_data(auth.get_user())
            name = user.get('name') or user.get('userid')
            login_area.write(f'Usuário: {name}')
            if st.button('LOGOUT', use_container_width=True, type='primary'):
                do_logout()
                st.rerun()

        else:
            col1, col2, col3 = st.columns([5, 5, 3], vertical_alignment='bottom')
            with col1:
                username = st.text_input('Usuario', key="_tu")
            with col2:
                password = st.text_input('Senha', key="_tp")
            with col3:
                if st.button(':key:', use_container_width=True, type='primary', key="_bi"):
                    if do_login(username, password):
                        login_area.success('Usuário logado com sucesso')
                        time.sleep(2)
                        st.rerun()
                    else:
                        login_area.error('Usuário/senha inválidos')



def sidebar3():
    """ cria tela de login no sidebar """
    # TODO: passar como parametros as acoes pos-login e pos-logout
    login_area3 = st.sidebar.container(border=False)
#    with login_area3:
#        if auth.valid():
#            user = auth.get_user()
#            login_area3.write(f'Usuário: {user}')
#            if st.button('LOGOUT', use_container_width=True, type='primary'):
#                do_logout()
#                st.rerun()
#        else:
#            col1, col2, col3 = st.columns([5, 5, 3], vertical_alignment='bottom')
#            with col1:
#                username = st.text_input('Usuario', key="_t3u")
#            with col2:
#                password = st.text_input('Senha', key="_t3p")
#            with col3:
#                if st.button(':key:', use_container_width=True, type='primary', key="_b3i"):
#                    None
#                    if do_login(username, password):
#                        login_area3.success('Usuário logado com sucesso')
#                        time.sleep(2)
#                        st.rerun()
#                    else:
#                        login_area3.error('Usuário/senha inválidos')

