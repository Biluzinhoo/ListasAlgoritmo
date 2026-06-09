lista_pala = []

while True:
    palavra = input("Digite uma palavra: ")

    if palavra == "":
        for n in lista_pala:
            print(n)
        break
    else:
        if palavra not in lista_pala:
            lista_pala.append(palavra)

            
