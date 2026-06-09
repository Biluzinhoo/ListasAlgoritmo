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
 
 
def main():
    expressao = input("Digite uma expressão matemática: ")
    resultado = tokenizar(expressao)
    print("Tokens:", resultado)
 
 
main()
 