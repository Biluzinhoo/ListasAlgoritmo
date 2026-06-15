def mdc(a,b):
    if b == 0:
        return a
    else:
        resto = a%b
        a = b
        b = resto
        return mdc(a,b)
    
def main():
    a = int(input("Informe um valor: "))
    b = int(input("Informe um valor: "))
    print(f"O mdc é: {mdc(a,b)}")

main()