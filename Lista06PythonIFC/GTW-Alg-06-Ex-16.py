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
 
 
def main():
    expressao = input("Digite uma expressão infixa: ")
    tokens = tokenizar(expressao)
    print("Tokens:", tokens)
 
    resultado = infix_para_postfix(tokens)
    print("Forma pós-fixada:", " ".join(resultado))
 
 
main()