class Ocorrencia:
    def __init__(self, nome, resumo):
        self.nome = nome
        self.resumo = resumo
        self.estado = "aberto"
        self.tipo = "NA"

    def definir_tipo(self, tipo):
        if tipo not in ("bug", "tarefa", "refatoracao", "NA"):
            raise ValueError("Tipo de ocorrencia invalido")

        self.tipo = tipo
