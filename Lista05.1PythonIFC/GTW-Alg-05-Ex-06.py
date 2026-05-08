import random

def sorteia_dado():
    nume = random.randint(1,6)
    return nume

resultado = sorteia_dado()
print(f"Valor do dado: {resultado}")