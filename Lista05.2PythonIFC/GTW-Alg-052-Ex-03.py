PRIMEIRO_ITEM = 10.95
DEMAIS_ITENS = 2.95

def calcular_envio(qtd_itens):
    if qtd_itens <= 0:
        return 0

    total = PRIMEIRO_ITEM + (qtd_itens - 1) * DEMAIS_ITENS
    return total

def main():
    quantidade = int(input("Digite a quantidade de itens: "))

    valor_envio = calcular_envio(quantidade)

    print(f"Valor do envio: R$ {valor_envio:.2f}")

main()