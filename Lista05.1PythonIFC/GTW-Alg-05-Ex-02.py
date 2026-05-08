
def imprime_n_vezes(nome, n):
    i = 0
    while i < n:
        print(nome)
        i+= 1

nome = input("Escreva um nome para ser repitido: ")
n = int(input("Insira o valor a ser repitido: "))
imprime_n_vezes(nome, n)