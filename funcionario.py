from excecoes import ErroNomeVazio

class Funcionario:
    def __init__(self, nome):
        if (nome == ""):
            raise ErroNomeVazio("Nome de entidades nao pode ser vazio.")

        self.nome = nome
        self.projetos = list()

    def inserir_projeto(self, projeto):
        self.projetos.append(projeto)
