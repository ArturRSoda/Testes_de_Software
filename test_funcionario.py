import unittest
from funcionario import Funcionario
from excecoes import ErroNomeVazio
from projeto import Projeto
from ocorrencia import Ocorrencia
from excecoes import ErroEntidadeJaExistente, ErroMuitasOcorrencias

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

        ocorrencia = Ocorrencia("BugCodigo1", "Erro ao executar codigo 1")

        funcionario.inserir_ocorrencia(ocorrencia)
        with self.assertRaises(ErroEntidadeJaExistente):
            funcionario.inserir_ocorrencia(ocorrencia)

    def test_inserir_mais_de_10_ocorrencia_abertas(self):


        funcionario = Funcionario("Felipe")
        for i in range(10):
            ocorrencia = Ocorrencia(f"BugCodigo{i}", f"Erro ao executar codigo {i}")
            funcionario.inserir_ocorrencia(ocorrencia)


        ocorrencia = Ocorrencia(f"BugCodigo11", f"Erro ao executar codigo 11")
        with self.assertRaises(ErroMuitasOcorrencias):
            funcionario.inserir_ocorrencia(ocorrencia)

        funcionario.fechar_ocorrencia(funcionario.ocorrencias[0])
        funcionario.inserir_ocorrencia(ocorrencia)

        self.assertEqual(funcionario.ocorrencias[-1].nome, "BugCodigo11")
