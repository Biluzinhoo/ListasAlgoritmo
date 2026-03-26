num = int(input("Informe um número inteiro de 4 dígitos: "))

d1 = num//1000
d2 = (num%1000)//100
d3 = (num%100)//10
d4 = (num%10)//1

total = d1+d2+d3+d4

print(f"A soma dos díditos é: {total}")