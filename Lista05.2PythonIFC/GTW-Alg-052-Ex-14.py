def data_magica(dia, mes, ano):

    ultimos_digitos = ano % 100

    if dia * mes == ultimos_digitos:
        return True
    else:
        return False


def main():

    print("Datas mágicas do século XX:\n")

    for ano in range(1900, 2000):

        for mes in range(1, 13):

            for dia in range(1, 32):

                if data_magica(dia, mes, ano):
                    print(f"{dia:02d}/{mes:02d}/{ano}")


main()