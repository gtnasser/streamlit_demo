# users controller
#
# simula uma interface simples de autenticacao de usuarios
#
# estrutura minima do registro de usuario deve ser:
# - userid
# - passwd
# - role

__db_users__ = [
    {
        "userid": "user",
        "passwd": "user",
        "roleid": "user"
    }, {
        "userid": "demo",
        "passwd": "demo",
        "roleid": "demo"
    }, {
        "userid": "user2",
        "passwd": "user2",
        "roleid": "user"
    }, {
        "userid": "admin",
        "passwd": "admin",
        "roleid": "admin",
        "name": "Barão"
    }
]


def validate(username, password):
    """ valida e retorna dados minimos do usuario """
    user = next( (u for u in __db_users__ if u['userid']==username and u['passwd']==password), None)
    return (user is not None)


def get_data(username):
    """ retorna todos os dados do usuario exceto senha """
    user = next( (us for us in __db_users__ if us['userid']==username), None)
    if user and 'passwd' in user:
        user.pop('passwd')
    return user

