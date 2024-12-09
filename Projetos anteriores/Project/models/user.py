from database import db

class Produto(db.Model):
    codigo = db.Column(db.String(64), primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
