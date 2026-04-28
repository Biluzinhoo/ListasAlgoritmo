mensagem = input("Insira a mensagem que queira: ")
deslocamento = int(input("Insira o deslocamento que queira: "))
resultado = ""

for c in mensagem:
    if c.isalpha:
        if c.islower():
            base = ord("a")
        else:
            base = ord("A")
        letra = chr((ord(c)-base + deslocamento)%26+base)

        resultado += letra
    
    else:
        resultado += c
print(f"Resultado: {resultado}")