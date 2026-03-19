import math


a = int(input("Coloque o valor de a: "))
b = int(input("Coloque o valor de b: "))

soma=a+b
diferenca = a-b
produto = a*b
quociente = a//b
resto = a%b
logaritmo = math.log10(a)
potencia = a**b

print(f"A soma é: {soma}")
print(f"A diferença é: {diferenca}")
print(f"O produto é: {produto}")
print(f"O quociente é: {quociente}")
print(f"O resto é: {resto}")
print(f"O logaritmo é: {logaritmo}")
print(f"a potência é: {potencia}")