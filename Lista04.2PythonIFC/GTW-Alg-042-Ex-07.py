pi = 3
sinal = 1
n = 2
print(f"1° valor de pi: {pi}")

for i in range (2, 16):
    termo = 4/(n*(n+1)*(n+2))
    pi += sinal*termo
    print(f"{i}° valor de pi: {pi}")
    sinal *= -1
    n+=2

