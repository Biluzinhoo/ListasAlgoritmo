import random

total = 0

for rodada in range(10):
    consecutivos = 0
    ultimo = ""
    sorteios = 0

    while consecutivos < 3:
        moeda = random.choice(["A", "O"])
        print(moeda, end=" ")
        sorteios += 1

        if moeda == ultimo:
            consecutivos += 1
        else:
            consecutivos = 1

        ultimo = moeda

    total += sorteios
    print(f"({sorteios} sorteios)")

media = total / 10
print(f"\nNa média, foram necessários {media:.1f} sorteios.")