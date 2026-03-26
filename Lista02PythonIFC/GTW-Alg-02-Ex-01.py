seg = int(input("Digite os segundos:"))
min = int(input("Digite os minutos:"))
hora = int(input("Digite as horas:"))
dia = int(input("Digite os dias:"))

total= seg + min*60 + hora*3600 + dia*86400

print(f"O valor total em segundos é: {total}")