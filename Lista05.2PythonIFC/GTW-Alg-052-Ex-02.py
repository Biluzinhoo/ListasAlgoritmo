BANDEIRADA = 4.00
VALOR_POR_140M = 0.25
DISTANCIA_TRECHO = 140  # em metros

def calcular_tarifa(distancia_km):
    distancia_metros = distancia_km * 1000

    trechos = distancia_metros / DISTANCIA_TRECHO

    total = BANDEIRADA + (trechos * VALOR_POR_140M)

    return total

def main():
    distancia = float(input("Digite a distância percorrida em km: "))

    valor = calcular_tarifa(distancia)

    print(f"Valor da corrida: R$ {valor:.2f}")

main()