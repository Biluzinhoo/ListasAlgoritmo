lado = int(input("Informe o número de lados do polígono: "))

if lado <= 2 or lado > 10 :
    print("Valor inválido, é aceito entre 3 à 10 lados")

else:
    if lado == 3:
        print("triângulo")
    elif lado == 4:
        print("quadrilátero")
    elif lado == 5:
        print("pentágono")
    elif lado == 6:
        print("hexágono")
    elif lado == 7:
        print("heptágono")
    elif lado == 8:
        print("octógono")
    elif lado == 9:
        print("eneágono")
    else:
        print("decágono")     



