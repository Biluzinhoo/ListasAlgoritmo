
soma = 0
i = 1
print("Informe 10 números: ")
while i <= 10:
    num = int(input())
    soma+=num
    if i == 1:
        max = num
        min = num

    else:
       if num > max:
           max =num
       if num < min:
           min = num
           
    i +=1
media = soma/10


print(f"O maior número foi: {max}\nO menor número foi: {min}\nA média foi: {media}" )

