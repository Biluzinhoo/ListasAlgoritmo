import math

r=float(input("Digite o valor do Raio da circunferência: "))

area= math.pi*r**2
volume= (4/3) * math.pi*r**3

print(f"O valor da área do círculo é {area:.2f} e do volume é {volume:.2f}")