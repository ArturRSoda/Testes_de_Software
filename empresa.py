class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = list()
        self.projetos = []

    def inserir_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def inserir_projeto(self, projeto):
        self.projetos.append(projeto)

