num = int(input("Informe um número inteiro de 3 dígitos: "))

C = num//100
D = (num%100)//10
U = (num%10)

print(f"Ordem inversa: {U}{D}{C}")
