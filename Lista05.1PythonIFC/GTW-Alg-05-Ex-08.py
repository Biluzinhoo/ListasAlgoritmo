def num_digitos(n):
    return len(str(n))
    

n = int(input("Digite um número inteiro: "))

if n < 0:
    print("Erro, número precisa ser maior que 0")

Quantidade = num_digitos(n)

print(f"Quantidade de dígitos: {Quantidade}")