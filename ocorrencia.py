class Ocorrencia:
    def __init__(self, nome, resumo):
        self.nome = nome
        self.resumo = resumo
        self.estado = "aberto"
        self.tipo = "NA"
        self.prioridade = "NA"

    def definir_tipo(self, tipo):
        if tipo not in ("bug", "tarefa", "refatoracao", "NA"):
            raise ValueError("Tipo de ocorrencia invalido")

        self.tipo = tipo

    def definir_prioridade(self, prioridade):
        if prioridade not in ("baixa", "media", "alta", "NA"):
            raise ValueError("Prioridade de ocorrencia invalido")

        self.prioridade = prioridade 
