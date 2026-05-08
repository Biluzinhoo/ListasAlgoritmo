def conta_digitos(n,d):
    n = str(n)
    d = str(d)
    return n.count(d)

n = int(input("Insira o número: "))
d = int(input("Insira o dígito: "))
if d < 0 or d > 9:
    print("Erro, dígitos aceitos entre 0 e 9")
else:   
    quantidade = conta_digitos(n,d)


    print(f"O dígito {d} apareceu {quantidade} vezes")
    