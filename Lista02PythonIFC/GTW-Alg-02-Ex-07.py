num = int(input("Informe um número inteiro de 3 dígitos: "))

C = num//100
D = (num%100)//10
U = (num%10)//1

print(f"Centena: {C}\nDezena: {D}\nUnidade: {U}\n")
