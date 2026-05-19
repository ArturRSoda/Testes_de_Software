import unittest
from empresa import Empresa
from funcionario import Funcionario
from projeto import Projeto
from ocorrencia import Ocorrencia
from excecoes import ErroNomeVazio, ErroEntidadeJaExistente

class ClassTesteEmpresa(unittest.TestCase):
    def test_criaEmpresa(self):
        empresa = Empresa("Elton-Lmtd")
        self.assertEqual(empresa.nome, "Elton-Lmtd")

    def test_criaEmpresaNomeVazio(self):
        with self.assertRaises(ErroNomeVazio):
            empresa = Empresa("")

    def test_incluirFuncionario(self):
        empresa = Empresa("Elton-Lmtd")
        funcionario = Funcionario("Felipe")
        empresa.inserir_funcionario(funcionario)
        self.assertEqual(empresa.funcionarios[0].nome, "Felipe")

    def test_incluirProjeto(self):
        empresa = Empresa("Elton-Lmtd")
        projeto = Projeto("SAVI")
        empresa.inserir_projeto(projeto)
        self.assertEqual(empresa.projetos[0].nome, "SAVI")

    def test_incluirFuncionarioEmProjeto(self):
        empresa = Empresa("Elton-Lmtd")
        funcionario = Funcionario("Felipe")
        projeto = Projeto("SAVI")
        empresa.inserir_funcionario(funcionario)
        empresa.inserir_projeto(projeto)

        empresa.inserir_funcionario_em_projeto(funcionario, projeto)
        self.assertEqual(projeto.funcionarios[0].nome, "Felipe")


    def test_verificarProjetoEmFuncionario(self):
        empresa = Empresa("Elton-Lmtd")
        funcionario = Funcionario("Felipe")
        projeto = Projeto("SAVI")
        empresa.inserir_funcionario(funcionario)
        empresa.inserir_projeto(projeto)

        empresa.inserir_funcionario_em_projeto(funcionario, projeto)
        self.assertEqual(funcionario.projetos[0].nome, projeto.nome)

    def test_inserir_funcionario_ja_existente(self):
        empresa = Empresa("Elton-Lmtd")
        funcionario1 = Funcionario("Felipe")
        funcionario2 = Funcionario("Felipe")

        empresa.inserir_funcionario(funcionario1)
        with self.assertRaises(ErroEntidadeJaExistente):
            empresa.inserir_funcionario(funcionario2)

    def test_inserir_projeto_ja_existente(self):
        empresa = Empresa("Elton-Lmtd")
        projeto1 = Projeto("SAVI")
        projeto2 = Projeto("SAVI")

        empresa.inserir_projeto(projeto1)
        with self.assertRaises(ErroEntidadeJaExistente):
            empresa.inserir_projeto(projeto2)

    def test_inserirFuncionarioEmProjetoJaInserido(self):
        empresa = Empresa("Elton-Lmtd")
        funcionario = Funcionario("Felipe")
        projeto = Projeto("SAVI")
        empresa.inserir_funcionario(funcionario)
        empresa.inserir_projeto(projeto)

        empresa.inserir_funcionario_em_projeto(funcionario, projeto)
        with self.assertRaises(ErroEntidadeJaExistente):
            empresa.inserir_funcionario_em_projeto(funcionario, projeto)

    def test_InserirOcorrencia(self):
        empresa = Empresa("Elton-Lmtd")
        funcionario = Funcionario("Felipe")
        projeto = Projeto("SAVI")
        ocorrencia = Ocorrencia("BugCodigo1", "Erro ao executar codigo 1")

        empresa.inserir_funcionario(funcionario)
        empresa.inserir_projeto(projeto)
        empresa.inserir_funcionario_em_projeto(funcionario, projeto)

        empresa.inserir_ocorrencia_em_projeto(ocorrencia, projeto, funcionario)

        self.assertEqual(projeto.ocorrencias[0].nome, "BugCodigo1")
        self.assertEqual(funcionario.ocorrencias[0].nome , "BugCodigo1")

    def test_InserirOcorrenciaEmProjetoSemFuncionarioRelacionado(self):
        empresa = Empresa("Elton-Lmtd")
        funcionario = Funcionario("Felipe")
        projeto = Projeto("SAVI")
        ocorrencia = Ocorrencia("BugCodigo1", "Erro ao executar codigo 1")

        empresa.inserir_funcionario(funcionario)
        empresa.inserir_projeto(projeto)
        # empresa.inserir_funcionario_em_projeto(funcionario, projeto)

        empresa.inserir_ocorrencia_em_projeto(ocorrencia, projeto, funcionario)

        self.assertEqual(len(projeto.ocorrencias), 0)
        self.assertEqual(len(funcionario.ocorrencias), 0)

