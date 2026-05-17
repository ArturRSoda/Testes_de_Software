from excecoes import ErroNomeVazio

class Empresa:
    def __init__(self, nome):
        if (nome == ""):
            raise ErroNomeVazio("Nome de entidades nao pode ser vazio.")

        self.nome = nome
        self.funcionarios = list()
        self.projetos = []

    def inserir_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def inserir_projeto(self, projeto):
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

