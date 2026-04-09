n = int(input("Insira o número para o cálculo: "))
num = 0
for i in range(1,n+1):
    print(num)
    num += (n-i+1)/i

print(f"O valor de A é: {num:.2f}")