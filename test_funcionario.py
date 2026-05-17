import unittest
from funcionario import Funcionario
from excecoes import ErroNomeVazio

class ClassTesteFuncionario(unittest.TestCase):
    def test_criaFuncionario(self):
        funcionario = Funcionario("Felipe")
        self.assertEqual(funcionario.nome, "Felipe")

    def test_criaFuncionarioNomeVazio(self):
        with self.assertRaises(ErroNomeVazio):
            funcionario = Funcionario("")