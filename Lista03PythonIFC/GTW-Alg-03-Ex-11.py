import math


a = float(input("Informe o valor de 'a' da função quadrática: "))
b = float(input("Informe o valor de 'b' da função quadrática: "))
c = float(input("Informe o valor de 'c' da função quadrática: "))

delta = b**2-4*a*c

if delta < 0:
    print("Não possui raízes reais")

elif delta == 0:
    raiz = (-b+math.sqrt(0))//(2*a)
    print(f"Tem apenas um raíz real: x={raiz:.2f}")

else:
    raiz1 = (-b+math.sqrt(delta))//(2*a)
    raiz2 = (-b-math.sqrt(delta))//(2*a)
    print(f"Apresenta duas raízes reais: x1={raiz1:.2f} e x2={raiz2:.2f}")
