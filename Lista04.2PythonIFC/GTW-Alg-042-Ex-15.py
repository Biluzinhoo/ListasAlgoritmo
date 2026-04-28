q = int(input("Digite um número decimal: "))

resultado = ""

while q > 0:
    r = q % 2
    resultado = str(r) + resultado
    q = q // 2

print(f"Em binário: {resultado}")