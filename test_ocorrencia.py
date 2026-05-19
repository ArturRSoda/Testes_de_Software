import unittest
from ocorrencia import Ocorrencia

class ClassTesteOcorrencia(unittest.TestCase):
    def test_criaOcorrencai(self):
        ocorrencia = Ocorrencia("BugCodigo1", "Erro ao executar codigo 1")
        self.assertEqual(ocorrencia.nome, "BugCodigo1")
        self.assertEqual(ocorrencia.resumo, "Erro ao executar codigo 1")

    def test_definir_tipo_ocorrencia(self):
        ocorrencia = Ocorrencia("BugCodigo1", "Erro ao executar codigo 1")

        ocorrencia.definir_tipo("bug")

        self.assertEqual(ocorrencia.tipo, "bug")
        with self.assertRaises(ValueError):
            ocorrencia.definir_tipo("tipo invalido")

    def test_definir_prioridade_ocorrencia(self):
        ocorrencia = Ocorrencia("BugCodigo1", "Erro ao executar codigo 1")

        ocorrencia.definir_prioridade("baixa")

        self.assertEqual(ocorrencia.prioridade, "baixa")
        with self.assertRaises(ValueError):
            ocorrencia.definir_prioridade("prioridade invalida")
