from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(80), nullable = True)
    email = db.Column(db.String(120), nullable = True)

    def toJson(self):
        return {"id": self.id, "nome": self.nome, "email": self.email}