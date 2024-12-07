""" TODO: docstring """
import streamlit as st
import auth

st.subheader('Auth Sample Page')
st.write('This sample allows you change the :red[role] and check how Auth Sample Pages can or not be accessed.')

st.write(f":blue[**Auth data**]:    :{'green' if auth.isvalid_role() else 'red'}-background[role:'{auth.get_role()}']  :{'green' if auth.isvalid_user() else 'red'}-background[user:'{auth.get_user()}'] ")

# validate session role
if not auth.isvalid_role():
    st.error('**Role status**: You are currently not logged.')
else:
    st.success(f'**Role status**: You are currently logged as **{auth.get_role()}**.')

# select role

filter_area = st.container()
content_area = st.container()

sel_roles = ['user', 'admin', 'demo', 'logout']
sel_pos = next((i for i, role in enumerate(sel_roles) if role == auth.get_role()), None)

def clear_msg():
    """clear content area"""
    content_area.write(' ')

def set_role(role = None):
    """update session data"""
    if role == 'logout':
        auth.set_user('')
        auth.set_role('')
    else:
        auth.set_role(role)
#    content_area.write(f'Current role changed to **\'{auth.get_role()}\'**')

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

# access board

st.divider()
content_area.markdown(
    f"""
    Page # | Criteria | Code | Can :red[{auth.get_role()}] access it?
    --- | --- | --- | ---
    1 | No validation | | :heavy_check_mark:
    2 | Anynone logged | `auth.isvalid_role() == True` | {':heavy_check_mark:' if auth.isvalid_role() else ':x:'}
    3 | Just **admin** role | `auth.role_in(['admin']) == True` | {':heavy_check_mark:' if auth.role_in(['admin']) else ':x:'}
    """
)


