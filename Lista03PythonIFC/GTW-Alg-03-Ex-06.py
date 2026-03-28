a = int(input("Informe o comprimento do lado a: "))
b = int(input("Informe o comprimento do lado b: "))
c = int(input("Informe o comprimento do lado c: "))

if a == b and a == c and b==c:
    print("Triângulo equilátero")
elif a != b and a != c and b!= c:
    print("Triângulo escaleno")
else:
    print("Triângulo isóceles")    