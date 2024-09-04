import enigma

def main():
    texto = 'Teste com um texto grande'
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    P, R = enigma.gerar_matrizes_de_permutacao(len(alfabeto))
    cripto = enigma.encriptar_enigma(texto, P, R)
    print(cripto)
    print(enigma.decriptar_enigma(cripto,P ,R ))
    
if __name__ == "__main__":
    main()