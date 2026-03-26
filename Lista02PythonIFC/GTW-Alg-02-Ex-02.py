segtotal = int(input("Insira o valor de segundos para que assim seja transformado no modelo DD:HH:MM:SS: "))

dias = segtotal//86400
resto= segtotal % 86400

horas =resto//3600
resto = resto%3600

min = resto//60
seg = resto%60

print(f"{dias}:{horas:02d}:{min:02d}:{seg:02d}")
