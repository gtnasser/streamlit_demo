# users controller
#
# estrutura minima do registro de usuario deve ser:
# - userid
# - passwd
# - role

db_users = [
    {
        "userid": "user",
        "passwd": "user",
        "role": "user"
    }, {
        "userid": "demo",
        "passwd": "demo",
        "role": "demo"
    }, {
        "userid": "user2",
        "passwd": "user2",
        "role": "user"
    }, {
        "userid": "admin",
        "passwd": "admin",
        "role": "admin",
        "name": "Figuer"
    }
]


def validate(username, password):
    """ valida e retorna dados minimo sdo usuario """
    user = next( (us for us in db_users if us['userid']==username and us['passwd']==password), None)
    return user


def get_data(username):
    """ retorna todos os dados do usuario exceto senha """
    user = next( (us for us in db_users if us['userid']==username), None)
    if user and 'passwd' in user:
        user.pop('passwd')
    return user

