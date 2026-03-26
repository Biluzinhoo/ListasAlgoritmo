data = int(input("Informe a data nesse formato DDMMAA, exp:111111 (11 de novembro de 2011): "))

dia = data//10000
mes = (data%10000)//100
ano = (data%100)

print(f"Data no formato AAMMDD: {ano:02d}{mes:02d}{dia:02d}")
