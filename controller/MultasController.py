from flask import Blueprint, request, redirect, url_for, render_template, flash
from repository import MultasRepository
from repository import EmprestimosRepository

multasController = Blueprint('bp_multas', __name__)
multasRepository = MultasRepository()

@multasController.route('/listar', methods=['GET'])
def listar_multas():
    try:
        # Busca todas as multas, sem filtrar por usuário
        multas = multasRepository.obter_todas_multas()
        return render_template("Multas/mulltas.html", multas=multas)
    except Exception as e:
        flash(f"Erro ao carregar as multas: {e}", "error")
        print(f"Erro ao carregar as multas: {e}")
        return render_template("Multas/mulltas.html", multas=[])


@multasController.route('/gerar/<int:emprestimo_id>', methods=['GET'])
def gerar_multa(emprestimo_id):
    try:
        # Busca o empréstimo para determinar o atraso
        emprestimo = EmprestimosRepository.buscarEmprestimoPorId(emprestimo_id)
        
        if not emprestimo:
            flash("Empréstimo não encontrado.", "error")
            return redirect(url_for('bp_loan.view_emprestimos'))

        # Verifica a data de devolução real e gera a multa, se necessário
        if emprestimo.data_devolucao_real and emprestimo.data_devolucao_real > emprestimo.data_devolucao_prevista:
            dias_atraso = (emprestimo.data_devolucao_real - emprestimo.data_devolucao_prevista).days
            if dias_atraso > 0:
                valor_multa = (dias_atraso // 5) * 10  # Multa de 10 por cada 5 dias de atraso
                multa = multasRepository.gerar_multa(emprestimo.usuario_id, valor_multa)
                flash(f"Multa gerada: {valor_multa} para o usuário {emprestimo.usuario_id}", "success")
            else:
                flash("O empréstimo foi devolvido no prazo ou antes.", "info")
        else:
            flash("A devolução ainda não foi realizada.", "warning")

        return redirect(url_for('bp_loan.view_emprestimos'))

    except Exception as e:
        flash(f"Erro ao gerar a multa: {e}", "error")
        return redirect(url_for('bp_loan.view_emprestimos'))


@multasController.route('/pagar/<int:multa_id>', methods=['GET'])
def pagar_multa(multa_id):
    try:
        # Marca a multa como paga
        multa = multasRepository.marcar_como_pago(multa_id)
        
        if multa:
            flash(f"Multa de ID {multa_id} paga com sucesso!", "success")
        else:
            flash("Erro ao pagar a multa.", "error")

        return redirect(url_for('bp_multas.listar_multas'))

    except Exception as e:
        flash(f"Erro ao pagar a multa: {e}", "error")
        return redirect(url_for('bp_multas.listar_multas'))


@multasController.route('/excluir/<int:multa_id>', methods=['GET', 'POST'])
def excluir_multa(multa_id):
    try:
        # Exclui a multa
        response = multasRepository.deletar_multa(multa_id)
        if response:  # Supondo que `response` seja um booleano (True/False)
            flash("Multa excluída com sucesso!", "success")
        else:
            flash("Erro ao excluir a multa.", "error")

        return redirect(url_for('bp_multas.listar_multas'))
    except Exception as e:
        flash(f"Erro ao excluir multa: {e}", "error")
        return redirect(url_for('bp_multas.listar_multas'))
