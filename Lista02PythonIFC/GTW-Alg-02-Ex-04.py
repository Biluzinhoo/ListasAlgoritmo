num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o tercceiro número: "))


min= min(num1,num2,num3)
max = max(num1,num2,num3)

meio = num1+num2+num3-max-min

print(f"{min}\n{meio}\n{max}")

