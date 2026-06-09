import string

def sem_caractere(t):
    lista_texto = []
    palavra_atual = ""

    for caractere in t:
        if caractere not in string.punctuation and caractere != " ":
            palavra_atual += caractere 
        else:
            if palavra_atual != "":
                lista_texto.append(palavra_atual) 
                palavra_atual = ""

    if palavra_atual != "": 
        lista_texto.append(palavra_atual)

    return lista_texto

def main():
    t = input("Escreva uma frase: ")
    resultado = sem_caractere(t)
    print(resultado) 

main()