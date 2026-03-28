v = int(input("Informe um volume em decibéis: "))

if v > 130 or v < 40:
    print("Volume inválido. Insira um valor entre 40 e 130 dB")

else:
    if v == 40:
        print("Nível do barulho: Sala silenciosa")
    elif v >40 and v <70:
        print("Nível do barulho: Entre sala silenciosa e despertador ")
    elif v == 70:
        print("Nível do barulho: Despertador ")
    elif v >70 and v <106:
        print("Nível do barulho: Entre despertador e cortador de grama")
    elif v == 106:
        print("Nível do barulho: Cortador de grama ")
    elif v >106 and v <130:
        print("Nível do barulho: Entre cortador de grama e britadeira")
    elif v == 130:
        print("Nível do barulho: Britadeira")
    