from model import Users, poggers
from model import Posts

class UserDAO():
    @staticmethod
    def searchUsers():
        return Users.query.all()
    @staticmethod
    def addUsers(nome, email):
        try:
            user = Users(nome = nome, email = email)
            poggers.session.add(user)
            post = Posts(titulo = "postagem", conteudo = "qualq", user_id =1)
            poggers.session.add(post)
            poggers.session.commit()
            return True
        except Exception as e:
            poggers.session.rollback()
            return False