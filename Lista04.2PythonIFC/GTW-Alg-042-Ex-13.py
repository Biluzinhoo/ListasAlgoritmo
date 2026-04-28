n = int(input("Digite um número inteiro (maior ou igual a 2):"))


if n < 2: 
    print(f"ERRO, Valor menor que 2")

else:
    fator = 2
    while fator <= n:
        if n%fator==0:
            n = n//fator
            print(f"{fator}")

        else:
            fator+=1
