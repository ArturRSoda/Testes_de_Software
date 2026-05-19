class ErroNomeVazio(Exception):
    """Erro de nome vazio."""
    pass

class ErroEntidadeJaExistente(Exception):
    """Erro de insercao de entidade ja existente."""
    pass

class ErroOcorrenciaFechada(Exception):
    """Erro de ocorrencia ja foi fechada"""
    pass
