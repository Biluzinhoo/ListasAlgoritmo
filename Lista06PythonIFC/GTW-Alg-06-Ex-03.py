def remover (lista,n):
    copia = sorted(lista)
    return copia [n:len(copia)-n]

def main():
    numeros = []
    print("Digite os números: ")

    while True: 
        num = input("Número: ")
        if num == "":
            break
        numeros.append(float(num))
    if len(numeros) < 4:
        print("Erro, Insira pelo menos 4 valores")

        return
    sem_extremos = remover(numeros,2)
    print(f"Lista sem os extremos: {sem_extremos} ")
    print(f"Lista sem alteração: {numeros}")


main()
