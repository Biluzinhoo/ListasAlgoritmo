def ordem(lista):
    crescente = sorted(lista)
    decrescente = sorted(lista, reverse=True)
    if len(lista) == 0 or len(lista) == 1:
        return True
    else:
        if lista == crescente or lista == decrescente:
            return True
        else:
            return False

def main():
    lista = []
    while True:
        num = input("Informe valores: ")
        if num == "":
            break
        num = float(num)
        lista.append(num)
    resultado = ordem(lista)
    print(resultado)

main()