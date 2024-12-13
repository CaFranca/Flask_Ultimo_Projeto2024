from flask import Blueprint, request, render_template, redirect, url_for
from repository import LivroRepository
from datetime import datetime

# Criação de um Blueprint chamado "bp_books" para gerenciar rotas relacionadas a livros
livroController = Blueprint("bp_books", __name__)
# Instancia o repositório de livros
livroRepository = LivroRepository()

# Rota para adicionar um livro ao banco de dados
@livroController.route("/add", methods=['POST', 'GET'])
def add_book():
    if request.method == "POST":
        try:
            # Obtém os dados do formulário
            titulo = request.form.get('titulo', '').strip()
            isbn = request.form.get('isbn', '').strip()
            data_publicacaoBruta = request.form.get('publicadoEm', '').strip()
            autor_id = request.form.get('autor_id', '').strip()
            categoria_id = request.form.get('categoria_id', '').strip()
            quantidade_total = request.form.get('quantidadeTotal', '').strip()
            quantidade_disponivel = request.form.get('quantidadeDisponivel', '').strip()

            # Valida e converte os dados
            if not titulo or not isbn or not data_publicacaoBruta or not autor_id or not categoria_id or not quantidade_total or not quantidade_disponivel:
                return "Todos os campos obrigatórios devem ser preenchidos.", 400

            try:
                data_publicacao = datetime.strptime(data_publicacaoBruta, '%Y-%m-%d').date()
            except ValueError:
                return "Data de publicação inválida. Use o formato YYYY-MM-DD.", 400

            autor_id = int(autor_id) if autor_id.isdigit() else None
            categoria_id = int(categoria_id) if categoria_id.isdigit() else None
            quantidade_total = int(quantidade_total) if quantidade_total.isdigit() else None
            quantidade_disponivel = int(quantidade_disponivel) if quantidade_disponivel.isdigit() else None

            # Chama o repositório para adicionar o livro
            sucesso = livroRepository.addBook(
                titulo=titulo,
                isbn=isbn,
                ano_publicacao=data_publicacao,
                autor_id=autor_id,
                categoria_id=categoria_id,
                quantidade_total=quantidade_total,
                quantidade_disponivel=quantidade_disponivel
            )

            if sucesso:
                return redirect(url_for('bp_books.view_books'))
            else:
                return "Erro ao adicionar o livro no banco de dados.", 500

        except Exception as e:
            # Loga o erro para depuração
            print(f"Erro ao processar a solicitação de adicionar livro: {e}")
            return "Ocorreu um erro no servidor. Por favor, tente novamente.", 500

    return render_template('livros/livroADD.html')

@livroController.route('/livros', methods=['GET'])
def view_books():
    # Obtém os parâmetros de pesquisa do request
    titulo = request.args.get('titulo', '').strip()
    autor = request.args.get('autor', '').strip()
    genero = request.args.get('genero', '').strip()
    ano_inicio = request.args.get('ano_inicio', '').strip()

    try:
        # Busca personalizada no repositório
        livros = livroRepository.searchBooksCustom(
            titulo=titulo, 
            autor=autor, 
            genero=genero, 
            ano_inicio=ano_inicio
        )

        # Obtém listas de autores e gêneros para os filtros
        autores = livroRepository.getAutores()
        categorias = livroRepository.getCategoria()

        # Verifica se os dados de autores e gêneros estão carregados corretamente
        if not autores:
            print("Nenhum autor encontrado.")
        if not categorias:
            print("Nenhum gênero encontrado.")

        # Renderiza o template com os dados filtrados
        return render_template(
            'livros/livros.html',
            livros=livros,
            autores=autores,
            categorias=categorias
        )

    except Exception as e:
        # Retorna uma mensagem de erro genérica e loga o erro (log para depuração)
        print(f"Erro ao carregar a página de livros: {e}")
        return "Ocorreu um erro ao carregar a página de livros.", 500

@livroController.route('/editar/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    if request.method == 'POST':
        # Coleta os dados do formulário
        titulo = request.form.get('titulo', '').strip()
        isbn = request.form.get('isbn', '').strip()
        data_publicacaoBruta = request.form.get('data_publicacao', '').strip()
        autor_id = request.form.get('autor_id', '').strip()
        categoria_id = request.form.get('categoria_id', '').strip()
        quantidade_total = request.form.get('quantidade_total', '').strip()
        quantidade_disponivel = request.form.get('quantidade_disponivel', '').strip()

        try:
            data_publicacao = datetime.strptime(data_publicacaoBruta, '%Y-%m-%d').date()
        except ValueError:
            return "Data de publicação inválida. Use o formato YYYY-MM-DD.", 400

        # Chama o método para atualizar o livro
        resultado = livroRepository.updateBook(
            id,
            titulo,
            isbn,
            data_publicacao,
            autor_id,
            categoria_id,
            quantidade_total,
            quantidade_disponivel
        )

        if "Erro" in resultado:
            return resultado  # Se falhou, retorna a mensagem de erro

        # Se sucesso, redireciona para a página de livros
        return redirect(url_for('bp_books.view_books'))

    # Se for GET, carrega os dados do livro para o formulário
    livro = livroRepository.getBookById(id)
    autores = livroRepository.getAutores()
    categorias = livroRepository.getCategoria()

    return render_template('livros/LivroEdit.html', livro=livro, autores=autores, categorias=categorias)

@livroController.route('/excluir/<int:id>', methods=['POST'])
def delete_book(id):
    # Chama o método de exclusão do livro no repositório
    resultado = livroRepository.deleteBook(id)

    if resultado.startswith("Erro"):
        # Se ocorrer um erro, exibe a mensagem de erro
        return resultado
    else:
        # Caso contrário, redireciona de volta para a lista de livros
        return redirect(url_for('bp_books.view_books'))

# Rota inicial para renderizar uma página específica para livros
@livroController.route("/")
def books_home():
    return redirect(url_for('bp_books.view_books'))
