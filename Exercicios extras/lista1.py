def soma_pares(numeros):
    soma = 0
    for numero in numeros:
        if numero%2 == 0:
            soma += numero
    return soma
def main():
    numeros = []
    while True: 
        num = input("Informe números: ")
        if num == "":
            break
        numeros.append(int(num))
    print(f"A soma dos valores pares é: {soma_pares(numeros)}")
main()
