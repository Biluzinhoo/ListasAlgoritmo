import random

def gerar_senha():

    tamanho = random.randint(7, 10)

    senha = ""

    for i in range(tamanho):

        codigo = random.randint(33, 126)

        senha += chr(codigo)

    return senha


def main():

    senha = gerar_senha()

    print("Senha gerada:", senha)


main()