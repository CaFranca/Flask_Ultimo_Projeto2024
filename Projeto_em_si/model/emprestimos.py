from database import database

class Emprestimos(database.Model):
    __tablename__= 'emprestimos'
    id = database.Column(database.Integer, primary_key=True)  # Chave primária
    id_usuario = database.Column(database.Integer, database.ForeignKey("usuarios.id"), nullable=False)
    id_livro = database.Column(database.Integer, database.ForeignKey("livros.id"), nullable=False)
    data_emprestimo = database.Column(database.DateTime, nullable=False)  # Data do empréstimo
    data_devolucao_prevista = database.Column(database.DateTime, nullable=False)  # Data prevista para devolução
    data_devolucao_real = database.Column(database.DateTime, nullable=True)  # Data real de devolução
    
    usuario = database.relationship("Usuarios", back_populates="emprestimos")
    livro = database.relationship("Livros", back_populates="emprestimos")
    
    def JSonificar(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "id_livro": self.id_livro,
            "data_emprestimo": self.data_emprestimo.isoformat(),
            "data_devolucao_prevista": self.data_devolucao_prevista.isoformat(),
            "data_devolucao_real": self.data_devolucao_real.isoformat() if self.data_devolucao_real else None,
        }
