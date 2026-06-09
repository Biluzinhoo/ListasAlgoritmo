abaixo = []
medio = []
acima = []
soma = []
i=1
while True:
    nota = input("Informe as notas: ")
    if nota == "":
        break
    soma.append(float(nota))

media = sum(soma) / len(soma)  
print(f"Média: {media}")

for nota in soma:             
    if nota > media:
        acima.append(nota)
    elif nota == media:
        medio.append(nota)
    else:
        abaixo.append(nota)

print("\nNotas abaixo da média:")
for n in abaixo:
    print(n)

print("\nNotas na média:")
for n in medio:
    print(n)

print("\nNotas acima da média:")
for n in acima:
    print(n)