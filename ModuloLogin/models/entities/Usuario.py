from werkzeug.security import check_password_hash
from flask_login import UserMixin

class Usuario(UserMixin):

    def __init__(self, id, username, password, email=""):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    @classmethod # no es necesario instanciar clase
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

