import unittest
from funcionario import Funcionario
from excecoes import ErroNomeVazio
from projeto import Projeto
from excecoes import ErroEntidadeJaExistente

class ClassTesteFuncionario(unittest.TestCase):
    def test_criaFuncionario(self):
        funcionario = Funcionario("Felipe")
        self.assertEqual(funcionario.nome, "Felipe")

    def test_criaFuncionarioNomeVazio(self):
        with self.assertRaises(ErroNomeVazio):
            funcionario = Funcionario("")

    def test_inserir_projeto_ja_existente(self):
        funcionario = Funcionario("Felipe")
        projeto1 = Projeto("SAVI")
        projeto2 = Projeto("SAVI")

        funcionario.inserir_projeto(projeto1)
        with self.assertRaises(ErroEntidadeJaExistente):
            funcionario.inserir_projeto(projeto2)