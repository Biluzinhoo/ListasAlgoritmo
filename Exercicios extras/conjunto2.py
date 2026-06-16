def diferenca(m,n):
    intersecao = m.intersection(n)
    novo_m = m - intersecao
    novo_n = n - intersecao
    resultado = list(novo_m.union(novo_n))
    return sorted(resultado)
m = {2, 4, 5, 9}
n ={2, 4, 11, 12}
print(diferenca(m,n))