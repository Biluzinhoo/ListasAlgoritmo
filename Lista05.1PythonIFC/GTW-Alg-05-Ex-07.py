import random

def sorteia_dado():
    nume = random.randint(1,6)
    return nume


c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0

 
i = 0
while i < 1000000:  
    resultado = sorteia_dado()
    if resultado == 1:
        c1 += 1
    elif resultado == 2:
        c2 += 1
    elif resultado == 3:
        c3 += 1
    elif resultado == 4:
        c4 += 1
    elif resultado == 5:
        c5 += 1
    else:
        c6 += 1
    i += 1    


print(f"Número 1: {c1} vezes")
print(f"Número 2: {c2} vezes")
print(f"Número 3: {c3} vezes")
print(f"Número 4: {c4} vezes")
print(f"Número 5: {c5} vezes")
print(f"Número 6: {c6} vezes")