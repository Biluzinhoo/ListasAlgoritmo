def conjunção (lista):
    if len(lista)==0:
        return ""
    elif len(lista)==1:
        return lista[0]
    elif len(lista) == 2:
        return print(f"{lista[0]} e {lista[1]}")
    else:
        return ", ".join(lista[:-1])+ " e " +lista[-1]
    

def main():
    lista = []
    while True:
        palavras = input("Informe palavras: ")
        if palavras == "":
            break
        lista.append(palavras)
    resultado = conjunção(lista)
    print(resultado)
main()
