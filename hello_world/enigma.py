import numpy as np
# from types import Tuple

# def gerar_matrizes_de_permutacao(N : int) -> Tuple[np.ndarray, np.ndarray]:
#     """
#     Gera duas matrizes de permutação de tamanho N x N.
#     """
#     raise NotImplementedError

# def encriptar_enigma(mensagem : str,
#               P : np.ndarray,
#               Q : np.ndarray) -> str:
#     raise NotImplementedError

# def decriptar_enigma(mensagem_encriptada : str,
#               P : np.ndarray,
#               Q : np.ndarray) -> str:
#     raise NotImplementedError

def gerar_matrizes_de_permutacao(N):
    matriz_identidade_mensagem = np.identity(N)
    P = np.random.permutation(matriz_identidade_mensagem)
    R = np.random.permutation(P)
    
    return P,R


