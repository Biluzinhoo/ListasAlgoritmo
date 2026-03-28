num = float(input("Insira um número inteiro de anos cronológicos: "))

if num < 0 :
    print("Por favor insira um valor positivo")
else:
    if num <= 2:
        num=num*10.5
        print(f"A conversão para anos caninos deu: {num:.1f}")
    else:
        num=(2*10.5)+(num-2)*4
        print(f"A conversão para anos caninos deu: {num:.1f}")

