def buscaReversa(dicio,n):
    chaves = []
    for chave, val in dicio.items():
        if val == n:
            chaves.append(chave)
    return chaves
    
def main():
    estoque={"maçã": "fruta",
             "alface":"vegetal",
             "cenoura": "legume",
             "banana": "fruta"
             }
    resultado = buscaReversa(estoque,"fruta")
    print(f"VAlores das frutas: {resultado}")

    resultado = buscaReversa(estoque,"legume")
    print(f"VAlores das frutas: {resultado}")

    resultado = buscaReversa(estoque,"grão")
    print(f"VAlores das frutas: {resultado}")

main()