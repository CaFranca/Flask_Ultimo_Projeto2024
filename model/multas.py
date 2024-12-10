from database import database

class Multas(database.Model):
    __tablename__= 'multas'
    id = database.Column(database.Integer, primary_key=True)  # Chave primária
    id_usuario = database.Column(database.Integer, database.ForeignKey("usuarios.id"), nullable=False)
    valor = database.Column(database.Float, nullable=False)  # Valor da multa
    data_geracao = database.Column(database.DateTime, nullable=False)  # Data em que a multa foi gerada
    status = database.Column(database.String(20), nullable=False)  # Status da multa (paga, pendente)
    
    usuario = database.relationship("Usuarios", back_populates="multas")
    
    def JSonificar(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "valor": self.valor,
            "data_geracao": self.data_geracao.isoformat(),
            "status": self.status,
        }
