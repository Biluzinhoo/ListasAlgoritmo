def isInteger(texto):

    texto = texto.strip()

    if len(texto) == 0:
        return False

    if texto[0] == "+" or texto[0] == "-":

        if len(texto) == 1:
            return False

        return texto[1:].isdigit()

    return texto.isdigit()


def main():

    valor = input("Digite uma string: ")

    if isInteger(valor):
        print("Representa um número inteiro")
    else:
        print("Não representa um número inteiro")


main()