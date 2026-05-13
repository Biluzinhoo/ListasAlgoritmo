def bissexto(ano):

    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False


def dias_no_mes(mes, ano):

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30

    elif mes == 2:

        if bissexto(ano):
            return 29
        else:
            return 28

    else:
        return 0


def main():

    mes = int(input("Digite o mês (1 a 12): "))
    ano = int(input("Digite o ano: "))

    dias = dias_no_mes(mes, ano)

    if dias == 0:
        print("Mês inválido")
    else:
        print("Quantidade de dias:", dias)


main()