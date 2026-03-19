inicial = float(input("Valor inicial depositado na conta: "))
juros = inicial*0.12
um = inicial+juros
dois = inicial+juros*2
tres = inicial+juros*3

print(f"Saldo da conta de investimento após 1 ano: {um:.2f} " )
print(f"Saldo da conta de investimento após 2 anos: {dois:.2f} " )
print(f"Saldo da conta de investimento após 3 anos: {tres:.2f} " )