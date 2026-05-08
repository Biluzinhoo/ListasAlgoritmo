def conta_digitos(n,d):
    n = str(n)
    d = str(d)
    return n.count(d)

def eh_permutacao( a, b):
    a = str(a)
    b = str(b)

    if len(a) != len(b):
        return False
    
    for d in range (1,10):
        if conta_digitos(a,d) != conta_digitos(b, d):
            return False
    return True


a = input("Insira o valor de a: ")
b = input("Insira o valor de b: ")

if eh_permutacao(a, b):
    print(f"{a} é permutação de {b}")
else:
    print(f"{a} não é permutação de {b}")
