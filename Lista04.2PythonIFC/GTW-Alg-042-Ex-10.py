palavra = input("Digite uma palavra: ")

i = 0
fim = len(palavra) - 1
palindromo = True

while i < fim:
    if palavra[i] != palavra[fim]:
        palindromo = False
        break
    
    i += 1
    fim -= 1

if palindromo:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")