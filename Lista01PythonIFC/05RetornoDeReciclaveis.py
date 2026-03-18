pequeno = int(input("Quantos recipientes pequenos serão reciclados?: "))
grande = int(input("Quantos recipientes grandes serão reciclados?: "))

credito = pequeno*0.10 + grande*0.25

print(f"Crédito recebido: R$ {credito:.2f}" )