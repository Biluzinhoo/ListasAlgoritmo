def primo(numero):

    if numero < 2:
        return False

    for i in range(2, numero):

        if numero % i == 0:
            return False

    return True


def main():

    n = int(input("Digite um número inteiro positivo: "))

    if primo(n):
        print("O número é primo")
    else:
        print("O número não é primo")


main()