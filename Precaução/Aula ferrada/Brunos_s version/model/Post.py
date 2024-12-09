from database import poggers

class Posts(poggers.Model):
    id = poggers.Column(poggers.Integer, primary_key = True)
    titulo = poggers.Column(poggers.String(200))
    conteudo = poggers.Column(poggers.Text)
    user_id = poggers.Column(poggers.Integer, poggers.ForeignKey("users.id"), nullable = False)
    
    autor = poggers.relationship("Users", back_populates = "posts", lazy=True)

    def JSonificar(self):
        return {"id": self.id, "titulo": self.titulo, "conteudo": self.conteudo}