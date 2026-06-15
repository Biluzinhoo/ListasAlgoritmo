def DecBinIterativo(q):
    if q == 0:
        return "0"
    if q == 1:
        return "1"
    if q != 0 or q != 1:     
        return DecBinIterativo(q//2) + str(q%2)
def main():
    q = int(input("Escreva um número para ser transformado em binário: "))
    if q < 0: 
        print("Erro, colocar número inteiro positivo")
    print(f"O valor em binário é: {DecBinIterativo(q)}")
main()