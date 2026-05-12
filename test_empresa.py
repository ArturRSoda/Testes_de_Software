import unittest
from empresa import Empresa

class ClassTesteEmpresa(unittest.TestCase):
    def test_criaEmpresa(self):
        empresa = Empresa("Elton-Lmtd")
        self.assertEqual(empresa.name, "Elton-Lmtd")

