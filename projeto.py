from excecoes import ErroEntidadeJaExistente, ErroNomeVazio

class Projeto:
    def __init__(self, nome):
        if (nome == ""):
            raise ErroNomeVazio("Nome de entidades nao pode ser vazio.")
        self.nome = nome
        self.funcionarios = list()

    def inserir_funcionario(self, funcionario):
        for f in self.funcionarios:
            if (f.nome == funcionario.nome):
                raise ErroEntidadeJaExistente("Funcionario ja existente.")
        self.funcionarios.append(funcionario)

