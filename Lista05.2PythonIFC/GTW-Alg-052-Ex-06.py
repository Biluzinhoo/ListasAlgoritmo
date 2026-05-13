def centralizar(texto, largura):

    espacos = (largura - len(texto)) // 2

    if espacos < 0:
        espacos = 0

    return " " * espacos + texto


def main():

    frase = input("Digite uma frase: ")
    largura = int(input("Digite a largura da linha: "))

    resultado = centralizar(frase, largura)

    print(resultado)


main()