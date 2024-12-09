from database import poggers

class Users(poggers.Model):
    id = poggers.Column(poggers.Integer, primary_key = True)
    nome = poggers.Column(poggers.String(80), nullable = True)
    email = poggers.Column(poggers.String(120), nullable = True)

    posts = poggers.relationship("Posts", back_populates = "autor", lazy=True)

    def JSonificar(self):
        return {"id": self.id, "nome": self.nome, "email": self.email, "posts": [post.JSonificar() for post in self.posts]}