def conta_elementos(lista):
    if len(lista) == 0:
        return 0
    else:
        return 1 + conta_elementos(lista[1:]) 
   
print(conta_elementos([1, 2, 3, 4]))
        
        