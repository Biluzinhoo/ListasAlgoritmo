def mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a

def main():
    a = int(input("Escrva uma vlaora para a: "))
    b = int(input("Informe um valor para b: "))
    print(mdc(a,b))
main()
