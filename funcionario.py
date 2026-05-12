class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        self.projetos = list()

    def inserir_projeto(self, projeto):
        self.projetos.append(projeto)
