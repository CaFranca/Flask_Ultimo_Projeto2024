from datetime import datetime
from database import database
from model import Multas

class MultasDAO:
    def obter_todas_multas(self):
        return database.session.query(Multas).all()

    def gerar_multa(self, usuario_id, valor_multa, emprestimo_id):
        # Gera uma nova multa associada ao empréstimo
        multa = Multas(usuario_id=usuario_id, valor=valor_multa, data_geracao=datetime.now(), status="pendente", emprestimo_id=emprestimo_id)
        database.session.add(multa)
        database.session.commit()

    def marcar_como_pago(self, multa_id):
        multa = database.session.query(Multas).filter(Multas.id == multa_id).first()
        if multa:
            multa.status = "paga"
            database.session.commit()
            return True
        return False

    def deletar_multa(self, multa_id):
        multa = database.session.query(Multas).filter(Multas.id == multa_id).first()
        if multa:
            database.session.delete(multa)
            database.session.commit()
            return True
        return False
