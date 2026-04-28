import unicodedata

frase = input("Digite uma frase: ")

frase_limpa = ""

for c in frase:
    if c.isalnum():
        c = unicodedata.normalize("NFD", c)
        c = "".join(letra for letra in c if unicodedata.category(letra) != "Mn")
        
        frase_limpa += c.lower()

i = 0
fim = len(frase_limpa) - 1
palindromo = True

while i < fim:
    if frase_limpa[i] != frase_limpa[fim]:
        palindromo = False
        break
    
    i += 1
    fim -= 1

if palindromo:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")