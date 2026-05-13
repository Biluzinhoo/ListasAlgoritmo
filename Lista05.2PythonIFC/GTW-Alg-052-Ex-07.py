def triangulo(a, b, c):

    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False


def main():

    lado1 = float(input("Digite o primeiro lado: "))
    lado2 = float(input("Digite o segundo lado: "))
    lado3 = float(input("Digite o terceiro lado: "))

    if triangulo(lado1, lado2, lado3):
        print("É possível formar um triângulo")
    else:
        print("Não é possível formar um triângulo")


main()