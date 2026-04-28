
valores = [4.95, 9.95, 14.95, 19.95, 24.95 ]
print("Preço Original\t\tValor de desconto\t\tValor com desconto")
for i in range(5):
    desconto = valores[i]*0.60
    precofinal = valores[i]-desconto
    print(f"R${valores[i]:.2f}\t\t\tR${desconto:.2f}\t\t\t\tR${precofinal:.2f}")
    
