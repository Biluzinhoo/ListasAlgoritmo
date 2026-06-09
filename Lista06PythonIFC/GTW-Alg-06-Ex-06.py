def divisores (n):
    numeros = []
    i=1
    while i < n:
        if n%i==0:
            numeros.append(i)
        i =i+1

    return numeros


def main():
    n = int(input("Escreva um número para descobrir seus divisores: "))
    resultado = divisores(n)
    for x in resultado:
        print(x)

main()
