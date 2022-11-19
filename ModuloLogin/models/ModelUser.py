from .entities.Usuario import Usuario

class ModelUser():

    @classmethod
    def login(self, db, user):
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, email FROM usuario 
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = Usuario(row[0], row[1], Usuario.check_password(row[2], user.password), row[3])
                return user
            else:
                return None

    @classmethod
    def get_by_id(self, db, id):
            cursor = db.connection.cursor()
            sql = "SELECT id, username, email FROM usuario WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return Usuario(row[0], row[1], None, row[2])
            else:
                return None