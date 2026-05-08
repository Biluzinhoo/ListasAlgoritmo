soma = 0
i = 0



while True:
    enter = input("Digite uma nota (ou pressione Enter para sair): ")
    
    if enter == "":
        break
    
    num = float(enter)
    
    soma += num
    i += 1
    
    if i == 1:
        max = num
        min = num
    else:
        if num > max:
            maior = num
        if num < min:
            min = num

if i > 0:
    media = soma / i
    print(f"Média: {media}")
    print(f"Maior nota: {max}")
    print(f"Menor nota: {min}")
else:
    print("Nenhuma nota foi informada.")