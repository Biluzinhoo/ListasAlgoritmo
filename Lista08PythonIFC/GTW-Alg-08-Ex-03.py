def eh_palindromo (s):
    s_limpo = "".join([char for char in s if char.isalnum()]).lower() 
    if len(s_limpo) <= 1:
        return True
    if s_limpo[0] != s_limpo[-1]:
        return False
    return eh_palindromo(s_limpo[1:-1])

def main():
    s = input("Escrav uma frase ou palavra: ")
    print(eh_palindromo(s))

main() 
