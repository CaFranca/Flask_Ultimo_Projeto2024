from DAO import MultasDAO

class MultasRepository:

    def __init__(self):
        self.dao = MultasDAO()

    def obter_todas_multas(self):
        return self.dao.obter_todas_multas()

    def gerar_multa(self, usuario_id, valor_multa):
        return self.dao.gerar_multa(usuario_id, valor_multa)

    def marcar_como_pago(self, multa_id):
        return self.dao.marcar_como_pago(multa_id)

    def deletar_multa(self, multa_id):
        return self.dao.deletar_multa(multa_id)