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
    print(f"| {'B':<4} {'I':<4} {'N':<4} {'G':<4} {'O':<4}|")
    print("-" * 34)
    for i in range(5):
        linha = [cartela[letra][i] for letra in 'BINGO']
        print(f"| {linha[0]:<4} {linha[1]:<4} {linha[2]:<4} {linha[3]:<4} {linha[4]:<4}|")
    print("-" * 34)

def cartela_vencedora(cartela):
    matriz = [[cartela[letra][i] for letra in 'BINGO'] for i in range(5)]
    for linha in matriz:
        if sum(linha) == 0:
            return True
    for col in range(5):
        if sum(matriz[lin][col] for lin in range(5)) == 0:
            return True
    if sum(matriz[i][i]     for i in range(5)) == 0:
        return True
    if sum(matriz[i][4 - i] for i in range(5)) == 0:
        return True
    return False

def gerar_sorteio():
    numeros = list(range(1, 76))
    random.shuffle(numeros)
    return numeros

def zerar_numero(cartela, numero):
    faixas = {'B': range(1,16), 'I': range(16,31), 'N': range(31,46),
              'G': range(46,61), 'O': range(61,76)}
    for letra, faixa in faixas.items():
        if numero in faixa and numero in cartela[letra]:
            idx = cartela[letra].index(numero)
            cartela[letra][idx] = 0
            return

def simular_partida():
    cartela = criar_cartela()
    sorteio = gerar_sorteio()
    for chamadas, numero in enumerate(sorteio, start=1):
        zerar_numero(cartela, numero)
        if cartela_vencedora(cartela):
            return chamadas, cartela

def main():
    resultados = []
    cartela_minima = None
    menor_chamadas = float('inf')

    for _ in range(1000):
        chamadas, cartela = simular_partida()
        resultados.append(chamadas)

        if chamadas < menor_chamadas:
            menor_chamadas = chamadas
            cartela_minima = cartela

    print(f"Mínimo: {min(resultados)}")
    print(f"Médio:  {sum(resultados)/len(resultados):.1f}")
    print(f"Máximo: {max(resultados)}")
    print("-" * 34)
    print("Cartela que venceu mais rápido:")
    exibir_cartela(cartela_minima)

main()