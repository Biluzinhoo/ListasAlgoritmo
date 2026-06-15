def conta_letras(palavra):
    contagem = {}
    for letra in palavra:
        if letra in contagem:
            contagem[letra] +=1
        else:
            contagem[letra] = 1
    return contagem


def main():
    palavra = input("Escreva uma palavra: ")
    print(conta_letras(palavra))
main()