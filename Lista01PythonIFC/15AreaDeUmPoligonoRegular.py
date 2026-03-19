import math


l = float(input("Insira o valor do lado: "))
n = int(input("Insira o número de lados: "))

area = (n*l**2)/(4*math.tan(math.pi/n))

print(f"O valor da area do polígono regular é: {area:.2f}")