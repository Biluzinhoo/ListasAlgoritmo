def encaixa(a,b):
    if a.endswith(b):
        print("Encaixa")
    else:
        print("Não encaixa")
    
a = input("Insira o primeiro número: ")
b = input("Insira o segundo número: ")

encaixa(a,b)