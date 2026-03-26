centavostotal = int(input("Informe o valor de centavos (0 à 99): "))

cinquenta = centavostotal//50
resto = centavostotal%50


vintecinco = resto//25
resto = resto%25


dez = resto//10
resto = resto%10

cinco = resto//5
resto = resto%5

um = resto

print(f"Moedas de 50 centavos: {cinquenta}")
print(f"Moedas de 25 centavos: {vintecinco}")
print(f"Moedas de 10 centavos: {dez}")
print(f"Moedas de 5 centavos: {cinco}")
print(f"Moedas de 1 centavos: {um}")