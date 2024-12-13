from database import database

class Livros(database.Model):
    __tablename__ = 'livros'
    id = database.Column(database.Integer, primary_key=True)  # Chave primária
    titulo = database.Column(database.String(200), nullable=False)  # Título do livro
    autor_id = database.Column(database.Integer, database.ForeignKey('autores.id'), nullable=False)  # Chave estrangeira para autores
    editora = database.Column(database.String(100), nullable=False)  # Editora do livro
    ano_publicacao = database.Column(database.Integer, nullable=False)  # Ano de publicação
    genero = database.Column(database.String(50), nullable=False)  # Gênero do livro
    isbn = database.Column(database.String(20), unique=True, nullable=False)  # Código ISBN único
    quantidade_total = database.Column(database.Integer, nullable=False)  # Quantidade total em estoque
    quantidade_disponivel = database.Column(database.Integer, nullable=False)  # Quantidade disponível
    
    # Relacionamento com a tabela "Autores"
    autor = database.relationship("Autores", back_populates="livros")
    
    emprestimos = database.relationship("Emprestimos", back_populates="livro", lazy=True)
    reservas = database.relationship("Reservas", back_populates="livro", lazy=True)
    
    def jsonificar(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor_id": self.autor_id,
            "editora": self.editora,
            "ano_publicacao": self.ano_publicacao,
            "genero": self.genero,
            "isbn": self.isbn,
            "quantidade_total": self.quantidade_total,
            "quantidade_disponivel": self.quantidade_disponivel,
        }
