print("Para calcular a área do terreno precisamos dos valores da profundidade e largura")
pronfundidade = float(input("Qual é a profundidade do terreno? (em metros): "))
largura = float(input("Qual é a largura do terreno? (em metros): "))

area = pronfundidade * largura
hectar = area/10000

print(f"A área do terreno é {hectar:.4f} hectares.")