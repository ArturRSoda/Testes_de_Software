import unittest
from empresa import Empresa
from funcionario import Funcionario

class ClassTesteEmpresa(unittest.TestCase):
    def test_criaEmpresa(self):
        empresa = Empresa("Elton-Lmtd")
        self.assertEqual(empresa.nome, "Elton-Lmtd")

    def test_incluirFuncionario(self):
        empresa = Empresa("Elton-Lmtd")
        funcionario = Funcionario("Felipe")
        empresa.inserir_funcionario(funcionario)
        self.assertEqual(empresa.funcionarios[0].nome, "Felipe")


