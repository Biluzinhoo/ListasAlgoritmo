def repeticao(palavra):
    palavra.lower()
    if len(palavra) == len(set(palavra)):
        return True
    else:
        return False

def main():
    palavra = input("Escreva uma palavra: ")
    print(repeticao(palavra))

main()