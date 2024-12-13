from database import database

class Autores(database.Model):
    __tablename__ = 'autores'
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100), nullable=False)
    livros = database.relationship("Livros", back_populates="autor")
