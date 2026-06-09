import random

def criar_cartela():
    return {
        'B': random.sample(range(1,  16), 5),
        'I': random.sample(range(16, 31), 5),
        'N': random.sample(range(31, 46), 5),
        'G': random.sample(range(46, 61), 5),
        'O': random.sample(range(61, 76), 5),
    }

def exibir_cartela(cartela):
    print(f"{'B':>4} {'I':>4} {'N':>4} {'G':>4} {'O':>4}")
    print("-" * 24)
    for i in range(5):
        linha = [cartela[letra][i] for letra in 'BINGO']
        print(f"{linha[0]:>4} {linha[1]:>4} {linha[2]:>4} {linha[3]:>4} {linha[4]:>4}")

def cartela_vencedora(cartela):
    matriz = [[cartela[letra][i] for letra in 'BINGO'] for i in range(5)]

    for linha in matriz:
        if sum(linha) == 0:
            return True

    for col in range(5):
        if sum(matriz[linha][col] for linha in range(5)) == 0:
            return True

    if sum(matriz[i][i] for i in range(5)) == 0:
        return True

    if sum(matriz[i][4 - i] for i in range(5)) == 0:
        return True

    return False

def main():
    c1 = criar_cartela()
    c1['B'][2] = 0; c1['I'][2] = 0; c1['N'][2] = 0; c1['G'][2] = 0; c1['O'][2] = 0
    print(" Linha horizontal zerada ")
    exibir_cartela(c1)
    print(f"Vencedora: {cartela_vencedora(c1)}\n")  

    c2 = criar_cartela()
    c2['N'] = [0, 0, 0, 0, 0]
    print(" Coluna vertical zerada (N) ")
    exibir_cartela(c2)
    print(f"Vencedora: {cartela_vencedora(c2)}\n")  

    c3 = criar_cartela()
    for i in range(5):
        c3[list('BINGO')[i]][i] = 0
    print(" Diagonal principal zerada ")
    exibir_cartela(c3)
    print(f"Vencedora: {cartela_vencedora(c3)}\n")  

    c4 = criar_cartela()
    c4['B'][0] = 0; c4['I'][2] = 0; c4['O'][4] = 0
    print(" Zeros cruzados (não vencedora) ")
    exibir_cartela(c4)
    print(f"Vencedora: {cartela_vencedora(c4)}\n")  

main()