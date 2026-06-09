def precedencia(operador):
    if operador == "+" or operador == "-":
        return 1
    elif operador == "*" or operador == "/":
        return 2
    elif operador == "^":
        return 3
    else:
        return -1


def tokenizar(expressao):
    tokens = []
    token_atual = ""
    ultimo_relevante = ""

    for caractere in expressao:
        if caractere == " ":
            continue
        elif caractere.isdigit():
            token_atual += caractere
            ultimo_relevante = caractere
        elif caractere in "()*/^":
            if token_atual != "":
                tokens.append(token_atual)
                token_atual = ""
            tokens.append(caractere)
            ultimo_relevante = caractere
        elif caractere in "+-":
            if ultimo_relevante.isdigit() or ultimo_relevante == ")":
                if token_atual != "":
                    tokens.append(token_atual)
                    token_atual = ""
                tokens.append(caractere)
            else:
                token_atual += caractere
            ultimo_relevante = caractere

    if token_atual != "":
        tokens.append(token_atual)

    return tokens


def infix_para_postfix(tokens):
    operadores = []
    postfix = []

    for token in tokens:
        if token.lstrip("+-").isdigit():
            postfix.append(token)
        elif precedencia(token) > 0:
            while (len(operadores) > 0 and
                   operadores[-1] != "(" and
                   precedencia(token) <= precedencia(operadores[-1])):
                postfix.append(operadores.pop())
            operadores.append(token)
        elif token == "(":
            operadores.append(token)
        elif token == ")":
            while operadores[-1] != "(":
                postfix.append(operadores.pop())
            operadores.pop()

    while len(operadores) > 0:
        postfix.append(operadores.pop())

    return postfix


def avaliar_postfix(postfix):
    valores = []

    for token in postfix:
        if token.lstrip("+-").isdigit():
            valores.append(int(token))
        else:
            direita = valores.pop()
            esquerda = valores.pop()

            if token == "+":
                valores.append(esquerda + direita)
            elif token == "-":
                valores.append(esquerda - direita)
            elif token == "*":
                valores.append(esquerda * direita)
            elif token == "/":
                valores.append(esquerda / direita)
            elif token == "^":
                valores.append(esquerda ** direita)

    return valores[0]


def main():
    expressao = input("Digite uma expressão matemática: ")

    tokens  = tokenizar(expressao)
    postfix = infix_para_postfix(tokens)
    resultado = avaliar_postfix(postfix)

    print(f"Forma pós-fixada: {' '.join(postfix)}")
    print(f"Resultado: {resultado}")


main()