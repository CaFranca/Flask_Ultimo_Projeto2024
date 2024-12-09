from models import User
from database import db


class UserDao:
    @staticmethod
    def Buscar_todos_usuarios():
        return User.query.all()

    @staticmethod
    def add_usuario(nome, email):
        try:
            user = User(nome=nome, email=email)
            db.session.add(user)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False