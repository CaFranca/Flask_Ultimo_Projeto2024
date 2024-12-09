from database import database

class Reservas(database.Model):
    id = database.Column(database.Integer, primary_key=True)  # Chave primária
    id_usuario = database.Column(database.Integer, database.ForeignKey("usuarios.id"), nullable=False)
    id_livro = database.Column(database.Integer, database.ForeignKey("livros.id"), nullable=False)
    data_reserva = database.Column(database.DateTime, nullable=False)  # Data da reserva
    status = database.Column(database.String(20), nullable=False)  # Status da reserva
    
    usuario = database.relationship("Usuarios", back_populates="reservas")
    livro = database.relationship("Livros", back_populates="reservas")
    
    def JSonificar(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "id_livro": self.id_livro,
            "data_reserva": self.data_reserva.isoformat(),
            "status": self.status,
        }
