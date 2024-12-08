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
        auth.set_user(user)
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

#            1. somente texto simples
#            login_area.write(f"Usuário: {user.get('name',None) or user.get('userid',None)}")
#            login_area.write(f"Role: {user.get('roleid',None)}")

#            2. texto dentro de uma area success
#            login_area.success(f"Usuário: {user.get('name',None) or user.get('userid',None)}  \n Role: {user.get('roleid',None)}")

#            3. avatar
#            cols = login_area.columns([3,8], vertical_alignment='center')
#            with cols[0]:
#                st.image("https://api.multiavatar.com/{user.get('userid',None)}.svg", width=80)
#                #st.image("https://robohash.org/{user.get('userid',None)}", width=80)
#            with cols[1]:
#                st.success(f"Usuário: **{user.get('name',None) or user.get('userid',None)}**  \n Role: {user.get('roleid',None)}")

#            4. avatar inside alert

            #userid = user.get("userid",None)
            userid = time.time()
            #div1 = f'<img style="width: 60px" src="https://robohash.org/{userid}">'
            div1 = f'<img style="width: 50px;margin-right: 20px;" src="https://api.multiavatar.com/{userid}.svg">'
            div2 = f"<div>Usuário: <b>{user.get('name',None) or user.get('userid',None)}</b> <br> Role: {user.get('roleid',None)}</div>"
            html = f'<div style="background-color:#e8f9ee;color:#177233;padding:10px;border-radius:5px;display:flex;align-items:center">{div1}{div2}</div>'
            st.write(html, unsafe_allow_html=True)


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
