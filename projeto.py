from excecoes import ErroEntidadeJaExistente, ErroNomeVazio

class Projeto:
    def __init__(self, nome):
        if (nome == ""):
            raise ErroNomeVazio("Nome de entidades nao pode ser vazio.")
        self.nome = nome
        self.funcionarios = list()
        self.ocorrencias = list()

    def inserir_funcionario(self, funcionario):
        for f in self.funcionarios:
            if (f.nome == funcionario.nome):
                raise ErroEntidadeJaExistente("Funcionario ja existente.")
        self.funcionarios.append(funcionario)

    def inserir_ocorrencia(self, ocorrencia):
        for o in self.ocorrencias:
            if (o.nome == ocorrencia.nome):
                raise ErroEntidadeJaExistente("Projeto ja existente.")
        self.ocorrencias.append(ocorrencia)
