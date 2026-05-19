import unittest
from ocorrencia import Ocorrencia

class ClassTesteOcorrencia(unittest.TestCase):
    def test_criaOcorrencai(self):
        ocorrencia = Ocorrencia("BugCodigo1", "Erro ao executar codigo 1")
        self.assertEqual(ocorrencia.nome, "Felipe")
        self.assertEqual(ocorrencia.resumo, "Erro ao executar codigo 1")

