def simetrico(M,N):
    diferenca = []
    resultado = M ^ N
    return sorted(resultado)

def main():
    M = {2,4,5,9}
    N = {2,4,11,12}
    print(simetrico(M,N))

main()