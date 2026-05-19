from excecoes import ErroEntidadeJaExistente, ErroNomeVazio

class Funcionario:
    def __init__(self, nome):
        if (nome == ""):
            raise ErroNomeVazio("Nome de entidades nao pode ser vazio.")

        self.nome = nome
        self.projetos = list()
        self.ocorrencias = list()

    def inserir_projeto(self, projeto):
        for p in self.projetos:
            if (p.nome == projeto.nome):
                raise ErroEntidadeJaExistente("Projeto ja existente.")
        self.projetos.append(projeto)

    def inserir_ocorrencia(self, ocorrencia):
        for o in self.ocorrencias:
            if (o.nome == ocorrencia.nome):
                raise ErroEntidadeJaExistente("Ocorrencia ja existente.")
        self.ocorrencias.append(ocorrencia)

    def fechar_ocorrencia(self, ocorrencia):
        for o in self.ocorrencias:
            if (o.nome == ocorrencia.nome):
                o.estado = "fechado"
