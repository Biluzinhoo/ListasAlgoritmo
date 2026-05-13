def char_para_valor(c):

    c = c.upper()

    if c >= "0" and c <= "9":
        return ord(c) - ord("0")

    else:
        return ord(c) - ord("A") + 10


def valor_para_char(v):

    if v >= 0 and v <= 9:
        return chr(v + ord("0"))

    else:
        return chr(v - 10 + ord("A"))


def base_para_decimal(numero, base):

    decimal = 0
    potencia = 0

    numero = numero[::-1]

    for c in numero:

        valor = char_para_valor(c)

        decimal += valor * (base ** potencia)

        potencia += 1

    return decimal


def decimal_para_base(numero, base):

    if numero == 0:
        return "0"

    resultado = ""

    while numero > 0:

        resto = numero % base

        resultado = valor_para_char(resto) + resultado

        numero = numero // base

    return resultado


def main():

    numero = input("Digite o número: ")

    base_origem = int(input("Digite a base de origem (2 a 16): "))

    base_destino = int(input("Digite a base de destino (2 a 16): "))

    decimal = base_para_decimal(numero, base_origem)

    resultado = decimal_para_base(decimal, base_destino)

    print("Resultado:", resultado)


main()