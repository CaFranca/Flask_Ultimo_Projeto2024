from model import user,db


class UserDAO:
    @staticmethod
    def buscar_todos_ususarios():
        return user.query.all()
    
    @staticmethod
    def add_usuario(nome,email):
            
        try:
            user=user(nome = nome, email = email)
            db.session.add(user)
            db.session.commit()
            return True         
        except Exception as e:
            db.session.rollback(e)
            return False
