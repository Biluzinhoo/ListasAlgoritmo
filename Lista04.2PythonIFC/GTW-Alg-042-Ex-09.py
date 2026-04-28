x = float(input("Informe o valor  de x: "))

if x == 0:
    print("divisão por 0")

else:    
    raiz = x/2

    while abs(raiz*raiz - x) >= 10**-12:
        media = (raiz + x/raiz)/2
        raiz = media

    print(f"Raiz aproximada: {raiz}")
