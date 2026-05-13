import math

def hipotenusa(cateto1, cateto2):
    h = math.sqrt(cateto1**2 + cateto2**2)
    return h

def main():
    a = float(input("Digite o primeiro cateto: "))
    b = float(input("Digite o segundo cateto: "))

    resultado = hipotenusa(a, b)

    print("A hipotenusa é:", resultado)

main()