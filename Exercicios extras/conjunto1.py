def verificar(s):
    s.lower()

    if len(s) == len(set(s)): #set remove as duplicatas
        return True
    else: 
        return False

s = input("Escreba uma palavra: ")
print(verificar(s))