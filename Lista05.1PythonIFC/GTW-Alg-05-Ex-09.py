def eh_bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400==0:
        print("É um ano bissexto")
    else: 
        print("Não é um ano bissexto")

ano = int(input("Digite um ano: "))

eh_bissexto(ano)