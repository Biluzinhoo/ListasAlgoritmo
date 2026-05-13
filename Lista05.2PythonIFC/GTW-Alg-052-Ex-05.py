def numero_ordinal(n):

    if n == 1:
        return "primeiro"
    elif n == 2:
        return "segundo"
    elif n == 3:
        return "terceiro"
    elif n == 4:
        return "quarto"
    elif n == 5:
        return "quinto"
    elif n == 6:
        return "sexto"
    elif n == 7:
        return "sétimo"
    elif n == 8:
        return "oitavo"
    elif n == 9:
        return "nono"
    elif n == 10:
        return "décimo"
    elif n == 11:
        return "décimo primeiro"
    elif n == 12:
        return "décimo segundo"
    else:
        return ""


def main():

    numero = int(input("Digite um número de 1 a 12: "))

    resultado = numero_ordinal(numero)

    if resultado == "":
        print("Número inválido")
    else:
        print(numero, "-", resultado)


main()