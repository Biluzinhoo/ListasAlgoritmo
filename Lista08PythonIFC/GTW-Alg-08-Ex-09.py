"""x = float(input("Informe o valor  de x: "))

if x == 0:
    print("divisão por 0")

else:    
    raiz = x/2

    while abs(raiz*raiz - x) >= 10**-12:
        media = (raiz + x/raiz)/2
        raiz = media

    print(f"Raiz aproximada: {raiz}")"""

def raiz_quadrada(n, estimativa = 1.0):
    if abs(estimativa**2-n) <= 10**-12:
        return estimativa
    nova_estimativa = (estimativa+(n/estimativa))/2
    return raiz_quadrada(n, nova_estimativa )

def main ():
    print(raiz_quadrada(2))
    print(raiz_quadrada(16))
    print(raiz_quadrada(100))
    print(raiz_quadrada(0.25))

main()


    