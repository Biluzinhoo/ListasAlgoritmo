def maior_e_posicao(numeros):
    maior = numeros[0]
    for i in range(len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i]
            posicao = i
    return maior, posicao

def main():
    numeros = []
    while True:
        num = input("Inform valores para a lista: ")
        if num == "":
            break
        numeros.append(int(num))
    maior, posicao = maior_e_posicao(numeros)
    print(f"O maior valor foi: {maior}. E a sua posição foi: {posicao}")
main() 