from model import Multas
from database import database as db
from datetime import datetime

class MultasDAO:

    @staticmethod
    def obter_todas_multas():
        try:
            # Retorna todas as multas da tabela 'multas'
            return Multas.query.all()
        except Exception as e:
            print(f"Erro ao obter todas as multas: {e}")
            return []

    @staticmethod
    def gerar_multa(usuario_id, valor_multa):
        try:
            # Cria uma nova multa
            nova_multa = Multas(
                usuario_id=usuario_id,
                valor=valor_multa,
                data_geracao=datetime.now(),
                status='Pendente'
            )
            db.session.add(nova_multa)
            db.session.commit()
            return nova_multa
        except Exception as e:
            print(f"Erro ao gerar a multa: {e}")
            db.session.rollback()
            return None

    @staticmethod
    def marcar_como_pago(multa_id):
        try:
            # Marca a multa como paga
            multa = Multas.query.get(multa_id)
            if multa:
                multa.status = 'Pago'
                db.session.commit()
                return multa
            else:
                return None
        except Exception as e:
            print(f"Erro ao marcar a multa como paga: {e}")
            db.session.rollback()
            return None

    @staticmethod
    def deletar_multa(multa_id):
        try:
            # Deleta a multa
            multa = Multas.query.get(multa_id)
            if multa:
                db.session.delete(multa)
                db.session.commit()
                return True
            return False
        except Exception as e:
            print(f"Erro ao deletar a multa: {e}")
            db.session.rollback()
            return False
