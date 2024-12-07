""" TODO: docstring """
import time
import streamlit as st
import auth

import fake_users_controller as userctl

def do_login(username, password):
    """ efetua validacao de username/password retornando True/False """
    if userctl.validate(username, password):
        user = userctl.get_data(username)
        auth.set_role(user.get('roleid', None))
        auth.set_user(user) #['userid'])
        return True
    return False


def do_logout():
    """ TODO: docstring """
    auth.set_role('')
    auth.set_user('')


def sidebar_login():
    """ cria tela de login no sidebar """
    login_area = st.sidebar.container(border=False)
    with login_area:

        if auth.isvalid_user():
            user = auth.get_user()
            login_area.write(f"Usuário: {user.get('name',None) or user.get('userid',None)}")
            login_area.write(f"Role: {user.get('roleid',None)}")
            if st.button('LOGOUT', use_container_width=True, type='primary'):
                do_logout()
                st.rerun()

        else:
            col1, col2, col3 = st.columns([5, 5, 3], vertical_alignment='bottom')
            with col1:
                username = st.text_input('Usuario')
            with col2:
                password = st.text_input('Senha')
            with col3:
                if st.button(':key:', use_container_width=True, type='primary', key="_bi"):
                    if do_login(username, password):
                        login_area.success('Usuário logado com sucesso')
                        time.sleep(2)
                        st.rerun()
                    else:
                        login_area.error('Usuário/senha inválidos')

            # teste: mostrar usuarios disponiveis
            users1 = login_area.container(border=True)
            user_list = ['* '+user["userid"] for user in userctl.__db_users__]
            users1.markdown('Usuarios disponíveis:   \n' + '  \n'.join(user_list))
