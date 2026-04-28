while True:

    bits = input("Insira as sequencias de bit: ")

    if bits == "":
        break

    if len(bits) != 8:
        print("Erro, deve ter 8 bits")
        continue

    if bits.count("1") + bits.count("0") != 8:
        print("Erro, só valores 0 e 1 são permitidos")
        continue

    qtd_1 = bits.count("1")

    if qtd_1 % 2 == 0:
        pariedade = "0"
    else:
        pariedade = "1"

    print(f"Bit de pariedade em par é: {pariedade}")