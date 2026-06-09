def divisores (n):
    numeros = []
    i=1
    while i < n:
        if n%i==0:
            numeros.append(i)
        i =i+1

    return numeros

def perfeitos (numeros,n):
    if sum(numeros) == n:
        return True
    else:
        return False

def main():
    n = 1
    while n <10000:
        resultado=divisores(n)
        if perfeitos(resultado,n):
            print(n)
        n=n+1
main()
