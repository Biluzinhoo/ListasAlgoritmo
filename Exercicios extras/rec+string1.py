def eh_palindromo(s):
    for letra in s:
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return eh_palindromo(s[1:-1])


def main():
    s = input("Escreva uma palavra: ")

    print(eh_palindromo(s))

main()