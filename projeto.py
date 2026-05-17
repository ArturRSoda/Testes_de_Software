from excecoes import ErroNomeVazio

class Projeto:
    def __init__(self, nome):
        if (nome == ""):
            raise ErroNomeVazio("Nome de entidades nao pode ser vazio.")
        self.nome = nome
        self.funcionarios = list()

    def inserir_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

