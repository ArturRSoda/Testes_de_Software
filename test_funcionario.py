import unittest
from funcionario import Funcionario

class ClassTesteFuncionario(unittest.TestCase):
    def test_criaFuncionario(self):
        funcionario = Funcionario("Felipe")
        self.assertEqual(funcionario.nome, "Felipe")

