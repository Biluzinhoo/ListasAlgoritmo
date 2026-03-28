lugar = input("Informe uma posição no tabuleiro de xadrez: ").lower()

coluna = ord(lugar[0]) - ord("a")
linha = int(lugar[1]) - 1

if coluna+linha % 2 == 0:
    print(f"A posição é um quadrado preto")
else:
    print(f"A posição é um quadrado branco")
