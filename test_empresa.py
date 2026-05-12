import unittest
from empresa import Empresa
from funcionario import Funcionario
from projeto import Projeto

class ClassTesteEmpresa(unittest.TestCase):
    def test_criaEmpresa(self):
        empresa = Empresa("Elton-Lmtd")
        self.assertEqual(empresa.nome, "Elton-Lmtd")

    def test_incluirFuncionario(self):
        empresa = Empresa("Elton-Lmtd")
        funcionario = Funcionario("Felipe")
        empresa.inserir_funcionario(funcionario)
        self.assertEqual(empresa.funcionarios[0].nome, "Felipe")

    def test_incluirProjeto(self):
        empresa = Empresa("Elton-Lmtd")
        projeto = Projeto("SAVI")
        empresa.inserir_projeto(projeto)
        self.assertEqual(empresa.projetos[0].nome, "SAVI")


