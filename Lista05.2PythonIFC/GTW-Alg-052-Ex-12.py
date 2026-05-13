def senha_valida(senha):

    if len(senha) < 8:
        return False

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False

    for caractere in senha:

        if caractere.isupper():
            tem_maiuscula = True

        elif caractere.islower():
            tem_minuscula = True

        elif caractere.isdigit():
            tem_numero = True

    if tem_maiuscula and tem_minuscula and tem_numero:
        return True
    else:
        return False


def main():

    senha = input("Digite uma senha: ")

    if senha_valida(senha):
        print("Senha válida")
    else:
        print("Senha inválida")


main()