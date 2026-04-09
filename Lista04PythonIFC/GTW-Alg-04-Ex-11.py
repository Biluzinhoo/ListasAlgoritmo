
n = int(input("informe um número: "))
i= 1
a= 0

while i<=n:
    if i%2==0:
        a -= 1/i
    else:
        a += 1/i
    i+=1

print(f"O resultado deu: {a:.4f}")