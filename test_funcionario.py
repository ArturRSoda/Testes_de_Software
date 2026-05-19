import unittest
from funcionario import Funcionario
from excecoes import ErroNomeVazio
from projeto import Projeto
from ocorrencia import Ocorrencia
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

    def test_inserir_ocorrencia_ja_existente(self):
        funcionario = Funcionario("Felipe")
        projeto1 = Projeto("SAVI")
        projeto2 = Projeto("SAVI")

        Ocorrencia1 = Ocorrencia("BugCodigo1", "Erro ao executar codigo 1")
        Ocorrencia2 = Ocorrencia("BugCodigo1", "Erro ao executar codigo 1")

        funcionario.inserir_ocorrencia(projeto1)
        with self.assertRaises(ErroEntidadeJaExistente):
            funcionario.inserir_ocorrencia(projeto2)
