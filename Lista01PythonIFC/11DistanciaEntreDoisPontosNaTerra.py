import math


lat1= float(input("Informe a latitude do ponto 1: "))
log1= float(input("Informe a longitude do ponto 1: "))
lat2= float(input("Informe a latitude do ponto 2: "))
log2= float(input("Informe a longitude do ponto 2: "))

lat1 = math.radians(lat1)
log1 = math.radians(log1)
lat2 = math.radians(lat2)
log2 = math.radians(log2)

distancia = 6371.01 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(log1 - log2))

print(f"a distância entre os dois pontos é de: {distancia:.2f}km")