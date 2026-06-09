lista_num = []
while True:
    num = int(input("Escreva o número: "))
    if num == 0:        
        lista_num.sort()
        for n in lista_num:
            print(n)
        break
    else:
        lista_num.append(num) 
        
   
    