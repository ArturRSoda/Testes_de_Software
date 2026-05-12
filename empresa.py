class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = list()

    def inserir_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

