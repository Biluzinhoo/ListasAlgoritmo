def inverte_numero(n):
    n_invertido = 0
    while n > 0:
        digito = n%10
        n_invertido = n_invertido *10 +digito
        n=n//10
    return n_invertido

def main():
    n = int(input("Escreva um número: "))
    print(f"O valor invertido desse número é: {inverte_numero(n)}")

main()