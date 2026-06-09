def precedencia(operador):
    if operador == "+" or operador == "-":
        return 1
    elif operador == "*" or operador == "/":
        return 2
    elif operador == "^":
        return 3
    else:
        return -1
 
 
def main():
    operador = input("Digite um operador (+, -, *, /, ^): ")
    resultado = precedencia(operador)
 
    if resultado == -1:
        print(f"Erro: '{operador}' não é um operador válido.")
    else:
        print(f"A precedência do operador '{operador}' é {resultado}.")
 
 
main()