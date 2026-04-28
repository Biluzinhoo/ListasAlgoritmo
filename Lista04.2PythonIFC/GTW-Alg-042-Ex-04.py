import math

perimetro = 0

x1 = input("Digite a coordenada x de um ponto: ")

if x1 != "":
    x1 = float(x1)
    y1 = float(input("Digite a coordenada y de um ponto: "))

    x_inicial = x1
    y_inicial = y1

    while True:
        x2 = input("Digite a coordenada x de um ponto (enter para sair): ")

        if x2 == "":
            distancia = math.sqrt((x_inicial - x1)**2 + (y_inicial - y1)**2)
            perimetro += distancia
            break

        x2 = float(x2)
        y2 = float(input("Digite a coordenada y de um ponto: "))

        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        perimetro += distancia

        x1 = x2
        y1 = y2

    print(f"O perímetro deste polígono é igual a {perimetro}")