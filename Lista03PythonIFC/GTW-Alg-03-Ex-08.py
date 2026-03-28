nota = input("Digite a nota (ex: C4): ").upper()

notas = "CDEFGAB"
frequencias = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]

if len(nota) == 2 and nota[0] in notas and nota[1].isdigit():
    i = notas.index(nota[0])
    oitava = int(nota[1])

    if 0 <= oitava <= 8:
        freq = frequencias[i] * 2 ** (oitava - 4)
        print(f"{freq:.2f} Hz")
    else:
        print("Nota inválida")
else:
    print("Nota inválida")