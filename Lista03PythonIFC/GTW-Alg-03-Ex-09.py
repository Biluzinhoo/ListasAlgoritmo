mes = input("Digite o mês: ").lower()
dia = int(input("Digite o dia: "))

if mes == "janeiro" and dia == 1:
    print("Confraternização Universal")
elif mes == "abril" and dia == 21:
    print("Tiradentes")
elif mes == "maio" and dia == 1:
    print("Dia do Trabalho")
elif mes == "setembro" and dia == 7:
    print("Independência do Brasil")
elif mes == "outubro" and dia == 12:
    print("Nossa Senhora Aparecida")
elif mes == "novembro" and dia == 2:
    print("Finados")
elif mes == "novembro" and dia == 15:
    print("Proclamação da República")
elif mes == "dezembro" and dia == 25:
    print("Natal")
else:
    print("Não é feriado nacional.")