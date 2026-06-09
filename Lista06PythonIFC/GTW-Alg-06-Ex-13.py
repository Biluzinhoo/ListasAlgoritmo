def countRange(lista, minimo, maximo):
    contador = 0
    for n in lista:
        if n >= minimo and n < maximo:
            contador += 1
    return contador
 
 
def main():
    lista = []
 
    print("Digite os números (Enter em branco para parar):")
    while True:
        num = input("Número: ")
        if num == "":
            break
        lista.append(float(num))
 
    minimo = float(input("Valor mínimo: "))
    maximo = float(input("Valor máximo: "))
 
    resultado = countRange(lista, minimo, maximo)
    print(f"\nQuantidade de elementos entre {minimo} e {maximo}: {resultado}")
 
 
main()