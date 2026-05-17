import unittest
from projeto import Projeto
from excecoes import ErroNomeVazio

class ClassTesteProjeto(unittest.TestCase):
    def test_criaProjeto(self):
        projeto = Projeto("SAVI")
        self.assertEqual(projeto.nome, "SAVI")

    def test_criaProjetoNomeVazio(self):
        with self.assertRaises(ErroNomeVazio):
            projeto = Projeto("")
