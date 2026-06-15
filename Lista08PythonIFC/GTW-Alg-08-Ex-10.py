def decod(lista):
    if lista == []:
        return []
    valor = lista[0]
    quantidade = lista[1]
    resultado = [valor] * quantidade
    return resultado + decod(lista[2:])

def main():
    lista = ["A", 12, "B", 4, "A", 6, "B", 1]
    print(f"Lista codificada: {lista}")
    print(f"Lista descodificada: {decod(lista)}")

main()