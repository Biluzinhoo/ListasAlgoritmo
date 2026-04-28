i = 0
soma = 0 

num = float(input("Insira o valor para o calculo(Escreva 0 para interromper o programa): "))
if num == 0:
    print(f"Erro, valor 0 digitado primeiro")

else:
    while num != 0 :
        num = float(input("Insira o valor para o calculo(Escreva 0 para interromper o programa): "))
        i+=1
        soma +=num
        
    media = soma/i

    print(f"A média é: {media: .2f}")
