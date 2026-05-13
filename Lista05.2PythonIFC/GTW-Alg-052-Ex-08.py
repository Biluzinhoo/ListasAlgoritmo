def corrigir_maiusculas(texto):

    resultado = ""
    maiuscula = True

    for caractere in texto:

        if maiuscula and caractere != " ":
            resultado += caractere.upper()
            maiuscula = False
        else:
            resultado += caractere

        if caractere == "." or caractere == "!" or caractere == "?":
            maiuscula = True

    return resultado


def main():

    frase = input("Digite uma frase: ")

    frase_corrigida = corrigir_maiusculas(frase)

    print("Resultado:")
    print(frase_corrigida)


main()