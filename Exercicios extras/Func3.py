def soma_digitos(num):
    soma = 0
    while num > 0:
        digito = num%10
        soma += digito
        num = num//10
    
    return soma

    


def main():
    num = int(input("Escreva um número: "))
    print(soma_digitos(num))

main()