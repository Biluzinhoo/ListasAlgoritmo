def agrupa_por_inicial(palavras):
    separacao= {}
    for palavra in palavras:
        letra = palavra[0]
        if letra in separacao:
            separacao[letra].append(palavra)
        else:
            separacao[letra] = [palavra]

    return separacao
palavras = ["banana", "abacaxi", "uva", "abacate", "berinjela"]
print(agrupa_por_inicial(palavras))