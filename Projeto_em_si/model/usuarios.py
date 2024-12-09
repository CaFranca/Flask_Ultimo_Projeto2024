from database import database

class Usuarios(database.Model):
    __tablename__= 'usuarios'
    id = database.Column(database.Integer, primary_key=True)  # Chave primária
    nome = database.Column(database.String(100), nullable=False)  # Nome do usuário
    email = database.Column(database.String(120), unique=True, nullable=False)  # Email único
    senha = database.Column(database.String(255), nullable=False)  # Senha com hash
    tipo = database.Column(database.String(20), nullable=False)  # Tipo de usuário (admin, usuário comum)
    data_criacao = database.Column(database.DateTime, nullable=False)  # Data de criação do registro
    
    emprestimos = database.relationship("Emprestimos", back_populates="usuario", lazy=True)
    reservas = database.relationship("Reservas", back_populates="usuario", lazy=True)
    multas = database.relationship("Multas", back_populates="usuario", lazy=True)
    
    def JSonificar(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "tipo": self.tipo,
            "data_criacao": self.data_criacao.isoformat(),
            "emprestimos": [emprestimo.JSonificar() for emprestimo in self.emprestimos],
            "reservas": [reserva.JSonificar() for reserva in self.reservas],
            "multas": [multa.JSonificar() for multa in self.multas]
        }
