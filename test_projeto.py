import unittest
from projeto import Projeto
from funcionario import Funcionario
from ocorrencia import Ocorrencia
from excecoes import ErroNomeVazio, ErroEntidadeJaExistente

class ClassTesteProjeto(unittest.TestCase):
    def test_criaProjeto(self):
        projeto = Projeto("SAVI")
        self.assertEqual(projeto.nome, "SAVI")

    def test_criaProjetoNomeVazio(self):
        with self.assertRaises(ErroNomeVazio):
            projeto = Projeto("")

    def test_inserir_funcionario_ja_existente(self):
        projeto = Projeto("SAVI")
        funcionario1 = Funcionario("Felipe")
        funcionario2 = Funcionario("Felipe")

        projeto.inserir_funcionario(funcionario1)
        with self.assertRaises(ErroEntidadeJaExistente):
            projeto.inserir_funcionario(funcionario2)

    def test_inserir_ocorrencia_ja_existente(self):
        projeto = Projeto("SAVI")

        ocorrencia = Ocorrencia("BugCodigo1", "Erro ao executar codigo 1")

        projeto.inserir_ocorrencia(ocorrencia)
        with self.assertRaises(ErroEntidadeJaExistente):
            projeto.inserir_ocorrencia(ocorrencia)
