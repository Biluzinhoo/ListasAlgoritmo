def hex2int(digito):
    digito = digito.upper()

    if digito == "0":
        return 0
    elif digito == "1":
        return 1
    elif digito == "2":
        return 2
    elif digito == "3":
        return 3
    elif digito == "4":
        return 4
    elif digito == "5":
        return 5
    elif digito == "6":
        return 6
    elif digito == "7":
        return 7
    elif digito == "8":
        return 8
    elif digito == "9":
        return 9
    elif digito == "A":
        return 10
    elif digito == "B":
        return 11
    elif digito == "C":
        return 12
    elif digito == "D":
        return 13
    elif digito == "E":
        return 14
    elif digito == "F":
        return 15
    else:
        return -1


def int2hex(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    elif numero == 2:
        return "2"
    elif numero == 3:
        return "3"
    elif numero == 4:
        return "4"
    elif numero == 5:
        return "5"
    elif numero == 6:
        return "6"
    elif numero == 7:
        return "7"
    elif numero == 8:
        return "8"
    elif numero == 9:
        return "9"
    elif numero == 10:
        return "A"
    elif numero == 11:
        return "B"
    elif numero == 12:
        return "C"
    elif numero == 13:
        return "D"
    elif numero == 14:
        return "E"
    elif numero == 15:
        return "F"
    else:
        return ""


def main():
    h = input("Digite um dígito hexadecimal: ")
    n = int(input("Digite um número entre 0 e 15: "))

    print("hex2int:", hex2int(h))
    print("int2hex:", int2hex(n))


main()