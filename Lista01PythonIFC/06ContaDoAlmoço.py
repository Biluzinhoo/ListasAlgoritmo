prato = float(input("Insira o valor do prato: R$ " ))
sobremesa = float(input("Insira o valor da sobremesa: R$ " ))
suco = float(input("Insira o valor do suco: R$ " ))

subtotal = prato+suco+sobremesa
servico = subtotal*0.10
total = subtotal+ servico

print(f"O valor total do almoço foi de: R${total: .2f}")