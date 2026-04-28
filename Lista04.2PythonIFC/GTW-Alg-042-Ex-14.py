bi = input("Escreva um número em binário para ser convertido: ")

resultado = 0
for i in bi:
    resultado = resultado *2 + int(i)
print(f"{resultado}")
