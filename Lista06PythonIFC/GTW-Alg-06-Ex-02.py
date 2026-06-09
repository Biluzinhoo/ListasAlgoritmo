lista_num = []

while True:
    num = int(input("Insira um número: "))
    if num == 0:
        lista_num.sort(reverse=True)
        for n in lista_num:
            print(n)
        break
    else:
        lista_num.append(num)