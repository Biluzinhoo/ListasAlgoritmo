def buscaReversa(dic,valor):
    resultado = []
    for char,val in dic.items():
        if val == valor:
            resultado.append(char)
        
    return resultado           

def main():
    dic = {"Ana":1,"João":1,"Paula":2}
    valor = int(input("Escreva um valor: "))
    print(buscaReversa(dic,valor))

main()