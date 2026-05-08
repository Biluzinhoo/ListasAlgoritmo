def potencia(x,y):
    i = 0
    resultado = 1
    while i < y:
        resultado *= x
        i += 1
    return resultado

x = float(input("Informe o valor de X: "))
y = float(input("Informe o valor de Y: "))

print(f"O valor da potenciação é: {potencia(x,y):.2f}")
