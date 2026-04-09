num = 0
quad = 0
cubo = 0

print("Número\t\tQuadrado\t\tCubo")
for i in range(11):
    print(f"{num}\t\t{quad}\t\t{cubo}")
    num +=1
    quad = num**2
    cubo = num**3
