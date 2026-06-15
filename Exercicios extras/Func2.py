def eh_palindromo(palavra):
    palavra_legal=palavra.lower().replace(" ","")
    texto_invertido = palavra_legal[::-1]
    if texto_invertido == palavra_legal:
        return True
    else:
        return False


def main():
    palavra = input("Escreva uma palavra: ")
    print(eh_palindromo(palavra))

main()