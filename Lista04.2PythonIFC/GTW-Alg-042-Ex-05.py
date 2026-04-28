soma = 0
while True:

    entrada = input("Insira a idade: ")

    if entrada == "":
        break


    else:
        idade = int(entrada)

        if idade <=2:
            soma+=0
        elif idade >=3 and idade<=12:
            soma+= 14
        elif idade >= 65:
            soma+= 18
        else:
            soma+=23

print(f"O valor total dos ingressos seria: R${soma:.2f}")
