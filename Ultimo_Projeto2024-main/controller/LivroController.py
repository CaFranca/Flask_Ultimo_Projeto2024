from flask import Blueprint, request, render_template, redirect, url_for, flash
from repository import LivroRepository

livroController = Blueprint("bp_books", __name__)
livroRepository = LivroRepository()


# Rota para adicionar um novo livro
@livroController.route("/add", methods=['POST'])
def add_book():
    try:
        # Obtém os dados do formulário enviados pelo usuário
        titulo = request.form.get('titulo')  # Título do livro
        isbn = request.form.get('isbn')  # ISBN do livro
        data_publicacao = request.form.get('publicadoEm')  # Data de publicação do livro
        autor_id = request.form.get('autor_id')  # ID do autor do livro
        categoria_id = request.form.get('categoria_id')  # ID da categoria do livro
        quantidade_total = request.form.get('quantidade_total')  # Quantidade total de exemplares

        # Validação básica dos dados recebidos
        if not (titulo and isbn and data_publicacao and autor_id and categoria_id and quantidade_total):
            # Caso algum campo obrigatório esteja vazio, exibe uma mensagem de erro
            flash("Todos os campos são obrigatórios.", "error")
            return redirect(url_for('bp_inicio.index'))  # Redireciona de volta para a página inicial

        # Exibe uma mensagem no console para verificar que os dados foram recebidos
        print("Livro recebido")

        # Chama o método addBook do repositório para adicionar o livro no banco de dados
        resultado = livroRepository.addBook(
            titulo=titulo,
            isbn=isbn,
            data_publicacao=data_publicacao,
            autor_id=autor_id,
            categoria_id=categoria_id,
            quantidade_total=quantidade_total
        )

        # Verifica se o resultado contém um erro e exibe a mensagem correspondente
        if "error" in resultado:
            flash(resultado["error"], "error")  # Mensagem de erro, caso haja
        else:
            flash("Livro adicionado com sucesso!", "success")  # Mensagem de sucesso, caso o livro seja adicionado com sucesso

        # Redireciona de volta para a página inicial
        return redirect(url_for('bp_inicio.index'))

    except Exception as e:
        # Caso ocorra alguma exceção durante o processo, captura o erro e exibe uma mensagem
        print("Fudeu")  # Exibe no console que houve um erro (mensagem de debug)
        flash(f"Ocorreu um erro: {e}", "error")  # Exibe a mensagem de erro para o usuário
        return redirect(url_for('bp_inicio.index'))  # Redireciona de volta para a página inicial



@livroController.route('/livros', methods=['GET'])
def view_books():
    try:
        titulo = request.args.get('titulo', '').strip()
        autor_id = request.args.get('autor_id', '').strip()
        categoria_id = request.args.get('categoria_id', '').strip()
        data_inicio = request.args.get('data_inicio', '').strip()
        isbn = request.args.get('isbn', '').strip()

        livros = livroRepository.searchBooksCustom(
            titulo=titulo,
            autor_id=autor_id,
            categoria_id=categoria_id,
            data_inicio=data_inicio
            
        )

        autores = livroRepository.getAutores()
        categorias = livroRepository.getCategorias()

        return render_template(
            'Livro/livros.html',
            livros=livros,
            autores=autores,
            categorias=categorias
        )
    except Exception as e:
        flash(f"Erro ao carregar os livros: {e}", "error")
        return render_template('Livro/livros.html', livros=[], autores=[], categorias=[])


@livroController.route('/editar/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    if request.method == 'POST':
        try:
            titulo = request.form.get('titulo')
            isbn = request.form.get('isbn')
            data_publicacao = request.form.get('data_publicacao')
            autor_id = request.form.get('autor_id')
            categoria_id = request.form.get('categoria_id')
            quantidade_total=request.form.get('quantidade_total')

            if not (titulo and isbn and data_publicacao  and autor_id and categoria_id and quantidade_total):
                flash("Todos os campos são obrigatórios.", "error")
                return redirect(url_for('bp_books.edit_book', id=id))

            resultado = livroRepository.updateBook(
                id, titulo, isbn, data_publicacao, autor_id, categoria_id, quantidade_total
            )

            if "error" in resultado:
                flash(resultado["error"], "error")
            else:
                flash("Livro atualizado com sucesso!", "success")

            return redirect(url_for('bp_books.view_books'))
        except Exception as e:
            flash(f"Erro ao atualizar o livro: {e}", "error")
            return redirect(url_for('bp_books.edit_book', id=id))

    livro = livroRepository.getBookById(id)
    autores = livroRepository.getAutores()
    categorias = livroRepository.getCategorias()

    return render_template('Livro/LivroEdit.html', livro=livro, autores=autores, categorias=categorias)


@livroController.route('/excluir/<int:id>', methods=['POST','GET'])
def delete_book(id):
    try:
        resultado = livroRepository.deleteBook(id)
        if "error" in resultado:
            flash(resultado["error"], "error")
        else:
            flash("Livro excluído com sucesso!", "success")

        return redirect(url_for('bp_books.view_books'))
    except Exception as e:
        flash(f"Erro ao excluir o livro: {e}", "error")
        return redirect(url_for('bp_books.view_books'))


@livroController.route("/")
def books_home():
    return redirect(url_for('bp_books.view_books'))
