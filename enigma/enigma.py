import numpy as np

import numpy as np
'''
Essa função gera duas matrizes de permutação da matriz identidade.
'''
def gerar_matrizes_de_permutacao(N):
    matriz_identidade = np.identity(N)
    P = np.random.permutation(matriz_identidade)
    R = np.random.permutation(matriz_identidade)
    return P, R

'''
Essa função encripta a mensagem.
'''
def encriptar_enigma(mensagem, P, R):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    mensagem = mensagem.lower()
    alfabeto_len = len(alfabeto)
    matriz_alfabeto = np.identity(alfabeto_len)
    lista_index_caracteres_mensagem= []
    for caracter_mensagem in mensagem:
        index_caracter = alfabeto.index(caracter_mensagem) # Encontra o índice do caractere no alfabeto
        lista_index_caracteres_mensagem.append(index_caracter) # Adiciona o índice à lista
    # Constrói uma matriz onde cada coluna corresponde a um caractere da mensagem
    mensagem_matriz = matriz_alfabeto[:,lista_index_caracteres_mensagem]
    mensagem_codificada = []
    for i in range(len(mensagem_matriz[0])):
        if i==0:
            # Para o primeiro caractere, aplica diretamente a matriz P
            letra_codificada = P @ mensagem_matriz[:,i]
        else:
            # Para os caracteres subsequentes, aplica P multiplicado por R iterativamente
            cod = P
            for p in range(i):
                cod = R@cod
            letra_codificada = cod@mensagem_matriz[:,i] # Aplica a transformação ao caractere atual
        mensagem_codificada.append(letra_codificada) # Adiciona o vetor codificado à lista 
    
    mensagem_final = ''
    for codificado in mensagem_codificada:
        index_letra = np.argmax(codificado) # Encontra o índice do maior valor no vetor codificado
        mensagem_final += alfabeto[index_letra] # Converte o índice de volta para um caractere
    
    return mensagem_final



def decriptar_enigma(mensagem_encriptada,P ,Q ):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    mensagem = mensagem_encriptada.lower()
    alfabeto_len = len(alfabeto)
    matriz_alfabeto = np.identity(alfabeto_len)
    lista_index_caracteres_mensagem= []
    for caracter_mensagem in mensagem:
        index_caracter = alfabeto.index(caracter_mensagem) # Encontra o índice do caractere no alfabeto
        lista_index_caracteres_mensagem.append(index_caracter) # Adiciona o índice à lista
    # Constrói uma matriz onde cada coluna corresponde a um caractere da mensagem encriptada
    mensagem_matriz = matriz_alfabeto[:,lista_index_caracteres_mensagem]
    mensagem_decriptada = []
    inverso_P = np.linalg.inv(P)
    inverso_Q = np.linalg.inv(Q)
    for i in range(len(mensagem_matriz[0])):
        if i==0:
            # Para o primeiro caractere, aplica diretamente a matriz inversa de P
            letra_codificada = inverso_P @ mensagem_matriz[:,i]
        else:
            # Para os caracteres subsequentes, aplica a matriz inversa de P multiplicada por Q iterativamente
            cod = inverso_P
            for p in range(i):
                cod = cod@inverso_Q
            letra_codificada = cod@mensagem_matriz[:,i] # Aplica a transformação inversa ao caractere atual
        mensagem_decriptada.append(letra_codificada)  # Adiciona o vetor decodificado à lista  
    
    mensagem_final = ''
    for codificado in mensagem_decriptada:
        index_letra = np.argmax(codificado) # Encontra o índice do maior valor no vetor decodificado
        mensagem_final += alfabeto[index_letra]  # Converte o índice de volta para um caractere
    
    return mensagem_final
