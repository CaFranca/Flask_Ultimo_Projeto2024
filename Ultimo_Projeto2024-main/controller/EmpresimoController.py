from flask import Blueprint, request, redirect, url_for, render_template, flash
from repository import EmprestimosRepository

emprestimoController = Blueprint('bp_loan', __name__)
emprestimosRepository = EmprestimosRepository()


@emprestimoController.route('/add', methods=['POST'])
def add_emprestimo():
    try:
        # Coleta de dados do formulário
        usuario_id = request.form.get('usuario_id')
        livro_id = request.form.get('livro_id')
        data_emprestimo = request.form.get('data_emprestimo')
        data_devolucao_prevista = request.form.get('data_devolucao_prevista')

        # Validação dos campos obrigatórios
        if not all([usuario_id, livro_id, data_emprestimo, data_devolucao_prevista]):
            flash("Todos os campos são obrigatórios.", "error")
            return redirect(url_for('bp_loan.view_emprestimos'))

        # Tentativa de criar o empréstimo
        response = emprestimosRepository.criarEmprestimo(
            usuario_id, livro_id, data_emprestimo, data_devolucao_prevista
        )
        if isinstance(response, str):
            flash(response, "error")
        else:
            flash("Empréstimo criado com sucesso!", "success")

        return redirect(url_for('bp_loan.view_emprestimos'))
    except Exception as e:
        flash(f"Erro ao criar empréstimo: {e}", "error")
        return redirect(url_for('bp_loan.view_emprestimos'))


@emprestimoController.route('/', methods=['GET'])
def view_emprestimos():
    try:
        # Busca todos os empréstimos para exibição
        emprestimos = emprestimosRepository.listarTodosJSON()
        return render_template("Emprestimo/emprestimos.html", emprestimos=emprestimos)
    except Exception as e:
        flash(f"Erro ao carregar os empréstimos: {e}", "error")
        return render_template("Emprestimo/emprestimos.html", emprestimos=[])


@emprestimoController.route('/editar/<int:emprestimo_id>', methods=['GET', 'POST'])
def edit_emprestimo(emprestimo_id):
    try:
        if request.method == 'POST':
            # Atualização de dados do empréstimo
            data_devolucao_real = request.form.get('data_devolucao_real')
            if not data_devolucao_real:
                flash("Data de devolução real é obrigatória.", "error")
                return redirect(url_for('bp_loan.edit_emprestimo', emprestimo_id=emprestimo_id))

            response = emprestimosRepository.atualizarDevolucao(emprestimo_id, data_devolucao_real)
            if "Erro" in response:
                flash(response, "error")
            else:
                flash("Devolução atualizada com sucesso!", "success")

            return redirect(url_for('bp_loan.view_emprestimos'))

        # Recuperação do empréstimo para exibição no formulário
        emprestimo = emprestimosRepository.buscarEmprestimoPorId(emprestimo_id)
        if not emprestimo:
            flash("Empréstimo não encontrado.", "error")
            return redirect(url_for('bp_loan.view_emprestimos'))

        return render_template("Emprestimo/emprestimo_edit.html", emprestimo=emprestimo)
    except Exception as e:
        flash(f"Erro ao editar empréstimo: {e}", "error")
        return redirect(url_for('bp_loan.view_emprestimos'))


@emprestimoController.route('/excluir/<int:emprestimo_id>', methods=['POST'])
def delete_emprestimo(emprestimo_id):
    try:
        response = emprestimosRepository.deletarEmprestimo(emprestimo_id)
        if "Erro" in response:
            flash(response, "error")
        else:
            flash("Empréstimo excluído com sucesso!", "success")

        return redirect(url_for('bp_loan.view_emprestimos'))
    except Exception as e:
        flash(f"Erro ao excluir empréstimo: {e}", "error")
        return redirect(url_for('bp_loan.view_emprestimos'))


@emprestimoController.route('/usuario/<int:usuario_id>', methods=['GET'])
def listar_por_usuario(usuario_id):
    try:
        emprestimos = emprestimosRepository.listarPorUsuarioJSON(usuario_id)
        return render_template("Emprestimo/emprestimos_por_usuario.html", emprestimos=emprestimos)
    except Exception as e:
        flash(f"Erro ao listar empréstimos por usuário: {e}", "error")
        return render_template("Emprestimo/emprestimos_por_usuario.html", emprestimos=[])


@emprestimoController.route('/livro/<int:livro_id>', methods=['GET'])
def listar_por_livro(livro_id):
    try:
        emprestimos = emprestimosRepository.listarPorLivroJSON(livro_id)
        return render_template("Emprestimo/emprestimos_por_livro.html", emprestimos=emprestimos)
    except Exception as e:
        flash(f"Erro ao listar empréstimos por livro: {e}", "error")
        return render_template("Emprestimo/emprestimos_por_livro.html", emprestimos=[])
