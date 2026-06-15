def cod(lista):
    if lista == []:
        return []
    if len(lista) == 1 or lista[0] != lista[1]:
        return [lista[0], 1] + cod(lista[1:])
    resto = cod(lista[1:])
    return [resto[0], resto[1] + 1] + resto[2:]

def main():
    entrada = input("Digite os valores separados por espaço: ")
    lista = entrada.split()
    print(f"Lista original: {lista}")
    print(f"Lista codificada: {cod(lista)}")

main()