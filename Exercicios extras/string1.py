def conta_vogais(palavra):
    contador = 0
    for char in palavra:
        if char in "aeiou":
            contador += 1
    return contador

def main():
    palavra = input("Escreva uma palavra: ")
    print(f"a quantidade de vogais é: {conta_vogais(palavra)}")

main()