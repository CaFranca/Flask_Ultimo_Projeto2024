from database import database

class Multas(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    usuario_id = database.Column(database.Integer, database.ForeignKey("usuarios.id"), nullable=False)
    valor = database.Column(database.Float, nullable=False)
    data_geracao = database.Column(database.DateTime, nullable=False)
    status = database.Column(database.String(20), nullable=False)

    usuario = database.relationship("Usuarios", back_populates="multas")

    def JSonificar(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "valor": self.valor,
            "data_geracao": self.data_geracao.isoformat(),
            "status": self.status
        }