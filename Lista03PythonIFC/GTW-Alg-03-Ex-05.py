mes = input("Informe um mês do ano: ").lower()

dias_mes ={
    "janeiro":31,
    "fevereiro":"28 ou 29",
    "março":31,
    "abril":30,
    "maio":31,
    "junho":30,
    "julho":31,
    "agosto":31,
    "setembro":30,
    "outubro":31,
    "novembro":30,
    "dezemvro":31
}

if mes in dias_mes :
    print(f"O mês de {mes} tem {dias_mes[mes]} dias")
else:
    print("Mês inválido")