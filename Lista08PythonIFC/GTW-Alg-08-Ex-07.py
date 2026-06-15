def DecBinIterativo(q):
    if q == 0:
        return "0"
    resultado = ""
    while q != 0:
        r = q%2
        resultado = str(r) + resultado
        q = q//2
    return resultado
def main():
    q = int(input("Escreva um número para ser transformado em binário: "))
    print(f"O valor em binário é: {DecBinIterativo(q)}")
main()