from excecoes import ErroEntidadeJaExistente, ErroNomeVazio, ErroOcorrenciaFechada

class Empresa:
    def __init__(self, nome):
        if (nome == ""):
            raise ErroNomeVazio("Nome de entidades nao pode ser vazio.")

        self.nome = nome
        self.funcionarios = list()
        self.projetos = []

    def inserir_funcionario(self, funcionario):
        for f in self.funcionarios:
            if (f.nome == funcionario.nome):
                raise ErroEntidadeJaExistente("Funcionario ja existente.")
        self.funcionarios.append(funcionario)

    def inserir_projeto(self, projeto):
        for p in self.projetos:
            if (p.nome == projeto.nome):
                raise ErroEntidadeJaExistente("Projeto ja existente.")
        self.projetos.append(projeto)

    def inserir_funcionario_em_projeto(self, funcionario, projeto):
        for f in self.funcionarios:
            if (f == funcionario):
                tmp_f = f
                break
        
        for p in self.projetos:
            if (p == projeto):
                tmp_p = p
                break;


        tmp_p.inserir_funcionario(tmp_f)
        tmp_f.inserir_projeto(tmp_p)



    def inserir_ocorrencia_em_projeto(self, ocorrencia, projeto, funcionario):
        for f in self.funcionarios:
            if (f == funcionario):
                tmp_f = f
                break
        
        for p in self.projetos:
            if (p == projeto):
                tmp_p = p
                break;


        if (tmp_p not in tmp_f.projetos):
            return

        tmp_p.inserir_ocorrencia(ocorrencia)
        tmp_f.inserir_ocorrencia(ocorrencia)

    def mudar_responsavel(self, funcionario_velho, funcionario_novo, ocorrencia):
        for f in self.funcionarios:
            if (f == funcionario_velho):
                tmp_f = f
                break

        if (ocorrencia.estado == "fechado"):
            raise ErroOcorrenciaFechada("Ocorrencia ja fechada")

        tmp_f.ocorrencias.remove(ocorrencia)
        funcionario_novo.inserir_ocorrencia(ocorrencia)


