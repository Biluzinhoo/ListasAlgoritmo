def encaixa(a, b):

    if b in a:
        print(f"{b} é segmento de {a}")
    else:
        print("Um não é segmento do outro")


a = input("Insira o primeiro número: ")
b = input("Insira o segundo número: ")


# Descobre qual é o maior
if len(a) >= len(b):
    encaixa(a, b)
else:
    encaixa(b, a)