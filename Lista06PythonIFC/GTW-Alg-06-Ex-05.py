zero = []
positivos= []
negativos = []
while True:
    num = input("Insira um número: ")
    if num == "":
        for n in negativos:
            print(n)
        for n in zero:
            print(n)
        for n in positivos:
            print(n)
        break
    else:
        num = int(num)
        if num > 0:
            positivos.append(num)
        elif num == 0:
            zero.append(num)
        else:
            negativos.append(num)