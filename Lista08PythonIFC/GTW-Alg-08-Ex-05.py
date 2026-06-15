def somatudo():
    n = input("Escreva um número: ")
    if n == "":
        return (0, 0)
    soma, contagem = somatudo()
    return (soma + int(n), contagem + 1)

soma, contagem = somatudo()
if contagem == 0:
    print("0,0")
else:
    print(soma)