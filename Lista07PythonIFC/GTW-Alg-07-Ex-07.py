import random

def criar_cartela():
    cartela = {
        'B': random.sample(range(1,  16), 5),
        'I': random.sample(range(16, 31), 5),
        'N': random.sample(range(31, 46), 5),
        'G': random.sample(range(46, 61), 5),
        'O': random.sample(range(61, 76), 5),
    }
    return cartela

def exibir_cartela(cartela):
    print(f"{'B':>4} {'I':>4} {'N':>4} {'G':>4} {'O':>4}")
    print("-" * 24)

    for i in range(5):
        linha = [cartela[letra][i] for letra in 'BINGO']
        print(f"{linha[0]:>4} {linha[1]:>4} {linha[2]:>4} {linha[3]:>4} {linha[4]:>4}")

def main():
    cartela = criar_cartela()
    exibir_cartela(cartela)

main()