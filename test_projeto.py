import unittest
from projeto import Projeto

class ClassTesteProjeto(unittest.TestCase):
    def test_criaProjeto(self):
        projeto = Projeto("SAVI")
        self.assertEqual(projeto.nome, "SAVI")

